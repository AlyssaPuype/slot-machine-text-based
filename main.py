import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
	'A' : 3,
	'B' : 5,
	'C' : 6,
	'D' : 7,
}

def get_spin(rows, cols, symbols):
	pass

def deposit():
	while True:
		amount = input('Enter deposit amount: $')

		'''Check if input is a positive whole number'''
		if not amount.isdigit():
			print('Enter a number: ')
			continue
		amount = int(amount)
		if amount == 0:
			print('Amount must be greater than 0')
			continue

		return amount

def get_number_of_lines():
	while True:
		lines = input(f'Enter number of lines to bet on (1- {str(MAX_LINES)}): ')
		if not lines.isdigit():
			print('Enter a number: ')
			continue
		lines = int(lines)
		if not 1 <= lines <= MAX_LINES:
			print(f'Enter valid number (1- {str(MAX_LINES)}): ')
			continue

		return lines

def get_bet():
	while True:
		amount = input('Enter bet amount on each line: $')
		if not amount.isdigit():
			print('Enter a number: ')
			continue
		amount = int(amount)
		if not MIN_BET <= amount <= MAX_BET:
			print(f'Amount must be between {MIN_BET} and {MAX_BET}')
			continue

		return amount

def main():
	balance = deposit()
	lines = get_number_of_lines()
	while True:
		bet = get_bet()
		total_bet = bet * lines

		if total_bet > balance:
			print('Your bet is too high')
			break

		print(f'You are betting {bet} on {lines} lines. \nTotal bet = {total_bet} \nCurrent balance =  {balance}')
		print(balance, lines, bet)


main()
