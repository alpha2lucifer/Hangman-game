from datetime import datetime
import play
import csv
def register_user():
    Data = []
    code = input("\nEnter player code :")
    name = input("Enter your name :")
    played_at = str(datetime.now())
    Data.append([code, name, played_at])
        
    with open("registered_user.csv","a",newline="") as f :
        w = csv.writer(f,delimiter=',')
        w.writerows(Data)

