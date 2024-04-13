import requests
from bs4 import BeautifulSoup
import csv

def fetch_user_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    user_data = []

    # Example: Extracting data from input fields with name attributes
    name = soup.find('input', {'name': 'name'}).get('value', '')
    age = soup.find('input', {'name': 'age'}).get('value', '')
    email = soup.find('input', {'name': 'email'}).get('value', '')

    user_data.append(name)
    user_data.append(age)
    user_data.append(email)

    return user_data

def save_to_csv(data):
    with open('user_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Data saved successfully!")

def main():
    url = 'https://example.com'  # Replace with the URL of your website
    user_data = fetch_user_data(url)
    save_to_csv(user_data)

if __name__ == "__main__":
    main()
