#!/usr/bin/python3

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
    
def gen_l(f):
    f_items=[]
    for elem in f:
        f_items = f_items + elem[1:]
    return list(combinations(f_items, len(f[0])))
    
def gen_ckplus1(fk,x):
    print("fk: " + str(len(fk)))
    f_items = []
    for elem in fk:
        f_items.append(list(elem[1:]))
    print("f_items: " + str(len(f_items)))
    lkplus1 = gen_l(fk)
    print("lkplus1: " + str(len(lkplus1)))
    ckplus1 = []
    #prune
    for elem in lkplus1:
        raw_list = list(combinations(elem, len(elem)-1))
        for cat_list in raw_list:
            l = list(cat_list)
            l = l[0:len(l)-2]
            if l not in f_items:
                lkplus1.remove(elem)
                break
    #dbscan
    print("lkplus1: " + str(len(lkplus1)))
    for elem in lkplus1:
        sup = 0
        for cat_list in tdb:
            if (all(i in cat_list for i in list(elem))):
                sup = sup + 1
        ckplus1.append([sup]+list(elem))
    print("ckplus1: " + str(len(ckplus1)))
    return ckplus1
            
c1 = gen_c1()
f1 = gen_fk(c1)
f = f + f1
print ("k=2")
c2 = gen_ckplus1(f1,0)
f2 = gen_fk(c2)
f = f + f2
print("k=3")
c3 = gen_ckplus1(f2,1)
f3 = gen_fk(c3)
print f3