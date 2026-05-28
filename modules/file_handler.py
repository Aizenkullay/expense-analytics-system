import json

def load_data():

    try:
        with open('data/expenses.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:

        print("File not found")

        return []
    
    except json.JSONDecodeError:

        print("An exceptional error occured")

        return []
    
    
def save_data(expenses):

    with open('data/expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
        print("Data saved successfully !")