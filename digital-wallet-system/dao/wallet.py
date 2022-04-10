from typing import Dict
from models.account import Account


class WalletDAO:

    def __init__(self) -> None:
        self.accountMap: Dict[int,Account] = dict()
    
    def getAccountMap(self):
        return self.accountMap
    
    def setAccountMap(self,accountMap: Dict[int,Account]):
        self.accountMap = accountMap