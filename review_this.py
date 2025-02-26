import os
import sqlite3
import requests

def process_user_data():
    unused_variable = "This is unused"
    print("This might trigger no-console warning")
    
    some_undefined_variable = "This will cause an error"
    user_input = input("Enter something: ")

    # Security issue: SQL injection vulnerability
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")
    
    # Syntax error: missing parentheses
    if x == 5:
        pass

    # Dangerous usage of eval
    eval("os.system('rm -rf /')")

    # Insecure HTTP request (no SSL/TLS)
    response = requests.get("http://example.com/api/data")
    
    # Security issue: storing sensitive data in plain text
    password = "supersecretpassword"
    api_key = "sk_live_abcdef123456"
    
    # Insecure file operation
    with open("config.txt", "w") as f:
        f.write(f"API Key: {api_key}")
    
    # Missing exception handling
    result = 10 / 0
    
    # Insecure redirect with user input
    redirect_url = f"http://example.com?redirect={user_input}"
    
    # Undefined function or object
    db.query(req.body.userInput)

    # Return message with sensitive info
    return f"Data processed: {password}"

