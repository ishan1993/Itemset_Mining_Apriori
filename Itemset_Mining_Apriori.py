#!/usr/local/bin/python3

from itertools import combinations
minsup = 771
f = []
tdb = []

def initial_parse():
    with open('categories.txt') as fp:
        for line in fp:
            line = line.split('\n')[0]
            tdb.append(line.split(';'))

def gen_c1():
    initial_parse()
    raw_list = []
    c1 = []
    for elem in tdb:
        for cat in elem:
            raw_list.append(cat)
    unique_list = list(set(raw_list))
    unique_list.sort()
    for elem in unique_list:
        sup = 0
        for cat in raw_list:
            if cat == elem:
                sup = sup+1
        c1.append([sup,elem])
    return c1
    
def dump_f1(f1):
    with open('patterns.txt','a') as fw:
        for elem in f1:
            fw.write(str(elem[0])+":"+elem[1]+"\n")

def gen_fk(ck):
    fk = []
    for elem in ck:
        if(elem[0] > minsup):
            fk.append(elem)
    return fk
    
def gen_ckplus1(fk,x):
    for elem in fk:
        elem.remove(elem[0])
    print("\nfk: " + str(len(fk)))
    print (fk[0:5])
    f_items = []
    for elem in fk:
        f_items = f_items + elem
    f_items = set(f_items)
    f_items = list(f_items)
    print("\nf_items: " + str(len(f_items)))
    print (f_items[0:5])
    
    lkplus1 = list(combinations(f_items, len(fk[0])+1))
    i = 0
    while i < len(lkplus1):
        lkplus1[i] = list(lkplus1[i])
        i=i+1
    print("\nlkplus1: " + str(len(lkplus1)))
    print(lkplus1[0:5])
    
    #prune
    for elem in lkplus1:
        j = 0     
        i = 0
        raw_list = list(combinations(elem, len(elem)-1))
        while i < len(raw_list):
            raw_list[i] = list(raw_list[i])
            i=i+1
        for cat_list in raw_list:
            for item in fk:
                if (all(i in item for i in cat_list)):
                    j = j+1
                    break
        if j<len(raw_list):
            lkplus1.remove(elem)
    
    #dbscan
    ckplus1 = []
    print("\nlkplus1 after pruning: " + str(len(lkplus1)))
    print(lkplus1[0:5])
    for elem in lkplus1:
        sup = 0
        for cat_list in tdb:
            if (all(i in cat_list for i in elem)):
                sup = sup + 1
        ckplus1.append([sup]+list(elem))
    print("\nckplus1: " + str(len(ckplus1)))
    print(ckplus1[0:5])
    return ckplus1


c1 = gen_c1()
f1 = gen_fk(c1)
f = f + f1
print ("k=2")
c2 = gen_ckplus1(f1,0)
f2 = gen_fk(c2)
f = f + f2
print("\nf2: " + str(len(f2)))
print(f2[0:5])
print ("\n\n\n\nk=3")
c3 = gen_ckplus1(f2,0)