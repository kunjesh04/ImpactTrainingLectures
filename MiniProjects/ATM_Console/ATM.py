class ATM:
    def __init__(self):
        self.balance = 20000
        self.history = []

    def run(self):
        while True:
            print("\n1: Withdrawal")
            print("2: Deposit")
            print("3: Mini Statement")
            print("4: Exit")
            option = input("Select Option: ")
            if option == "1":
                self.withdrawal()
            elif option == "2":
                self.deposit()
            elif option == "3":
                self.mini_statement()
            elif option == "4":
                print("ATM Exited")
                break
            else:
                print("Enter Valid Option")

    def withdrawal(self):
        amount = int(input("Enter amount (multiples of 100) to be withdrawn: "))
        if amount % 100 != 0:
            print("Amount should be in multiples of 100")
            return
        if amount > self.balance:
            print("Insufficient Balance")
            return
        if amount > 10000:
            otp = input("Enter OTP: ")
            if len(otp) != 4:
                print("Invalid OTP")
                return
        self.balance -= amount
        self.history.append(f"-{amount}")
        print(f"{amount} withdrawn.")
        print("Available Balance:", self.balance)

    def deposit(self):
        amount = int(input("Enter Amount to be deposited: "))
        if amount%100 != 0:
            print('Amount should be in multiple of 100')
            return
        notes_dict = {1: 100, 2: 200, 3: 500}
        print("1: 100\n2: 200\n3: 500")
        note_type = int(input("Enter type of notes: "))
        num_notes = int(input("How many notes will be deposited? "))
        if amount != notes_dict[note_type] * num_notes:
            print("Amount Not matched")
            return
        self.balance += amount
        self.history.append(f"+{amount}")
        print(f"{amount} Deposited")
        print("Available Balance:", self.balance)

    def mini_statement(self):
        prev_transactions = self.history[-5:]
        print("Previous 5 transactions:", prev_transactions)

atm = ATM()
atm.run()
