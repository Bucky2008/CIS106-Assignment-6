# Input phase (before loop)
response = input("Do you want to enter employee data? (Yes/No): ")

# Process
total_pay = 0
count = 0

while response == "Yes":
    # Input inside loop
    last_name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter rate of pay: "))

    # Calculate gross pay
    if hours > 40:
        gross = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        gross = hours * rate

    # Output per employee
    print("Last Name:", last_name)
    print("Gross Pay:", gross)

    # Update totals
    total_pay = total_pay + gross
    count = count + 1

    # Ask again (loop control)
    response = input("Do you want to enter another employee? (Yes/No): ")

# Final output after loop
if count > 0:
    average = total_pay / count
else:
    average = 0

print("Total Gross Pay:", total_pay)
print("Number of Employees:", count)
print("Average Pay:", average)