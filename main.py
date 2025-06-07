from functions import add_expenses, expenses_delete, show_today_expenses

def main():
    
    print("""
        **********************************************
        *       💰   HARAJATLAR MENYUSI   💰         *
        **********************************************
        *                                            *
        *    1.➕  Harajat qo'shish                  *
        *    2.❌  Harajatni o'chirish               *
        *    3.📅  Bugungi harajatlarni ko'rish      *
        *    4.🚪  Chiqish                           *
        *                                            *
        **********************************************
        """)
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_expenses()
    elif choice == "2":
        expenses_delete()
    elif choice == "3":
        show_today_expenses()
    elif choice == "4":
        print("Good bye :)")
        return 
    else:
        print("Invalid choice")
    return main()


if __name__ == "__main__":
    main()