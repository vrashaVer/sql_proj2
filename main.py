import sqlite3
from action_over_db import add_products,add_custumers,add_orders,open_connection,close_connection,get_total_sales, get_count_of_orders,get_average_order_value,get_the_most_popular_category,get_product_count_per_category,update_smartphone_prices
from tabulate import tabulate

if __name__ == "__main__":
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    with open('create_db.sql', encoding='utf-8') as file:
        cursor.executescript(file.read())
        connection.commit()

    cursor.close()
    connection.close
    menu_list_action = {
        1:'Add products',
        2:'Add customers',
        3:'Add orders',
        4:'Get total sales',
        5:'Get order count per customer',
        6:'Get average order value',
        7:'Get most popular category',
        8:'Get product count per category',
        9:'Update smartphone prices',
        0:'Exit',
    }

    save = True
 
    while True:

        print('\n                      MENU:\n')
        for action in menu_list_action:
            print(f'{action}. {menu_list_action.get(action)}')
        print('\n')
        try:
            choice = int(input("Enter choice: "))

            if choice not in menu_list_action:
                print("Invalid choice, please enter a number from the menu.")
                continue

            if choice == 1 :
                if choice in menu_list_action:
                    connection, cursor = open_connection()
                    results = add_products(cursor)
                    headers = ["Product ID", "Name", "Category", "Price"]
                    table = [list(row) for row in results]
                    print("Added products:")
                    print(tabulate(table, headers=headers, tablefmt="grid"))
                else: 
                    print('This function cannot be performed more than 1 time')
                    save = False

            elif choice == 2:
                if choice in menu_list_action:
                    connection, cursor = open_connection()
                    results = add_custumers(cursor)
                    headers = ["Customer ID", "First Name", "Last Name", "Email"]
                    table = [list(row) for row in results]
                    print("Added customers:")
                    print(tabulate(table, headers=headers, tablefmt="grid"))
                else:
                    print('This function cannot be performed more than 1 time')
                    save = False

            elif choice == 3:
                if choice in menu_list_action:
                    connection, cursor = open_connection()
                    results = add_orders(cursor)
                    headers = ["Order ID", "Customer ID", "Product ID", "Quantity", "Order Date"]
                    table = [list(row) for row in results]
                    print("Added orders:")
                    print(tabulate(table, headers=headers, tablefmt="grid"))
                else:
                    print('This function cannot be performed more than 1 time')
                    save = False

            elif choice == 4:
                connection, cursor = open_connection()
                result = get_total_sales(cursor)
                headers = ["Total Sales"]
                table = [result] if result else [["No data"]]
                print(tabulate(table, headers=headers, tablefmt="grid"))
                save = False
            
            elif choice == 5:
                connection, cursor = open_connection()
                results = get_count_of_orders(cursor)

                headers = ["First Name", "Last Name", "Order Count"]
                table = [list(row) for row in results]
                print(tabulate(table, headers=headers, tablefmt="grid"))
                save = False
            
            elif choice == 6:
                connection, cursor = open_connection()
                result = get_average_order_value(cursor)
                headers = ["Average order check"]
                table = [result]
                print(tabulate([table], headers=headers, tablefmt="grid"))
                save = False

            elif choice == 7:
                connection, cursor = open_connection()
                result = get_the_most_popular_category(cursor)
                headers = ["The most popular category"]
                table = [result] if result else [["No data"]]
                print(tabulate(table, headers=headers, tablefmt="grid"))
                save = False
            
            elif choice == 8:
                connection, cursor = open_connection()
                results = get_product_count_per_category(cursor)
                headers = ["Category", "Quantity of products"]
                table = [list(row) for row in results]
                print(tabulate(table, headers=headers, tablefmt="grid"))
                save = False

            elif choice == 9:
                connection, cursor = open_connection()
                results = update_smartphone_prices(cursor)
                headers = ["ID product", "Name", "New Price"]
                table = [list(row) for row in results]
                print("Updated prices of goods in the category 'smartphones':")
                print(tabulate(table, headers=headers, tablefmt="grid"))

            elif choice == 0:
                break

            if save == True:
                save_changes = input("Do you want to save changes? (y/n): ")
                if save_changes.lower() == 'y':
                    connection.commit()
                    close_connection(connection,cursor)
                    if choice == 1 or choice == 2 or choice == 3:
                        del menu_list_action[choice]
                    print("Changes were successfully saved")
                else:
                    connection.rollback()
                    close_connection(connection,cursor)
                    print('Changes were not saved')
            else:
                close_connection(connection,cursor)
            save = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")
       

