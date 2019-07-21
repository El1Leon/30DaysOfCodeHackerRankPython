print("How much does the meal cost?")
meal_cost = float(input().strip())
print("How much percentage do you want to tip?")
tip_percent = int(input().strip())/100
print(str(tip_percent)+"%")
print("The tax is going to be")
tax_percent = int(input().strip())/100
print(str(tax_percent)+"%")

tip = meal_cost * tip_percent
tax = meal_cost * tax_percent
total = meal_cost + tip + tax

print("The total meal cost is $" + str(round(total)) + ".")

#The string passed to strip is treated as a 
# bunch of characters, not a string. 
#Thus, strip('Axyx') means 
# "strip occurrences of A, x, or y 
# from either end of the string".
