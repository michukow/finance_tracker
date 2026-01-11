# Personal finance tracker - work in progres
import json
import matplotlib.pyplot as plt
from datetime import datetime


class Transaction:
	def __init__(self,amount,description,date,category):
		self.amount=amount
		self.description=description
		self.date=date
		self.category=category

	def to_dict(self):
		return self.__dict__

	def info(self):
		print(f"{self.category} || {self.amount} | {self.description} | {self.date}")

def add():
	print("Adding transaction...")
	while True:
		try:
			amount=float(input("Amount: "))
			if amount==0:
				print("Insert valid amount.")
				continue 
			break
		except ValueError:
			print("Insert a number.")

	while True:
		try:
			description=input("Description: ")
			if description=="":
				print("The description should not be empty.")
				continue
			break
		except ValueError:
			print("Insert a number.")

	date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	if amount>0:
		category="INCOME"
	else:
		category="EXPENSE"

	transaction=Transaction(amount,description,date,category)

	try:
		with open("transactions.json","r",encoding="utf-8") as file:
			data=json.load(file)
			if not isinstance(data, list):
				data=[]
	except FileNotFoundError:
		data=[]
	data.append(transaction.to_dict())
	try:
		with open("transactions.json","w",encoding="utf-8") as file:
			json.dump(data,file,indent=4,ensure_ascii=False)
		print("Transaction added.\n")
	except FileNotFoundError:
		print("File not found.")

def show():
	print("Showing transactions...")
	try:
		with open("transactions.json","r",encoding="utf-8") as file:
			data=json.load(file)

		if not isinstance(data, list) or not data:
			print("No transactions yet.\n")
			return

		for i,t in enumerate(data,start=1):
			transaction=Transaction(t["amount"],t["description"],t["date"],t["category"])
			print(f"{i}. ",end="")
			transaction.info()

	except FileNotFoundError:
			print("File not found.")

def balance():
	try:
		with open('transactions.json','r',encoding='utf-8') as file:
			data=json.load(file)

			if not data:
				print("No transactions yet.\n")
				return
			else:
				total = sum(t["amount"] for t in data)
				print(f"Current balance: {total:.2f}\n")

	except FileNotFoundError:
			print("File not found.")

def delete():
    try:
        with open("transactions.json","r",encoding="utf-8") as file:
            data=json.load(file)

        if not data:
            print("No transactions.")
            return

        for i, t in enumerate(data,start=1):
            transaction=Transaction(t["amount"],t["description"],t["date"],t["category"])
            print(f"{i}. ",end="")
            transaction.info()

        while True:
            try:
                i=int(input("Enter transaction number to delete: "))-1
                if i<0 or i>=len(data):
                    print("Invalid number. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        removed=data.pop(i)

        with open("transactions.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

        print("Transaction removed.")

    except FileNotFoundError:
        print("File not found.")

def update():
    try:
        with open("transactions.json","r",encoding="utf-8") as file:
            data=json.load(file)

        if not data:
            print("No transactions.")
            return

        for i,t in enumerate(data,start=1):
            transaction=Transaction(t["amount"],t["description"],t["date"],t["category"])
            print(f"{i}. ",end="")
            transaction.info()

        while True:
            try:
                i=int(input("Enter transaction number to edit: "))-1
                if i<0 or i>=len(data):
                    print("Invalid number. Try again.")
                    continue
                break
            except ValueError:
                print("Please enter a number.")

        old=data[i]

        new_amount=input("New amount OR press Enter to keep: ")
        if new_amount!= "":
            try:
                old["amount"]=float(new_amount)
                old["category"]="INCOME" if old["amount"]>0 else "EXPENSE"
            except ValueError:
                print("Invalid amount.")
                return


        new_description=input("New description OR press Enter to keep: ")
        if new_description!="":
            old["description"]=new_description

        old["date"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("transactions.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

        print("Transaction updated.")

    except FileNotFoundError:
        print("File not found.")


def chart():
	incomes=[]
	expenses=[]
	with open("transactions.json","r",encoding="utf-8") as file:
		data=json.load(file)
		if not data:
			print("Chart can not be drawn.")
			return

		for t in data:
			if t["amount"]>0:
				incomes.append(t["amount"])
			else:
				expenses.append(abs(t["amount"]))

	total_income=sum(incomes)
	total_expense=sum(expenses)

	labels=["Income","Expenses"]
	values=[total_income,total_expense]

	plt.bar(labels,values)
	plt.title("Income vs Expenses")
	plt.ylabel("Amount")
	plt.show()

def main():
	while True:
		print()
		print("=== MENU ===")
		print("1. Add transaction")
		print("2. Show transactions")
		print("3. Show balance")
		print("4. Delete transaction")
		print("5. Update specific transaction")
		print("6. Draw the chart")
		print("7. Exit")
		print()

		choice=str(input("Choose option: "))

		if choice=="1":
			add()
		elif choice=="2":
			show()
		elif choice=="3":
			balance()
		elif choice=="4":
			delete()
		elif choice=="5":
			update()
		elif choice=="6":
			chart()
		elif choice=="7":
			break
		else:
			print("Invalid option. Try again! \n")

if __name__ == "__main__":
    main()