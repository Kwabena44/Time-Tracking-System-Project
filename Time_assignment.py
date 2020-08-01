 
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

