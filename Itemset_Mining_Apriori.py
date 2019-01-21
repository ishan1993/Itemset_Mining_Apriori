#!/usr/bin/python3

minsup = 771

def initial_parse():
    tdb = []
    with open('categories.txt') as fp:
        for line in fp:
            line = line.split('\n')[0]
            tdb.append(line.split(';'))
    return tdb

def gen_c1():
    tdb = initial_parse()
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

def dbscan(strings,db):
    sup = 0
    for elem in strings:
        for trans in db:
           sup = sup+1
    
    return sup

c1 = gen_c1()
f1 = gen_fk(c1)