# 2043 - Simple Bank System
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.balance.insert(0,0)

    def validAccount(self, account):
        valid = account >= 0 and account < len(self.balance)
        #print("validAccount",account,valid)
        return valid

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.validAccount(account1) or not self.validAccount(account2): return False
        if self.balance[account1] < money:
            #print("Transfer: insufficient funds")
            return False
        self.balance[account1] -= money
        self.balance[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self.validAccount(account): return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.validAccount(account): return False
        if self.balance[account] < money:
            #print("withdraw: insufficient funds")
            return False
        self.balance[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
