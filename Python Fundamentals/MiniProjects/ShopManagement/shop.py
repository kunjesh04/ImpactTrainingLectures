class Shop:
    def __init__(self):
        self.inventory = {}
    
    def run(self):
        while True:
            print("\n1: Inventory")
            print("2: Search by ID")
            print("3: Search by Name")
            print("4: Buy From Vendor")
            print("5: Sell to Customer")
            print("6: Stop")
            option = input("Select Option: ")
            if option == "1":
                self.showInventory()
            elif option == "2":
                self.searchByID()
            elif option == "3":
                self.searchByName()
            elif option == "4":
                self.buyFromVendor()
            elif option == "5":
                self.sellToCustomer()
            elif option == "6":
                print("ATM Exited")
                break
            else:
                print("Enter Valid Option")
    
    def showInventory(self):
        for product, info in self.inventory.items():
            print(product, info)
    
    def searchByID(self):
        pID = int(input('Enter ID to search for : '))
        for product, prodInfos in self.inventory.items():
            if pID == prodInfos['ID']:
                print(prodInfos)
                return prodInfos
            else:
                print('Product NOT found')
            
    def searchByName(self):
        pName = input('Enter Name to search for : ')
        pName = pName.capitalize()
        for product, prodInfos in self.inventory.items():
            if pName == prodInfos['Name']:
                print(prodInfos)
                return prodInfos
            else:
                print('Product NOT found')
    
    def buyFromVendor(self):
        Name = 'Product '+str(len(self.inventory))
        
        info = {}
        
        pID = int(input('Enter ID : '))
        info["ID"] = pID
        
        allIds = []
        for product, prodInfos in self.inventory.items():
            allIds.append(prodInfos['ID'])
        
        if pID in allIds:
            print('ID already exists!')
            return    
            
        pName = input('Enter Name : ')
        info["Name"] = pName.capitalize()
        
        pQty = int(input('Enter Units to buy : '))
        info["Qty"] = pQty
        
        pPrice = int(input('Enter Price Per Unit : '))
        info["Price Per Unit"] = pPrice 
        
        self.inventory[Name] = info
        print(f'{Name} [{info["Name"]}] purchased') 
    
    def sellToCustomer(self):
        opt = int(input('You need to locate the product first with ID (Enter 1) or Name (Enter 2)'))
        if opt == 1 :
            purchaseProdInfo = self.searchByID()
        elif opt == 2:
            purchaseProdInfo = self.searchByName()
        else :
            print('Invalid Option Selected')
            return
        purProd = [prod for prod in self.inventory if self.inventory[prod]==purchaseProdInfo]
        purQty = int(input('Enter Qty in units : '))
        if purQty > purchaseProdInfo['Qty']:
            print('Not enough quantity')
            return
        newInfo = purchaseProdInfo
        newInfo['Qty'] = purchaseProdInfo['Qty'] - purQty
        self.inventory[purProd[0]] = newInfo
        print('Purchase Successful\n Bill : \n')
        print(f'ID : {purchaseProdInfo["ID"]}')
        print(f'Name : {purchaseProdInfo["Name"]}')
        print(f'Qty : {purQty}')
        print(f'Price Per Unit : {purchaseProdInfo["Price Per Unit"]}')
        print(f'Total Price : {purQty*purchaseProdInfo["Price Per Unit"]}')
        
        
shop = Shop()
shop.run()