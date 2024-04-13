import csv

def get_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    return name, age, email

def save_to_csv(data):
    with open('user_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Data saved successfully!")

def main():
    print("Welcome to the user data program!")
    while True:
        choice = input("Do you want to enter user data? (yes/no): ")
        if choice.lower() == 'yes':
            user_data = get_user_data()
            save_to_csv(user_data)
        elif choice.lower() == 'no':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()


    