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
    item = input('Expense name: ').strip()
    if not item:
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
        for index, expense in enumerate(expenses, start=1):
            print(
                f"{index}. name: {expense['name']} - amount: ${expense['amount']:.2f} - category: {expense['category']} - time:{format_datetime(expense['datetime'])} ")


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

    show_expenses(expenses)

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


def edit_expense(expenses):
    show_expenses(expenses)

    try:
        edited_expense = int(input('Choose your expense to edit: '))
    except ValueError:
        print('Invalid number!')
        return

    if edited_expense < 1 or edited_expense > len(expenses):
        print('Invalid number!')
        return

    new_item = input('New item: ').strip()
    if not new_item:
        print('Expense name cannot be empty!')
        return

    try:
        new_amount = float(input('New amount: '))
    except ValueError:
        print('Invalid amount!')
        return
    if new_amount <= 0:
        print('Amount must be greater than zero!')
        return

    print('\nChoose the new category: ')
    for key, value in categories.items():
        print(f'{key}. {value}')
    new_category = input('Choose category: ')
    if new_category not in categories:
        print('Invalid category!')
        return

    new_datetime = datetime.now().isoformat()
    selected_expense = expenses[edited_expense - 1]

    selected_expense['name'] = new_item
    selected_expense['amount'] = new_amount
    selected_expense['category'] = categories[new_category]
    selected_expense['datetime'] = new_datetime

    save_expenses(expenses)
    print('Expense updated successfully!')


def filter_by_category(expenses):
    if not expenses:
        print('No expenses yet!')
        return

    print('\nYour categories: ')
    for key, value in categories.items():
        print(f'{key}. {value}')

    selected_category = input('\nSelect your category: ')

    if selected_category not in categories:
        print('Invalid category!')
        return

    found = False
    total = 0

    print(f"Expense in {categories[selected_category]}:")

    for expense in expenses:
        if expense['category'] == categories[selected_category]:
            print(f"{expense['name']} - ${expense['amount']:.2f}")

            total += expense['amount']
            found = True

    if not found:
        print('No expenses in this category!')
    else:
        print(
            f"\nTotal {categories[selected_category]} expenses: ${total:.2f}")


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
    print('6. Edit Expense')
    print('7. Filter Your Categories')
    print('8. Exit')

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
        edit_expense(expenses)

    elif choice == '7':
        filter_by_category(expenses)

    elif choice == '8':
        print('Bye')
        break
    else:
        print('Invalid choice, Try again.')
