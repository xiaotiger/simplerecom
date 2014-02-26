import sys

class Record :
    def __init__(self, uid, iid, score) :
        self.uid = uid
        self.iid = iid
        self.score = score

def consin_cal(ll, lr) :
    lrd = dict(lr)
    comm = 0.0
    lrc = 0.0
    llc = 0.0
    for k, v in ll :
        llc += v*v
        if k in lrd :
            comm += v * lrd[k]
    for k, v in lr :
        lrc += v*v
    return comm/(lrc + llc)


class Data :
    def __init__(self) :
        self.udata = dict()
        self.idata = dict()
    def add_record(self, r) :
        self.udata.setdefault(r.uid, [])
        self.udata[r.uid].append((r.iid, r.score))
        self.idata.setdefault(r.iid, [])
        self.idata[r.iid].append((r.uid, r.score))
    def load(self, path) :
        fp = open(path) 
        for line in fp :
            items = line.strip().split(" ")
            record = Record(int(items[0]), items[1], float(items[2]))
            self.add_record(record)
            
