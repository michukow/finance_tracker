# Personal finance tracker - work in progres
import json
from datetime import datetime

class Transaction:
    def __init__(self,amount,description,date):
        self.amount=amount
        self.description=description
        self.date=date

    def to_dict(self):
    	return self.__dict__

    def show(self):
    	print(f"{self.amount} | {self.description} | {self.date}")

def add():
	print("Adding transaction...")
	amount=float(input("Amount: "))
	description=input("Description: ")

	date=datetime.now()
	date=date.strftime("%Y-%m-%d %H:%M:%S")
	transaction=Transaction(amount,description,date)

	try:
		with open("transactions.json","r",encoding="utf-8") as file:
			data=json.load(file)
			if not isinstance(data, list):
				data=[]
	except FileNotFoundError:
		data=[]
	data.append(transaction.to_dict())
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

    for i,t in enumerate(data,start=1):
    	transaction = Transaction(t["amount"], t["description"], t["date"])
    	print(f"{i}. ", end="")
    	transaction.show()



def balance():
	with open('transactions.json','r',encoding='utf-8') as file:
		data=json.load(file)

		if not data:
			print("No transactions yet.\n")
			return
		else:
			total = sum(t["amount"] for t in data)
			print(f"Current balance: {total:.2f}\n")

def delete():
    with open("transactions.json","r",encoding="utf-8")as file:
        data=json.load(file)

    if not data:
        print("No transactions.\n")
        return

    for i,t in enumerate(data,start=1):
        print(f"{i}. {t['amount']} | {t['description']} | {t['date']}")

    try:
        index=int(input("Enter transaction number to delete: ")) - 1
        if index<0 or index>=len(data):
            print("Invalid number.\n")
            return
    except ValueError:
        print("Invalid input.\n")
        return

    removed=data.pop(index)

    with open("transactions.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

    print(f"Removed: {removed['amount']} | {removed['description']}\n")

def main():
	while True:
		print()
		print("=== MENU ===")
		print("1. Add transaction")
		print("2. Show transactions")
		print("3. Show balance")
		print("4. Delete transaction")
		print("5. Exit")
		print()

		choice=input("Choose option: ")

		if choice=="1":
			add()
		elif choice=="2":
			show()
		elif choice=="3":
			balance()
		elif choice=="4":
			delete()
		elif choice=="5":
			print("Exiting.")
			break
		else:
			print("Invalid option.\n")

if __name__ == "__main__":
    main()