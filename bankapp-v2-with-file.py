class Account:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if self.balance < amount:
            print("Insufficient funds..!! -\nNew balance ==>", self.balance)
            return False
        else:
            self.balance -= amount
            print("Withdrawal successful -\nNew balance ==>", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful -\nNew balance ==>", self.balance)

    def transfer(self, amount, beneficiary):

        print("\n\nATTEMPTING TRANSFER TO ", beneficiary.username, "\n\n")
        if self.withdraw(amount) == False:
            return False
        else:
            beneficiary.account.deposit(amount)

        print(beneficiary.username, "RECIEVED ", amount, ".")

    def display_balance(self):
        print(self.balance)
    # CODE TO FIN A USER IN A FILE AND UPDATE THEIR DETAILS

    
class User:
    
    def __init__(self, username):
        self.username = username

        age, gender, account = self.get_details()
        self.age = age
        self.gender = gender
        self.account = account

    def get_details(self):
        data = open("users.csv", "r").readlines()

        for line in data:

            splitted_data = line.split(",")

            username = splitted_data[0]
            age = splitted_data[1]
            gender = splitted_data[2]
            pin = splitted_data[3]
            balance = splitted_data[4]

            if username == self.username:
                print("Account loaded")
                print("YAY..!!!! FOUND HIM ==> ", username)

                return age, gender, Account(int(balance))

    def display_details(self):
        print(f"\n\nACCOUNT NAME - {self.username}\n\nUSER AGE - {self.age}\n\nACCOUNT BALANCE - {self.account.balance}")

    def update_balance(self):

        file = open("users.csv", "r")
        data= file.readlines()

        updated_data = []

        for line in data:

            splitted_data = line.split(",")

            username = splitted_data[0]
            age = splitted_data[1]
            gender = splitted_data[2]
            pin = splitted_data[3]
            balance = splitted_data[4]

            if username == self.username:
                print("FOUND USER")
                print("UPDATING BALANCE FROM", balance, "TO", self.account.balance)
                splitted_data[4] = str(self.account.balance) + "\n"
                updated_data.append(splitted_data)
            else:
                updated_data.append(splitted_data)
        
        file.close()

        file = open("users.csv", "w")

        for line in updated_data:
            line = ",".join(line)
            file.write(line)

        file.close()
    


Alero = User("Alero")
Alero.account.deposit(2000)
Alero.account.withdraw(12000)
Alero.update_balance()

# john = User("john", 23, "m")
# Alamu.account.transfer(23000, john)

# sophia = User("sophia", 40, "f")
# sophia.account.transfer(15000, john)

# john.account.display_balance()

# Alero.display_details()


# # CODE TO FIN A USER IN A FILE AND UPDATE THEIR DETAILS

# def update_balance(self_username, new_balance):

#     file = open("users.csv", "r")
#     data= file.readlines()

#     updated_data = []

#     for line in data:

#         splitted_data = line.split(",")

#         username = splitted_data[0]
#         age = splitted_data[1]
#         gender = splitted_data[2]
#         pin = splitted_data[3]
#         balance = splitted_data[4]

#         if username == self_username:
#             print("FOUND USER")
#             print("UPDATING BALANCE FROM", balance, "TO", new_balance)
#             splitted_data[4] = str(new_balance) + "\n"
#             updated_data.append(splitted_data)
#         else:
#             updated_data.append(splitted_data)
    
#     file.close()

#     file = open("users.csv", "w")

#     for line in updated_data:
#         line = ",".join(line)
#         file.write(line)

#     file.close()

            
# update_balance("lizzy", 5000000)