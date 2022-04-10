class Transaction:


    def __init__(self, frm , to, amount, date) -> None:
        self.frm = frm
        self.to = to
        self.amount = amount
        self.date = date
    
    def getTransactionInfo(self):
        return  "Transaction [from=" + str(self.frm) + ", to=" + str(self.to) + ", amount=" + str(self.amount) + ", date=" + str(self.date) + "]"

    def getFrom(self):
        return self.frm
    
    def setFrom(self,frm):
        self.frm = frm
    
    def getTo(self):
        return self.to
    
    def setTo(self,to):
        self.to = to
    
    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount = amount
    
    def getDate(self):
        return self.date
    
    def setDate(self,date):
        self.date = date
            