import pandas as pd


def analyse_sales():
    print("\nRETRIEVE CLIENTS SALES INFORMATION\n")
    name = input("What is the name of the client ? ")
    data_clients = pd.read_excel("clients_sales.xlsx", sheet_name = "clients")                   # Read the excel file
    client_number = data_clients[data_clients['name'] == name]['client number']                  # Match the client name with the client number   
    if not client_number.empty:                                                                  # If the client number is found
        client_number = client_number.iloc[0]                                                    # Get the client number               
    else:
        print("\nClient not found\n")
        analyse_sales()
        return

    data_sales = pd.read_excel("clients_sales.xlsx", sheet_name = "sales")
    sales = data_sales[data_sales['Client number'] == client_number]['Client number'].count()   # Count the number times the client number appears in the sales sheet

    mean = data_sales[data_sales['Client number'] == client_number]['Sales'].mean()             # Calculate the mean of the sales

    max_spent = data_sales[data_sales['Client number'] == client_number]['Sales'].max()         # Calculate the maximum of the sales

    sum = data_sales[data_sales['Client number'] == client_number]['Sales'].sum()               # Calculate the sum of the sales

    print("The client has bought ", sales," products.")
    print("Here is the mean of its sales : ", round(mean, 2))
    print("Here is the maximum spend for a sale : ", round(max_spent, 2))
    print("Here is the sum of all the sales : ", round(sum, 2))

    while True:                                                                                 # While loop to keep the question open
        choice = input("\nWould you like to continue ? (y or n)")                               # Ask if the user wants to continue (only accept y or n)   
        if choice == "y":
            analyse_sales()
        elif choice == "n":
            show_excel()
        else:
            print("Invalid option\n")

def excel_sales():
    data = pd.read_excel("clients_sales.xlsx", sheet_name = "sales")        # Read the sales sheet from the excel file
    print(data)                                                             # Print the sales sheet                               

def excel_clients():
    data = pd.read_excel("clients_sales.xlsx", sheet_name = "clients")      # Read the clients sheet from the excel file
    print(data)                                                             # Print the clients sheet

def show_excel():                                                           # Function to show the excel file
    while True:                                                             # While loop to keep the submenu open                          
        print("\nEXCEL CLIENTS AND SALES INFORMATION\n")
        print("1) Show clients")
        print("2) Show sales")
        print("3) Analyse clients sales")
        print("4) Go back\n")
        choice = input("Choose an option between 1 and 4: ")

        if choice == "1":
            excel_clients()
        elif choice == "2":
            excel_sales()
        elif choice == "3":
            analyse_sales()
        elif choice == "4":
            main()
        else:
            print("Invalid option\n")

def show_clients():                                             # Function to display the clients in a txt file
    with open("clients.txt", "r") as file:
        print(file.read())
    main()

def create_client():                                            # Function to create a new client
    class Client:
        def __init__(self, name, birth, city, email):           # Constructor
            self.name = name
            self.birth = birth
            self.city = city
            self.email = email

        def check_if_first(self):                               # Function to check if the file is empty
            with open("clients.txt", "r") as file:
                if file.read(1):
                    return False
                else:
                    return True
    
        def show_client(self):                                  # Function to show the client information
            print("\nClient name : {}".format(self.name))
            print("Client date_birth : {}".format(self.birth))
            print("Client city_birth : {}".format(self.city))
            print("Client email : {}\n".format(self.email))

        def save_client(self):                                  # Function to save the client information in a txt file
            with open("clients.txt", "a") as file:
                if self.check_if_first():
                    file.write("CLIENT INFORMATION\n")
                    file.write(f"{self.name},{self.birth},{self.city},{self.email}\n")
                else:
                    file.write(f"\n{self.name},{self.birth},{self.city},{self.email}\n")

    print("\nCLIENT CREATION\n")
    name = input("What is the name of the client? ")
    birth = input("What is the date of birth of the client? ")
    city = input("What is the city of birth of the client? ")
    email = input("What is the email of the client? ")
    client = Client(name, birth, city, email)                   # Instance of the class Client
    client.show_client()                                        # Method to show the client information
    client.save_client()                                        # Method to save the client information in a txt file   
    print("The client has been created and saved.\n")
    main()


def main():
    menu = 1
    while menu:                                                 # While loop to keep the menu open
        print("-------------------------------------------")
        print("Welcome to the client and sales analysis\n")
        print("1) Create a new client")
        print("2) Show all the clients in Txt file")
        print("3) Show Excel file clients and sales")
        print("4) Quit")
        choice = input("Choose an option between 1 and 4: ")
        print("-------------------------------------------")

        if choice == "1":                                       # If the user chooses 1, the function create_client() is called
            create_client()
        elif choice == "2":
            show_clients()                                      # If the user chooses 2, the function show_clients() is called
        elif choice == "3":
            show_excel()                                        # If the user chooses 3, the function show_excel() is called
        elif choice == "4":                                     # If the user chooses 4, the loop is broken      
            menu = 0
        else:
            print("Invalid option\n")

if __name__ == "__main__":                                      # If the program is called directly, the function main() is called
    main()