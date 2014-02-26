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

class SimRes :
    def __init__(self, data) :
        self.data = data
        self.usimRes = dict()
        self.isimRes = dict()
    def getusim(self, uidx, uidy) :
        if uidx == uidy :
            return 1.0
        return self.usimRes[uidx][uidy]
    def getisim(self, iidx, iidy) :
        return self.isimRes[iidx][iidy]
    def calusim(self, uidx, uidy) :
        return consin_cal(self.data.udata[uidx], self.data.udata[uidy])
    def calisim(self, iidx, iidy) :
        return consin_cal(self.data.idata[iidx], self.data.idata[iidy])
    def calall(self) : 
        for sk, sv in self.data.udata.iteritems() :
            for tk, tv in self.data.udata.iteritems() :
                if sk == tk :
                    continue
                self.usimRes.setdefault(sk, dict())
                self.usimRes[sk][tk] = self.calusim(sk, tk)
        for sk, sv in self.data.idata.iteritems() :
            for tk, tv in self.data.idata.iteritems() :
                if sk == tk :
                    continue
                self.isimRes.setdefault(sk, dict())
                self.isimRes[sk][tk] = self.calisim(sk, tk)

