#input phase (before loop)
response = input("Do you want to enter student data? (Yes/No):")

#process phase 
count = 0

while response == "Yes":
    #input inside loop
    last_name = input("Enter last name:")
    score1 = float(input("Enter exam score 1:"))
    score2 = float(input("Enter exam score 2:"))

#calculate average 
    average = (score1 + score2) / 2

#output inside loop 
print("Last Name:", last_name)
print("Average Score:", average)

#count students 
count = count + 1 

# ask again
response = input("Do you want to enter another student? (Yes/No):")

#final output after loop
print("Total number of students entered:", count)

