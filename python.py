import requests
import sqlite3
import random

# Create a database connection and a table for storing user responses
conn = sqlite3.connect('user_responses.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS responses
             (question TEXT, response TEXT)''')

# Define a function to get a random question from LeetCode's API
def get_random_question():
    response = requests.get('https://leetcode.com/api/problems/all/')
    questions = response.json()['stat_status_pairs']
    random_question = random.choice(questions)
    return random_question['stat']['question__title']

# Define a function to take user input and store it in the database
def store_user_input(question):
    response = input('Your answer: ')
    c.execute("INSERT INTO responses VALUES (?,?)", (question, response))
    conn.commit()

# In the main function, call the function to get a random question, display it to the user, take user input and store it in the database
def main():
    question = get_random_question()
    print('Question: ', question)
    store_user_input(question)

main()