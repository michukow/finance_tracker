import json
import matplotlib.pyplot as plt
from datetime import datetime

class Transaction:
	def __init__(self,type,amount,category,description,date):
		self.type=type
		self.amount=amount 
		self.category=category
		self.description=description
		self.date=date

	def to_dict(self):
		return self.__dict__

	def info(self):
		print(f"{self.type} || {self.amount} | {self.category} | {self.description} | {self.date}")

def add():
    print("Adding transaction...")

    while True:
        try:
            amount=float(input("Amount: "))
            if amount==0:
                print("Amount cannot be zero.")
                continue
            break
        except ValueError:
            print("Insert a valid number.")
    while True:
        description=input("Description: ").strip()
        if description=="":
            print("Description cannot be empty.")
        else:
            break

    if amount>0:
        type="INCOME"
        categories={
            "1": "Salary",
            "2": "Business",
            "3": "Investment",
            "4": "Refund",
            "5": "Scholarship",
            "6": "Other"
        }
    else:
        type="EXPENSE"
        categories={
            "1": "Food",
            "2": "Rent",
            "3": "Home",
            "4": "Transport",
            "5": "Fun & Hobby",
            "6": "Other"
        }

    print("\nSelect category:")
    for k, v in categories.items():
        print(f"{k} - {v}")

    while True:
        choice=input("Category number: ")
        if choice in categories:
            category=categories[choice]
            break
        else:
            print("Select a valid category number.")

    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    transaction=Transaction(type,amount,category,description,date)

    try:
        with open("transactions.json","r",encoding="utf-8") as file:
            data=json.load(file)
            if not isinstance(data,list):
                data=[]
    except FileNotFoundError:
        data=[]

    data.append(transaction.to_dict())

    with open("transactions.json","w",encoding="utf-8") as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

    print("Transaction added successfully.")


def show():
	print("Showing transactions...")
	try:
		with open("transactions.json","r",encoding="utf-8") as file:
			data=json.load(file)

		if not isinstance(data, list) or not data:
			print("No transactions yet.\n")
			return

		for i,t in enumerate(data,start=1):
			transaction=Transaction(t["type"],t["amount"],t["category"],t["description"],t["date"])
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
            print("No transactions yet.")
            return

        for i, t in enumerate(data,start=1):
            transaction=Transaction(t["type"],t["amount"],t["category"],t["description"],t["date"])
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
            transaction=Transaction(t["type"],t["amount"],t["category"],t["description"],t["date"])
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
                old["type"]="INCOME" if old["amount"]>0 else "EXPENSE"
            except ValueError:
                print("Invalid amount.")
                return

        if old["type"]=="INCOME":
            categories={
                "1": "Salary",
                "2": "Business",
                "3": "Investment",
                "4": "Refund",
                "5": "Scholarship",
                "6": "Other"
            }
        else:
            categories={
                "1": "Food",
                "2": "Rent",
                "3": "Home",
                "4": "Transport",
                "5": "Fun & Hobby",
                "6": "Other"
            }

        print("Updating category...")
        print("Select category:")
        for k, v in categories.items():
            print(f"{k} - {v}")

        while True:
            choice=input("Insert category number or press Enter to keep: ")
            if choice in categories:
                category=categories[choice]
                old["category"]=category
                break
            else:
                print("Select a valid category number.")


        new_description=input("New description OR press Enter to keep: ")
        if new_description!="":
            old["description"]=new_description

        old["date"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("transactions.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

        print("Transaction updated.")

    except FileNotFoundError:
        print("File not found.")

def month_report():
	incomes=[]
	expenses=[]
	while True:
		try:
			month=input("Insert number of month: ")
			year=input("Insert a year: ")
			if year=="" or int(year)<0 or int(month)<1 or int(month)>12 or month=="":
				continue
			break
		except ValueError:
			print("Insert valid number of year or month.")

	if not month.startswith("0") and int(month)<10:
		month="0"+month
	print(f"Generating month report {month}-{year}")
	print()
	with open("transactions.json","r",encoding="utf-8") as file:
		data=json.load(file)

	for t in data:
		if t["date"].startswith(f"{year}-{month}"):
			if t["amount"]>0:
				incomes.append(t["amount"])
			else:
				expenses.append(abs(t["amount"]))

	total_income=sum(incomes)
	total_expense=sum(expenses)

	print(f"Income: {total_income}")
	print(f"Expenses: {total_expense}")
	print("---------------")
	print(f"Net: {total_income-total_expense}")

def general_chart():
	incomes=[]
	expenses=[]
	with open("transactions.json","r",encoding="utf-8") as file:
		data=json.load(file)

		if not data:
			print("General chart can not be shown.")
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

def month_chart():
	expenses=[]
	labels=[]
	category_totals={}
	
	while True:
		try:
			month=input("Insert number of month: ")
			year=input("Insert a year: ")
			if year=="" or int(year)<0 or int(month)<1 or int(month)>12 or month=="":
				continue
			break
		except ValueError:
			print("Insert valid number of year or month.")

	if not month.startswith("0") and int(month)<10:
		month="0"+month

	with open("transactions.json","r",encoding="utf-8") as file:
		data=json.load(file)

		if not data:
			print("Month char can not be shown.")

		for t in data:
			if t["date"].startswith(f"{year}-{month}") and t["amount"]<0:
				if t["category"] in category_totals:
					category_totals[t["category"]]+=abs(t["amount"])
				else:
					category_totals[t["category"]]=abs(t["amount"])

	labels=list(category_totals.keys())
	y=list(category_totals.values())

	plt.pie(y,labels=labels,autopct="%1.1f%%")
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
		print("6. Generate month report")
		print("7. Draw the month chart with categories")
		print("8. Draw the chart")
		print("9. Exit")
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
			month_report()
		elif choice=="7":
			month_chart()
		elif choice=="8":
			general_chart()
		elif choice=="9":
			break
		else:
			print("Invalid option. Try again! \n")

if __name__ == "__main__":
    main()