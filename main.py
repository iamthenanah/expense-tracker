import json
from datetime import datetime

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
    with open('expenses.json', 'w', encoding='utf-8') as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)


def load_expenses():
    try:
        with open('expenses.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def format_datetime(datetime_string):
    if datetime_string == 'Unknown':
        return 'Unknown'
    date = datetime.fromisoformat(datetime_string)
    return date.strftime('%d %B %Y - %H:%M')


def add_expense(expenses):
    item = input('Expense name: ')
    if not item.strip():
        print('Expense name cannot be empty!')
        return
    try:
        amount = float(input('Amount: '))
        if amount <= 0:
            print('Amount must be greater than zero!')
            return
    except ValueError:
        print('Invalid amount!')
        return

    print('\nYour category: ')
    for key, value in categories.items():
        print(f'{key}. {value}')
    category_choice = input('Choose category: ')
    if category_choice not in categories:
        print('Invalid category!')
        return

    current_time = datetime.now()

    expense = {
        'name': item,
        'amount': amount,
        'category': categories[category_choice],
        'datetime': current_time.isoformat()
        # 'datetime': current_time.strftime('%Y-%m-%d %H:%M')
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
                f"name: {expense['name']} - amount: ${expense['amount']:.2f} - category: {expense['category']} - time:{format_datetime(expense['datetime'])} ")


def total_expense(expenses):
    if not expenses:
        print('No expenses yet!')
    else:
        total = sum(expense['amount'] for expense in expenses)

        print(f'Total expense: ${total:.2f} 💵')


def delete_expense(expenses):
    if not expenses:
        print('No expenses!')
        return

    print('\nChoose expense to delete: ')
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']} - ${expense['amount']:.2f} - {expense['category']}")
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
            f"{expense['name']} - ${expense['amount']:.2f} - {expense['category']}")
    print(f"\n{deleted['name']} deleted successfully!")


def search_expense(expenses):
    if not expenses:
        print('No expenses yet!')
        return

    keyword = input('Search expense name: ').lower()

    found = False

    for expense in expenses:
        if keyword in expense['name'].lower():
            print(
                f"{expense['name']} - ${expense['amount']:.2f} - {expense['category']} - {format_datetime(expense['datetime'])}")
            found = True
    if not found:
        print('No matching expense found!')


expenses = load_expenses()
updated = False

for expense in expenses:
    if 'datetime' not in expense:
        expense['datetime'] = 'Unknown'
        updated = True
if updated:
    save_expenses(expenses)


while True:
    print('\n==== Expense Tracker ====')
    print('1. Add Expense')
    print('2. Show Expense')
    print('3. Total Expense')
    print('4. Delete Expense')
    print('5. Search Expense')
    print('6. Exit')

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
        search_expense(expenses)

    elif choice == '6':
        print('Bye')
        break
    else:
        print('Invalid choice, Try again.')
