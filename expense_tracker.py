import os

FILENAME = "expenses.txt"

def load_data():
    transactions = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for line in file:
                date, desc, amount = line.strip().split("|")
                transactions.append({
                    "date": date,
                    "desc": desc,
                    "amount": float(amount)
                })
    return transactions

def save_data(transactions):
    with open(FILENAME, "w") as file:
        for t in transactions:
            file.write(f"{t['date']}|{t['desc']}|{t['amount']}\n")

def add_transaction(transactions):
    date = input("Enter date (YYYY-MM-DD): ")
    desc = input("Enter description: ")
    while True:
        try:
            amount = float(input("Enter amount (positive for income, negative for expense): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    transactions.append({"date": date, "desc": desc, "amount": amount})
    print("Transaction added!")

def show_transactions(transactions):
    if not transactions:
        print("No transactions to show.")
        return
    print("\nDate       | Description             | Amount")
    print("----------------------------------------------")
    for t in transactions:
        print(f"{t['date']:10} | {t['desc'][:20]:20} | {t['amount']:8.2f}")
    print("----------------------------------------------")

def show_balance(transactions):
    balance = sum(t["amount"] for t in transactions)
    print(f"\nYour total balance is: {balance:.2f}")

def main():
    transactions = load_data()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Show balance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(transactions)
            save_data(transactions)
        elif choice == "2":
            show_transactions(transactions)
        elif choice == "3":
            show_balance(transactions)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
