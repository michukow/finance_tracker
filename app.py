# Personal finance tracker - work in progres
import json

transactions=[]

def add():
	print("Adding transaction...")
	amount=float(input("Amount: "))
	description=input("Description: ")

	transaction={
		"amount":amount,
		"description":description
	}

	try:
		with open("transactions.json","r",encoding="utf-8") as file:
			data=json.load(file)
			if not isinstance(data, list):
				data=[]
	except FileNotFoundError:
		data=[]
	data.append(transaction)
	with open("transactions.json","w",encoding="utf-8") as file:
		json.dump(data,file,indent=4,ensure_ascii=False)
	print("Transaction added.\n")

def show():
    print("Showing transactions...")
    with open("transactions.json","r",encoding="utf-8") as file:
        data=json.load(file)
    if not isinstance(data, list) or not data:
        print("No transactions yet.\n")
        return
    for i, t in enumerate(data,start=1):
        print(f"{i}. {t['amount']} | {t['description']}")
    print()


def balance():
	with open('transactions.json','r',encoding='utf-8') as file:
		data=json.load(file)
		if not data:
			print("No transactions yet.\n")
			return
		else:
			total = sum(t["amount"] for t in data)
			print(f"Current balance: {total:.2f}\n")

def main():
	while True:
		print("=== MENU ===")
		print("1. Add transaction")
		print("2. Show transactions")
		print("3. Show balance")
		print("4. Exit")

		choice=input("Choose option: ")

		if choice=="1":
			add()
		elif choice=="2":
			show()
		elif choice=="3":
			balance()
		elif choice=="4":
			print("Exiting.")
			break
		else:
			print("Invalid option.\n")

if __name__ == "__main__":
    main()