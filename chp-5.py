#Control Flow in Python
#Control flow refers to the way a program decides which code to execute and in what order. In Python, this is done using if, elif, else statements and loops like for and while.

# --------------------If-Else & Elif Example------------------------

# User se ek number lega
num = int(input("Enter Any Number:"))

if num % 2 ==0 :
    print("This number is Even")

elif num % 2 != 0 :
    print("This number is Odd")

else:
    print("This number is Composite")

    # --------------------Nested If Example------------------------

menu = input("This is a Menu List! (Breakfast, Lunch, Dinner): ")

if menu == 'Breakfast':
    print("You chose Breakfast")
    
    dish = input("Choose any breakfast? (Omelette, Pancakes): ")
    
    if dish == "Omelette":
        print("Omelette is for 10$")
    elif dish == "Pancakes":
        print("Pancakes is for 15$")
    else:  
        print("No dish available!")

elif menu == 'Lunch':
    print("You chose Lunch")

    lunch = input("Choose any Lunch? (Dal-Makhni, Dal-Chawal): ")
    
    if lunch == "Dal-Makhni":
        print("Dal-Makhni is for 25$")
    elif lunch == "Dal-Chawal":
        print("Dal-Chawal is for 20$")
    else:
        print("No more options available!")

if menu == "Dinner":
    print("You choose Dinner")

dinner = input("Choose any Dinner? (Biryani , Pulao):")

if dinner == "Biryani":
    print("Biryani is for 50$")

elif dinner == "Pulao":
    print("Pulao is for 35$")

else:
    print("No more options!")

# --------------------REAL WORLD EXAPMLE------------------------

print("Welcome to the Shopping Mart")
category = input("We have variety of collection choose from these (mens , womens):")

if category == "mens":
    print("You choose Mens's Clothes")

mens = input("Choose what to wear? (Normal , Part-Wear):")
if mens == "Normal":
    print("Normal Clothes is for 25$")

elif mens == "Party-Wear":
    print("Party-Wear is for 25$")

else :
    print("We have no more choice!")

if category == "womens":
    print("You choose Women's Clothes")

mens = input("Choose what to wear? (Normal , Part-Wear):")
if mens == "Normal":
    print("Normal Clothes is for 25$")

elif mens == "Party-Wear":
    print("Party-Wear is for 25$")

else :
    print("We have no more choice!")

# --------------------Loops and Iteration------------------------

#For loop

grocery_list = ["eggs , milk, butter"]
for items in grocery_list:
    print(f"buying: {items}")

# While loop

num = 6
while num > 0 :
    print(f"Remaining names: {num}")
    num -= 1
   
#break

key_list = ["living room", "kitchen", "bedroom", "bathroom"]  # Correct list format

for key in key_list:  # Iterating through each location
    if key == "bathroom":  # Checking if the current location is "bathroom"
        print("Found the key in the bathroom!")
        break  # Stop searching once the key is found
    print(f"Looking for the key in: {key}")  # Keep searching

#continue

months = ["january", "february", "march", "april", "may"]
for month in months:
    if month in ["january","may"]:
        continue
    print(f"This month is: {month}")

#nested

# List of days (Monday to Friday)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# List of subjects (rotating)
subjects = ["Math", "Science", "English", "History", "Computer", "Art"]

# Nested loop to generate timetable
for day in days:
    print(f"\n{day} Timetable:")
    for period in range(1, 7):  # 1st to 6th period
        subject = subjects[period - 1]  # Assign subject based on index
        print(f"  Period {period}: {subject}")

    



