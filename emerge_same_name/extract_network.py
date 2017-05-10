import codecs
import json
mess = {}
size = 0
sizeo = 0
network= {}
len_net = 0


index_of_author = set()


def add_networks(dic1, key_a, key_b, val):
    if key_a in dic1:
        dic1[key_a].update({key_b: val})
    else:
        dic1.update({key_a: {key_b: val}})

with codecs.open('./inter_res/author_with_aff.txt', 'r', encoding='utf-8', errors='ignore') as f1:
    for line in f1:
        items = line.rstrip().split(' ', 2)
        index_of_author.add(items[2])

# print(index_of_author)

with codecs.open('../../aminernetwork/AMiner-Paper.txt', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if line != '\n':
            line1 = line[:-1].split(' ', 1)
            if len(line1) <= 1:
                continue
            line2 = line1[1].split(';')
            for i in range(0, len(line2)):
                mess[line1[0]+str(i)] = line2[i]

        if line[:2] == '#@':
            size = len(line[3:-1].split(';'))
        if line[:2] == '#o':
            sizeo = len(line[3:-1].split(';'))
        if line == '\n':

            for i in range(min(size,sizeo)):
                for j in range(i+1,min(size,sizeo)):
                    # print('1')
                    if mess['#@'+str(i)]+':'+mess['#o'+str(i)] in index_of_author and \
                        mess['#@' + str(j)] + ':' + mess['#o' + str(j)] in index_of_author and mess['#o'+str(i)] != '' and mess['#o'+str(j)] != '':
                        # print (str(mess['#@'+str(i)]+':'+mess['#o'+str(i)]))
                        # s1=set()
                        # s2=set()
                        # s1.add(mess['#o'+str(i)])
                        # s2.add(mess['#o'+str(j)])
                        
                        # t1=mess['#@'+str(i)],s1
                        # t2=mess['#@'+str(j)],s2
                        # if t1[1] and t2[1]:
                        #     add_networks(network,t1,t2,1)
                        #     add_networks(network,t2,t1,1)
                       

                        # print(t2)

                        if mess['#@'+str(i)]+':'+mess['#o'+str(i)]  not in network or mess['#@'+str(j)]+':'+mess['#o'+str(j)] not in network \
                        or mess['#@'+str(i)]+':'+mess['#o'+str(i)] not in network[mess['#@'+str(j)]+':'+mess['#o'+str(j)]]\
                        or mess['#@'+str(j)]+':'+mess['#o'+str(j)] not in network[mess['#@'+str(i)]+':'+mess['#o'+str(i)]]:

                            add_networks(network,mess['#@'+str(i)]+':'+mess['#o'+str(i)],mess['#@'+str(j)]+':'+mess['#o'+str(j)],1)
                            add_networks(network,mess['#@' + str(j)] + ':' + mess['#o' + str(j)],mess['#@' + str(i)] + ':' + mess['#o' + str(i)], 1)
                        else: 
                            network[mess['#@'+str(i)]+':'+mess['#o'+str(i)]][mess['#@'+str(j)]+':'+mess['#o'+str(j)]]+=1
                            network[mess['#@'+str(j)]+':'+mess['#o'+str(j)]][mess['#@'+str(i)]+':'+mess['#o'+str(i)]]+=1 



            mess = {}

            size = 0
            sizeo = 0



fr = open('./inter_res/network_dict_with_conumbers.json', 'w',encoding = 'utf-8',errors='ignore')
json.dump(network,fr,ensure_ascii=False)

