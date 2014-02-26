import sys
import data_model
import sim_model

class Recom :
    def __init__(self, simres, data) :
        self.simres = simres
        self.data = data
    def recom(self, uid) :
        print "sim, ",  self.simres.usimRes[uid]
        topfriend = sorted(self.simres.usimRes[uid].iteritems(), key=lambda d:d[1], reverse=True)[:30]
        print topfriend
        cands = dict() 
        for k, v in topfriend :
            for iid,score in self.data.udata[k] :
                cands.setdefault(iid, 0.0)
                cands[iid] += v*score
        print cands
        topcands = sorted(cands.iteritems(), key = lambda d:d[1], reverse=True)[:30]
        print cands['394']
        print cands['828']
        print cands['164']

if __name__ == "__main__" :
    data = data_model.Data()
    data.load(sys.argv[1])
    simres = sim_model.SimRes(data)
    simres.calall()
    print simres.getusim(1,2)
    print simres.getusim(1,3)
    print simres.getusim(3,2)
    recom = Recom(simres, data)
    recom.recom(1)
    print data.udata[1]
