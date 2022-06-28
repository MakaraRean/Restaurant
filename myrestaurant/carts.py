class Cart():
    _victualID=[]
    _qty=[]

    def getID(self):
        return self._victualID

    def getQty(self):
        return self._qty

    def setItem(self,qty,victualID):
        self._qty.append(qty)
        self._victualID.append(victualID)