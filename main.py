import json

categories = {
    '1': 'Food 🍕',
    '2': 'Drinks ☕',
    '3': 'Transportation 🚕',
    '4': 'Education 📚',
    '5': 'Entertainment 🎞️',
    '6': 'Bills 🛋️',
    '7': 'Health 🍎',
    '8': 'Other 📦',
}


def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)


def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def add_expense(expenses):
    item = input('Expense name: ')
    try:
        amount = float(input('Amount: '))
    except ValueError:
        print('Invalid amount!')
        return

    print('\nYour category: ')
    for key, value in categories.items():
        print(f'{key}. {value}')
    category_choice = input('Choose category')
    if category_choice not in categories:
        print('Invalid category!')
        return

    expense = {
        'name': item,
        'amount': amount,
        'category': categories[category_choice]
    }

    expenses.append(expense)
    save_expenses(expenses)
    print('\nExpense added successfully!')


def show_expenses(expenses):
    if not expenses:
        print('\nNo expenses yet!')
    else:
        print('\nYour expenses:')
        for expense in expenses:
            print(
                f"name: {expense['name']} - amount: ${expense['amount']} - category: {expense['category']}")


def total_expense(expenses):
    if not expenses:
        print('No expenses yet!')
    else:
        total = sum(expense['amount'] for expense in expenses)
        print(f'Total expense: ${total} 💵')


def delete_expense(expenses):
    if not expenses:
        print('No expenses!')
        return
    else:
        print('\nChoose expense to delete: ')
        for index, expense in enumerate(expenses, start=1):
            print(
                f"{index}. {expense['name']} - ${expense['amount']} - {expense['category']}")
        try:
            deleted_item = int(input('Choose expense to delete: '))
        except ValueError:
            print('Invalid number!')
            return
        if deleted_item < 1 or deleted_item > len(expenses):
            print('Expense not found!')
            return
        deleted = expenses.pop(deleted_item - 1)
        save_expenses(expenses)
        print('Your expenses now:')
        for expense in expenses:
            print(
                f"{expense['name']} - ${expense['amount']} - {expense['category']}")
        print(f"\n{deleted['name']} deleted successfully!")


expenses = load_expenses()

while True:
    print('\n==== Expense Tracker ====')
    print('1. Add Expense')
    print('2. Show Expense')
    print('3. Total Expense')
    print('4. Delete Expense')
    print('5. Exit')

    choice = input('Choose: ')

    if choice == '1':
        add_expense(expenses)

    elif choice == '2':
        show_expenses(expenses)

    elif choice == '3':
        total_expense(expenses)

    elif choice == '4':
        delete_expense(expenses)

    elif choice == '5':
        print('Bye')
        break
    else:
        print('Invalid choice, Try again.')
