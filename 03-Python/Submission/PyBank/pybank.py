import csv

csvpath = "Resources/budget_data.csv"

#Create the lists to store data. 
profits = []
monthly_changes = []

#Initialize Variables
total_months = 0
total_profit = 0
initial_profit = 0


with open(csvpath, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
            #Count the number of rows in the csv as months
            total_months += 1

            #calculate the total profit
            total_profit += int(row[1])

            
            #if not first row get the calculate the change
            if total_months > 1:
                
                profit = int(row[1]) - initial_profit
                #Store these profit changes in a list
                profits.append(profit)
                # Store the months and year coulumn to a list
                monthly_changes.append(row[0])

            
            #Reset our Variable
            initial_profit = int(row[1])

            #Print CSV data
            print(row)

# Print or write our Variable resutls
#Total Months
print(total_months)

#Total Profits
print(total_profit)

#Average of the profits
avg_profit = sum(profits) / len(profits)
print(sum(profits)/ len(profits))

# Greatest profit increase
greatest_increase_profits = max(profits)
increase_date = profits.index(greatest_increase_profits)
max_month = monthly_changes[increase_date]
print(max(profits))

# Greatest profit Decrease
greatest_decrease_profits = min(profits)
decrease_date = profits.index(greatest_decrease_profits)
min_month = monthly_changes[decrease_date]


# create summary table
profit_summ = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit}
Average  Change: ${avg_profit}
Greatest Increase in Profits: {max_month} (${greatest_increase_profits})
Greatest Decrease in Profits: {min_month} (${greatest_decrease_profits})
        """
print(profit_summ)

#write summary to text
# writes to file
with open("budget_analysis.txt", "w") as file:
    file.write(profit_summ)


