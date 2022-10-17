# a program that keeps stock of all inventory

# define the shoe class
class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # define method to retrieve cost
    def get_cost(self):
        return self.cost

    # define method to retrieve quantity
    def get_quantity(self):
        return self.quantity

    # method that represents the class as a string
    def __str__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    def __repr__(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


# create empty list
shoe_object_list = []


# define function to append into list
def read_shoes_data():
    # try catch for exception handling
    try:

        # open file to read from
        with open("inventory.txt", "r+") as file_open:
            data = file_open.readlines()

            # for loop looping over data to get indexes
            for lines in data[1:]:
                country, code, product, cost, quantity = lines.strip("\n").split(",")
                temp_shoe_obj = Shoes(country, code, product, cost, quantity)

                # append into list
                shoe_object_list.append(temp_shoe_obj)
    except FileNotFoundError:
        print("The file that you are trying to open does not exist")


# define function to capture and append shoes to list
def capture_shoes():
    # ask user for input
    country = input("Which country are the shoes from? ")
    code = input("What is the shoes' code? ")
    product = input("What is the product name? ")
    cost = int(input("How much do the shoes cost? "))
    quantity = int(input("How many pairs are left in stock? "))

    # append input into list
    temp_shoe_obj = Shoes(country, code, product, cost, quantity)
    shoe_object_list.append(temp_shoe_obj)


# define view all function
def view_all():
    # for loop looping over list
    for shoe in shoe_object_list:
        print(f"Shoe Country: {shoe.country}\n"
              f"Shoe Code: {shoe.code}\n"
              f"Shoe Product: {shoe.product}\n"
              f"Shoe Cost: {shoe.cost}\n"
              f"Shoe Quantity: {shoe.quantity}\n")


# define restock function
def re_stock():
    # initialise lowest quantity and shoe position
    lowest_quant = int(shoe_object_list[0].quantity)
    shoe_position = 0

    # for loop looping over the list
    for count, shoe in enumerate(shoe_object_list):

        # conditional body to check for lowest quality
        if lowest_quant > int(shoe.quantity):
            lowest_quant = int(shoe.quantity)
            shoe_position = count
    print(shoe_object_list[shoe_position])

    # ask user for input
    quant_update = input("Would you like to update the quantity? type y for yes or n for no. ")

    # conditional body to update quantity or not
    if quant_update == 'y':
        quant_update2 = int(input("Enter the new amount of stock: "))
        shoe_object_list[shoe_position].quantity = quant_update2
        print(shoe_object_list[shoe_position])

    # use try catch for error handling
    try:

        # open file to write into
        with open("inventory.txt", "w+") as file_writer:
            file_writer.write(f"Country,Code,Product,Cost,Quantity\n")

            # for loop to update quantity in file
            for lines in shoe_object_list:
                file_writer.write(f"{lines.country},{lines.code},{lines.product},{lines.cost},{lines.quantity}\n")
    except FileNotFoundError:
        print("The file that you are trying to open does not exist")

    else:
        pass


# define shoe search function where users searches by code
def search_shoe():
    shoe_position = 0
    code_search = input("Enter the code of the shoe you're looking for (case sensitive): ")
    for count, shoe in enumerate(shoe_object_list):
        shoe_position = count
        if shoe.code == code_search:
            print(f"Here is the information for the shoes you are looking for:\n"
                  f"{shoe_object_list[shoe_position]}")
            break


# define a function to determine the value per item
def value_per_item():
    for shoe in shoe_object_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"Shoe Value: R{value}")


# define a function to determine highest quantity
def highest_qty():
    highest_quant = int(shoe_object_list[0].quantity)
    shoe_position = 0

    for count, shoe in enumerate(shoe_object_list):
        if highest_quant < int(shoe.quantity):
            highest_quant = int(shoe.quantity)
            shoe_position = count
    print(f"{shoe_object_list[shoe_position]} is on sale grab it quick!")


# create the menu items
while True:
    menu = input('''Select one of the following Options below:
        rsd - Read shoe data
        cs -  Capture shoes
        va - View all 
        rs - Restock
        ss - Search shoe
        vpi - Value per item
        hq - Highest quantity
        e - Exit
        : ''').lower()

    if menu == 'rsd':
        read_shoes_data()

    elif menu == 'cs':
        capture_shoes()

    elif menu == 'va':
        view_all()

    elif menu == 'rs':
        re_stock()

    elif menu == 'ss':
        search_shoe()

    elif menu == 'vpi':
        value_per_item()

    elif menu == 'hq':
        highest_qty()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
