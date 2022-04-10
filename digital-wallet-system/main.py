from controllers.wallet_controller import WalletController


class Driver:

    def __init__(self) -> None:
        self.wService = WalletController()
        
    
    def startServer(self):        
        
        while True:
            print("\nOPTIONS:")
            print("1. Create wallet")
            print("2. Transfer Amount")
            print("3. Account Statement")
            print("4. Overview")
            print("5. Exit")

            option = int(input())

            if option == 1:
                print("YOU SELECTED CREATE WALLET")
                print("Enter name")
                name = input()
                print("Enter amount")
                amount = float(input())
                self.wService.createWallet(name, amount)
                
                
            elif option == 2:
                print("YOU SELECTED TRANSFER")
                print("Enter SENDER account number")
                frm = int(input())
                print("Enter RECEIVER account number")
                to = int(input())
                print("Enter amount")
                amount1 = float(input())
                self.wService.transafer(frm, to, amount1)
                
            
            elif option == 3:
                print("YOU SELECTED ACCOUNT STATEMENT")
                print("Enter account num")
                self.wService.statement(int(input()))
                
            
            elif option == 4:
                print("YOU SELECTED OVERVIEW")
                self.wService.overview()
                
                
            elif option == 5:
                print("APPLICATION STOPPED")
                break
                
            else:
                print("YOU HAVE SELECTED INVALID OPTION. PLEASE REENTER")
                break
            

if __name__ == "__main__":
    startServer = Driver()
    startServer.startServer()