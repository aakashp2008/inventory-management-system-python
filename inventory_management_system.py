import os

FILE_NAME = "inventory.txt"


def add_product():
    product_id = input("Enter Product ID: ")

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == product_id:
                    print("\nProduct ID already exists!")
                    return

    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price: "))

    with open(FILE_NAME, "a") as file:
        file.write(f"{product_id},{product_name},{category},{quantity},{price}\n")

    print("\nProduct Added Successfully!")


def view_products():
    if not os.path.exists(FILE_NAME):
        print("\nNo product records found!")
        return

    print("\n================================================================================")
    print(f"{'ID':<10}{'Product Name':<25}{'Category':<20}{'Qty':<10}{'Price'}")
    print("================================================================================")

    with open(FILE_NAME, "r") as file:
        for line in file:
            product_id, name, category, quantity, price = line.strip().split(",")

            print(f"{product_id:<10}{name:<25}{category:<20}{quantity:<10}{price}")


def search_product():
    if not os.path.exists(FILE_NAME):
        print("\nNo product records found!")
        return

    product_id = input("\nEnter Product ID to Search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == product_id:
                print("\nProduct Found")
                print("--------------------------------")
                print("Product ID   :", data[0])
                print("Product Name :", data[1])
                print("Category     :", data[2])
                print("Quantity     :", data[3])
                print("Price        :", data[4])
                found = True
                break

    if not found:
        print("\nProduct Not Found!")


def update_product():
    if not os.path.exists(FILE_NAME):
        print("\nNo product records found!")
        return

    product_id = input("\nEnter Product ID to Update: ")
    updated = False
    records = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == product_id:
                print("\nEnter New Product Details")

                product_name = input("Product Name: ")
                category = input("Category: ")
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))

                records.append(
                    f"{product_id},{product_name},{category},{quantity},{price}\n"
                )

                updated = True
            else:
                records.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if updated:
        print("\nProduct Updated Successfully!")
    else:
        print("\nProduct Not Found!")


def delete_product():
    if not os.path.exists(FILE_NAME):
        print("\nNo product records found!")
        return

    product_id = input("\nEnter Product ID to Delete: ")
    deleted = False
    records = []

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == product_id:
                deleted = True
            else:
                records.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(records)

    if deleted:
        print("\nProduct Deleted Successfully!")
    else:
        print("\nProduct Not Found!")


def menu():
    while True:
        print("\n====================================================")
        print("           INVENTORY MANAGEMENT SYSTEM")
        print("====================================================")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        print("----------------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            print("\nThank you for using Inventory Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    menu()
