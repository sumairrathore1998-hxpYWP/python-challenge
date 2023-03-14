import os
import csv

budget_data_csv = os.path.join("C:\\UofT-Bootcamp\\Starter_Code\\Instructions\\PyBank\\Resources\\budget_data")
file_to_output = "output.txt"

total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


with open('C:\\UofT-Bootcamp\\Starter_Code\\Instructions\\PyBank\\Resources\\budget_data.csv') as csvfile:  
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:

        total_months += 1

        total_revenue = total_revenue + int(row["Profit/Losses"])

        revenue_change = float(row["Profit/Losses"])- previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]
       

        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

with open(file_to_output, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------------\n")
    txt_file.write("Total Months: %d\n" % total_months)
    txt_file.write("Total Revenue: $%d\n" % total_revenue)
    txt_file.write("Average Revenue Change $%d\n" % revenue_average)
    txt_file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    txt_file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))