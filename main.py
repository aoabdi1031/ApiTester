import yaml
import sys
import requests

from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter

# Function to handle manual test requests
def make_requests(data):

    print("\n")

    for i, test_case in enumerate(data['tests'], start=0):
        header = test_case['headers']
        param = test_case['params']
        method = test_case['method'].upper()

        if method == 'GET':
            response = requests.get(test_case['endpoint'], headers=header, params=param)
        elif method == 'POST':
            response = requests.post(test_case['endpoint'], headers=header, json=param)
        elif method == 'PUT':
            response = requests.put(test_case['endpoint'], headers=header, json=param)
        elif method == 'DELETE':
            response = requests.delete(test_case['endpoint'], headers=header, params=param)

        if response.status_code == test_case['expected']['status_code']:
            print(f"Test {i + 1} Passed")
        else:
            print(f"Test {i + 1} Failed")
            print(f"Expected: {test_case['expected']['status_code']}")
            print(f"Received: {response.status_code}")
            print(f"Response: {response.text}")

# Function to read YAML file
def readfile(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Manual Testing

def manual_testing():
    completer = PathCompleter()  # Completer for file paths
    yaml_file_path = prompt("Please provide the YAML file path: ", completer=completer)
    data = readfile(yaml_file_path)
    make_requests(data)


# Automatic Testing 
def automatic_testing():
    print("Automatic testing selected. This feature is under construction.")




# Command-line menu
def main_menu():
    while True:
        print("\n--- API Testing Program ---")
        print("1. Manual Testing")
        print("2. Automatic Testing")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            manual_testing()
        elif choice == '2':
            automatic_testing()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_menu()
