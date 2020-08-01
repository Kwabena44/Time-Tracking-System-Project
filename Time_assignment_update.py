from datetime import datetime, date
while True:
    try:
        x = input("Please enter start date and time, use the format DD/MM/YY HH:MM:")
        start_date = datetime.strptime(x,"%d/%m/%y %H:%M") 
        break
    except ValueError as e:
        print('Please use the format DD/MM/YY HH:MM:')
print(start_date)


while True:
    try:
        x = input("Please enter end date and time, use the format DD/MM/YY HH:MM:")
        end_date = datetime.strptime(x,"%d/%m/%y %H:%M") 
        break
    except ValueError as e:
        print('Please use the format DD/MM/YY HH:MM:')
print(end_date)


