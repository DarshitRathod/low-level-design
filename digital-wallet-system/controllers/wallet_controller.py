from datetime import datetime
from dao.wallet import WalletDAO
from models.account import Account
from models.transaction import Transaction


class WalletController:

    def __init__(self) -> None:
        self.dao = WalletDAO()
    

    def createWallet(self,name,amount):
        account = Account(name, amount)
        accountMap = self.dao.getAccountMap()
        accountMap[account.getAccountNumber()] = account
        print("Account created for user " + name + " with account number " + str(account.getAccountNumber()))

    def transafer(self,frmAccount,toAccount,transferAmount):

        if not self.validate(frmAccount,toAccount,transferAmount):
            return

        tran = Transaction(frmAccount, toAccount, transferAmount, datetime.now())
        fromAccount: Account = self.dao.getAccountMap().get(frmAccount)
        toAccount: Account = self.dao.getAccountMap().get(toAccount)
        if fromAccount.getBalance() < transferAmount:
            print("Insufficient Balance")
            return

        fromAccount.setBalance(float(fromAccount.getBalance() - transferAmount))
        toAccount.setBalance(float(toAccount.getBalance() + transferAmount))
        fromAccount.getTransaction().add(tran)
        toAccount.getTransaction().add(tran)
        print("Transfer Successful")


    def validate(self,frmAccount,toAccount,transferAmount):
        if frmAccount == toAccount:
            print("Sender and Receiver cannot be same.")
            return False
        
        if transferAmount < 0.0001:
            print("Amount too low")
            return False
        
        if not  (frmAccount in self.dao.getAccountMap()):
            print("Invalid Sender account number")
            return False
        
        if not  (toAccount in self.dao.getAccountMap()):
            print("Invalid Receiver account number")
            return False
        
        return True
    
    def statement(self,accountNum):
        account: Account = self.dao.getAccountMap().get(accountNum)
        if(account == None):
            print("Invalid Account Number")
            return
        print("Summary for account number: " + str(accountNum))
        print("Current Balance: " + str(account.getBalance()))
        print("Your Transaction History")
        for i in account.getTransaction():
            print(i.getTransactionInfo())
    
    def overview(self):
        
        for accNum,acc in self.dao.getAccountMap().items():
            print("Balance for account number " + str(accNum) + ": ",end=" ")
            print(self.dao.getAccountMap().get(accNum).getBalance())
            #print(acc.getAccountInfo())

    