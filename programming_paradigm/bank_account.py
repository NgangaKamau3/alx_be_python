#Implement a BankAccount class that encapsulates banking operations. 
# This will only contain the methods, without any user interaction code.

import sys

class BankAccount:
	"""Ä simple bank account class that supports deposits, withdrawals, and balance inquiries."""
	def __init__(self, account_balance=0):
		"""Initialize the bank account with an optional initial balance."""
		self.balance = account_balance

	def deposit(self, amount):
		"""Deposit a specified amount into the account."""
		if amount > 0:
			self.balance += amount
			return True
		else:
			return False

	def withdraw(self, amount):
		"""Withdraw a specified amount from the account if sufficient funds are available."""
		if 0 < amount <= self.balance:
			self.balance -= amount
			return True
		else:
			return False

	def display_balance(self):
		"""Display the current balance of the account."""
		return self.balance
