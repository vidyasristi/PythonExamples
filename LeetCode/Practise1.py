name = input("enter name: ")
age = int(input("enter age: "))
# print("Your name is " + name)
# print("Your name is " + age)

from datetime import date

year_ = date.today().year
year_100 = str((year_ - age) + 100)

print(name + " will be 100 years old in the year " + year_100)

