class Bank:
    print('Welcome to ABC bank')
    bal = 10000 

    def deposit(self):
        amt = int(input('Enter amount to be deposited: '))
        min_amt = 100
        max_amt = 50000
        if min_amt <= amt <= max_amt and amt % 100 == 0:
            print(f'Amount deposited: {amt}')
            self.bal += amt
            print(f'Total balance: {self.bal}')
        else:
            print('Deposit failed. Amount must be between 100 and 50000, and a multiple of 100.')

    def withdraw(self):
        count=0  
        while count< 3:
            choice = int(input('Enter 1 to withdraw money or 0 to cancel: '))
            if choice==1:
              amt1 = int(input('Enter the withdrawal amount: '))
              min_amt = 100
              mul = amt1 % 100
              limit = 20000
              min_bal = 500
              if amt1 <= self.bal and amt1 <= limit and mul == 0 and (self.bal - amt1) >= min_bal:
                  self.bal -= amt1
                  print(f'Total balance after withdrawal: {self.bal}')
                  count+=1 
              else:
                  print('Enter a valid amount. Check withdrawal conditions.')
             
              if count==3:
                print('You have reached the maximum number of withdrawal attempts for today.')
                break
            elif choice==0: 
               print('withdrawal cancelled')
               break
            else:
               print('enter valid input')

    def option(self):
        while True:
            print('\n1. Deposit')
            print('2. Withdraw')
            print('3. Balance Inquiry')
            print('4. Exit')
            opt = int(input('Enter your choice: '))
            if opt == 1:
                self.deposit()
            elif opt == 2:
                self.withdraw()
            elif opt == 3:
                self.balance_inquiry()
            elif opt == 4:
                print('Exiting...')
                break
            else:
                print('Invalid option, please try again.')

    def checkpin(self):
        pin = int(input('Enter pin number: '))
        if pin == 1234:
            print('Correct pin entered')
            self.option()
        else:
            for i in range(1, 4):
                if i > 1:
                    print('Invalid pin entered. Try again.')
                    pin = int(input('Enter pin number: '))
                if pin == 1234:
                    print('Correct pin entered')
                    self.option()
                    break
                if i == 3:
                    print('Invalid pin entered. Your account is blocked for today.')

obj = Bank()
obj.checkpin()
