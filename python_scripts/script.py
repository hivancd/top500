import json

def read_file(filename):
    lista = []
    with open(filename) as file:
        for line in file:
            lista.append(line.split('  '))
    return lista

a = read_file('C:\\Users\\Chihe\\Desktop\\top500\\txt\\top5002021.txt')

# print(a)
for e in a:
    e = e[0].split('\t')
    if('\n'in e[3]):
        e[3] = e[3][0:4]
    print(json.dumps(e), end=', \n')
    # print(e[3])
    # if(1==1):
    #     print('[')
    #     for i in range(len(e)):
    #         if(('(details...)') not in e[i]):
    #             print('"'+ e[i] +'"', end='')
    #             print(',')
    #     print('],')      
    
    