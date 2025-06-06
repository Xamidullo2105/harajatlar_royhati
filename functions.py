from datetime import datetime
from file_manager import read, append, writerows

def add_expenses():
    amount = float(input("Summa (so'm): "))
    description = input("Nima uchun: ")
    date = input("Sana (06.06.2025): ")
    append("expenses", [amount, description, date])
    print("Harajat qo'shildi ✅")


def expenses_delete():
    expenses = read("expenses")
    if not expenses:
        print("Harajat yo'q")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e[2]} - {e[1]}: {e[0]} so'm")
    try:
        index = int(input("O'chirish uchun raqam: ")) - 1
        if 0 <= index < len(expenses):
            expenses.pop(index)
            writerows("expenses", expenses)
            print("Harajat o'chirildi ✅")
        else:
            print("Bunday raqam yo'q ❌")
    except:
        print("Faqat raqam kiriting!")

def show_today_expenses():
    expenses = read("expenses")
    today = datetime.now().strftime('%Y-%m-%d')
    today_expenses = []
    for e in expenses:
        if e[2] == today:
            today_expenses.append(e)
    if not today_expenses:
        print("Bugun harajat yo'q 😃")
        return
    for i, e in enumerate(today_expenses, 1):
        print(f"{i}. {e[2]} - {e[1]}: {e[0]} so'm")