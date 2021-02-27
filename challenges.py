#callenge 1
#ask for the users first name and display output message Hello first name
first_name = input("enter your first_name: ")
print("Hello" "" + "" +  first_name)


#challenge 2
#ask users first name & then ask for their surname & display output message
#Hello [firstname][surname]
FirstName = input("enter firstName:")
surname = input("enter surname:")
print("Hello" + "" +   FirstName  + surname)


#challenge 3
#code that will display the joke "what do you call a bear with no teeth?" and on the next line display answer
#"A gummy bear!" Try to create it using only one line of code
print("what do you call a bear with no teeth? \n A gummy bear!")


#challenge 4
#ask the user to enter two numbers .Add them together and displsy the answer as The total is[answer]
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
answer = num1 + num2
print("The total is",  answer)


#challenge 5
#ask the user to enter three numbers, add the first two together and then multiply the total by the third.
#display the answer as The answer is [answer]
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))
sum = num1+num2
print(sum)
answer = num3*sum
print("The answer is",answer)


#challenge 6
#ask how many slices of pizza you started with & ask how many slices they have eaten.
#Work out how many slices they have left with and display the answer in a user friendly format.
a = int(input("enter slices of pizza you started with: "))
b = int(input("enter slices of pizza you have eaten: "))
slices_left = a-b
print(f" The slices you left with are {slices_left}")


#challenge 7
#ask the user their name & age add1 to their age & display the output[name]
#next birthday will be [new age]
Name = input("enter  your name: ")
Age = int(input("enter your age: "))
new_age = Age +1
print(Name)
print("next birthday will be",new_age)


#challenge 8
#ask the total price of the bill, then ask how many diners there are.Divide the total bill by the number of diners
# and show how much each person must pay.
Bill_price = float(input("enter total price per bill: "))
NumberDiners = int(input("enter number of diners: "))
AmountPerPerson = Bill_price/NumberDiners
print("each person must pay", AmountPerPerson)

#challenge 9
#1kg has 2204 pounds ,ask the user to enter a weight in kilograms and convert it to pounds.
weight = int(input("enter your weight in kg: "))
weight_pounds = weight*2204
print("weight in pounds is", weight_pounds)

#challenge 10
#ask for number of days and then will show how many hours ,minutes & seconds are in that number of days.
days = int(input("enter number of days: "))
hours = (days*24)
minutes = (hours*60)
seconds = (minutes*60)
print(f"The {days} the days you entered has {hours}hours, {minutes} minutes & {seconds} seconds .")
