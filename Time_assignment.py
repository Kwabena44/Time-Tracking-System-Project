    
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 14:21:37 2020


@author: Timothy
"""
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



work_time = end_date - start_date
print(f"your total work time is {work_time}")
print ("Stop time: ", end_date)
currency = "$"


total_seconds=work_time.seconds
    #print('tot sec: ', total_seconds)
hours = total_seconds/3600
    #print('tot hours: ', hours)
hours_days = work_time.days
    #print('tot hoursdays: ', hours_days)
total_hours = hours + (hours_days * 24)
    #print('tot_hours: ', total_hours)
rate_of_pay = 5
total_pay = round(total_hours * rate_of_pay, 2)
print(f'Your total pay is {currency}', total_pay)
today = date.today()



import csv
with open('total_pay.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Start Date and Time", "End Date and Time", "Hours Worked", "Rate per hour", "Total Pay $"])


from csv import writer


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


list_of_elements = [today, start_date, end_date, work_time, rate_of_pay, total_pay]
append_list_as_row('total_pay.csv', list_of_elements)



import pandas as pd


read_file = pd.read_csv('total_pay.csv') 
read_file

