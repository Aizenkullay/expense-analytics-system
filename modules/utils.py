import datetime

def line():
    print("=" * 69)

def get_standard_time():
    
    while True:
        date=input("Enter date as (DD-MM-YYYY or D-M-YY) : ")
        date_rep=date.replace("/","-")
        possible_formats=["%d-%m-%Y", "%d-%m-%y"]
        
        for date_foramts in possible_formats:
            try:
                prased_format=datetime.datetime.strptime(date_rep,date_foramts)
                standard_time=prased_format.strftime("%d-%m-%Y")
                return standard_time
            except ValueError:
                continue
        print("Invalid input or date does not exist. Please try again.")