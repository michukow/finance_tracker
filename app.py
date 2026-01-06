# Personal finance tracker - work in progres

transactions=[]

def add():
	print("Adding transaction...")
	amount = float(input("Amount: "))
	type = str(input("Type (income/expense): ")).lower()
	description = input("Description: ")

	transaction = {
		"amount": amount,
		"type": type,
		"description": description
	}

	transactions.append(transaction)
	print("Transaction added.\n")

def show():
	print("Showing transactions...")
	if not transactions:
		print("No transactions yet.\n")
		return

	for i,t in enumerate(transactions, start=1):
		print(f"{i}. {t['type']} | {t['amount']} | {t['description']}\n")

def main():
	while True:
		print("=== MENU ===")
		print("1. Add transaction")
		print("2. Show transactions")
		print("3. Exit")

		choice = input("Choose option: ")

		if choice=="1":
			add()
		elif choice=="2":
			show()
		elif choice=="3":
			print("Exiting.")
			break
		else:
			print("Invalid option.\n")

if __name__ == "__main__":
    main()