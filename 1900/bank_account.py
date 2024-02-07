'''
This class represents a bank account.  Exciting times!
'''
class BankAccount:
	# Constructor - allows us to specify the owner, initial balance, account
	#  type, and interest rate
	def __init__(self, owner, balance, is_savings, rate):
		self.owner = owner 				# Name of account owner
		self.balance = balance 			# Current account balance		
		self.is_savings = is_savings	# False for checking, True for savings
		self.interest_rate = rate 		# As a percentage (e.g., 1 for 1%)

		acct_type = 'savings' if self.is_savings else 'checking'
		print(f'Created a new {acct_type} account for {self.owner} with balance ${self.balance:.2f}, interest rate {self.interest_rate}%.')

	# Deposits the specified amount into the account
	def deposit(self, amount):
		if amount <= 0:
			print('Deposit amount must be positive.  No changes to account made.')
		else:
			self.balance += amount
			print(f"Deposited ${amount:.2f} into {self.owner}'s account, new balance is ${self.balance:.2f}.")

	# Withdraws the specified amount from the account
	def withdraw(self, amount):
		if amount <= 0:
			print('Withdraw amount must be positive.  No changes to account made.')
		elif amount > self.balance:
			print('Withdraw amount exceeds available balance.  No changes to account made.')
		else:
			self.balance -= amount
			print(f"Withdrew ${amount:.2f} from {self.owner}'s account, new balance is ${self.balance:.2f}.")

	# Modifies the interest rate of the account by the specified amount, as a
	#  percentage
	def adjust_interest_rate(self, amount):
		self.interest_rate += amount
		print(f"Changed interest rate on {self.owner}'s account by {amount}%, new interest rate is {self.interest_rate}%.")

	# Makes one annual interest payment to the account, based on the current
	#  balance and interest_rate
	def pay_interest(self):
		interest = self.interest_rate / 100 * self.balance;
		self.balance += interest
		print(f"Made interest payment of ${interest:.2f} to {self.owner}'s account, new balance is ${self.balance:.2f}.")

#initialize new objects
new_savings = BankAccount('Poor College Student', 0, True, .4)
new_checking = BankAccount('Scrooge Mcduck', 75000, False, .01)

#adjust amounts and interest rates for each object
new_savings.deposit(1000)
new_checking.withdraw(30000)
new_savings.adjust_interest_rate(.3)
new_checking.adjust_interest_rate(.01)

#apply annual interest to objects
new_savings.pay_interest()
new_checking.pay_interest()
























