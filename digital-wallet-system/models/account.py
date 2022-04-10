from models.user import User
from utills.account_number_generetor import AccountNumberGenerator
from sortedcontainers import SortedSet
class Account:

    def __init__(self,name,amount) -> None:
        self.accountNumber = AccountNumberGenerator.getNextAccountNumber()
        self.user = User(name)
        self.balance = amount
        self.transaction = SortedSet()
        
    def getAccountInfo(self):
        return "Account [accountNumber=" + str(self.accountNumber) + ", name=" + str(self.user.getName()) + ", balance=" + str(self.balance) + ", tranactions=" + str(self.transaction) + "]"

    def getAccountNumber(self):
        return self.accountNumber
    
    def setAccountNumber(self,accountNumber: int):
        self.accountNumber = accountNumber
    
    def getUser(self):
        return self.user
    
    def setUser(self,user: User):
        self.user = user
    
    def getBalance(self):
        return self.balance
    
    def setBalance(self,balance: float):
        self.balance = balance
    
    def getTransaction(self):
        return self.transaction
    
    def setTransaction(self,transaction: set):
        self.transaction = transaction