#---------------LIST & TUPLES --------------------

shopping_list = ["comb", "hair-clips", "hair-bands"]
print(shopping_list)

print(shopping_list[0]) #positive indexing
print(shopping_list[-2]) #negative indexing

shopping_list[-1] = "dresses" #Changing List Items
print(shopping_list)

shopping_list.append("jeans") #adding list item
print(shopping_list)
shopping_list.extend(["kid-clothes", "mens-clothes"])
print(shopping_list)

shopping_list.remove("jeans") #removing item
print(shopping_list)

deleted_item = shopping_list.pop(3) #popping item
print(deleted_item)
print(shopping_list)

#sorting list item (Ascending Order)
ages = [56 , 55 , 20, 30] 
ages.sort() 
print(ages)
names = ["ali" , "basim", "zainab", "daniyal"]
names.sort()
print(names)

#sorting list item (Descending Order)
ages = [56 , 55 , 20, 30]
ages.sort(reverse=True) 
print(ages)
names = ["ali" , "basim", "zainab", "daniyal"]
names.sort(reverse=True)
print(names)

#looping through list
for item in shopping_list:
    print(item)

 #Reversing a List
ages = [556,78,23,12]
ages.reverse()
print(ages)

#List Slicing (Extracting Elements)
shopping_list = ["pants", "jeans", "denim-shirt"]
print(shopping_list[1:2])

# Sorting by String Length (key=len)
grocery = ["daal", "chawal", "oil", "butter"]
grocery.sort(key=len)
print(grocery)

#Sorting by Last Character (key=lambda word: word[-1])
grocery = ["daal", "chawal", "oil", "butter"]
grocery.sort(key=lambda word: word[-2])
print(grocery)

#-----------------List Comprehension --------------------------------

#new_list = [expression for element in iterable if condition]
#expression is the operation you want to perform on each element.
#element is the variable that takes on the value of each element in the iterable.
#iterable is the list or other iterable that you want to process.
#condition is an optional filter that determines whether an element is included in the new list.

#example without condition
balloon_colors = [ x*3 for x in ["red", "green", "blue", "yellow"]]
print(balloon_colors)

#example with condition
balloon_colors = [ x*3 for x in ["red", "green", "blue", "yellow"] if len(x) > 4]
print(balloon_colors)

balloon_colors = [ x.upper() for x in ["red", "green", "blue", "yellow"]]
print(balloon_colors)

balloon_colors = [ x.lower() for x in ["red", "green", "blue", "yellow"]]
print(balloon_colors)

#-------------------Tuples in Python --------------------------------

ages = (1 , 3 , 4 , 5, 8)
grocery = ("apple" , "banana" , "orange")
mixed = ("apple" ,1, "banana" ,0.1, "orange")
print(mixed)
print(ages)
print(grocery)

#indexing
print(mixed[0])
print(grocery[-3])
print(ages[-1])

#Even though tuples are immutable, Python may create new instances in memory when you define identical tuples in separate assignments. This is why id(ages) and id(ages_1) may differ.
ages = (30, 40 , 50)
ages2 = (30, 40 , 50)
print(id(ages))
print(id(ages2))
print(ages == ages2)

#real life example 
shopping_list = ("hair-bands", "clips", "sandals")
shopping_list2 = ("hair-bands", "clips", "sandals")
print(id(shopping_list))
print(id(shopping_list2))
print(shopping_list == shopping_list2)

# Tuples Are Immutable
#shopping_list = ("hai-bands", "clips", "sandals")
#shopping_list[0] = "jeans"
#print(shopping_list) #this will throw error
#TypeError: 'tuple' object does not support item assignment

# Lists Are Mutable
shopping_list = ["hair-bands", "clips", "sandals"]
shopping_list[0] = "jeans"
print(shopping_list)

#Why Are Lists Mutable?
#A mutable object is one that can be changed after it is created. In Python, lists are mutable because you can:
#✔️ Add elements (append(), extend(), insert())
#✔️ Remove elements (remove(), pop(), clear())
#✔️ Modify elements (list[index] = new_value)

#Slicing Tuples
shopping_list = ("hair-bands", "clips", "sandals")
print(shopping_list[:2])
print(shopping_list[:1])
print(shopping_list[1:])
print(shopping_list[2:])

#Tuple Length
shopping_list = ("hair-bands", "clips", "sandals")
print(len(shopping_list[0]))
print(len(shopping_list))

# Iterating through a tuple
shopping_list = ("hair-bands", "clips", "sandals")
for item in shopping_list:
  print(item)

# Checking if an item exists in a tuple
shopping_list = ("hair-bands", "clips", "sandals")
print("clips" in shopping_list)
print("jeans" in shopping_list)

#Concatenating (Joining) Tuples
shopping_list = ("hair-bands", "clips", "sandals")
grocery_list = ("milk", "oil", "butter")
print(shopping_list + grocery_list)

#Repeating a Tuple
shopping_list = ("hair-bands", "clips", "sandals")
print(shopping_list * 2)

# Nested Tuples
nested_tuple_list = (shopping_list , grocery_list)
print(nested_tuple_list)

#Unpacking Tuples
shopping_list = ("hair-bands", "clips", "sandals")  

# Unpacking the tuple into variables
item1, item2, item3 = shopping_list  

# Printing values
print(item1, item2, item3)  


#Accessing Tuple Elements
shopping_list = ("hair-bands", "clips", "sandals")
print(shopping_list[0])
print(shopping_list[-2])

#Counting & Finding Items in a Tuple
shopping_list = ("hair-bands", "clips", "sandals")
grocery_list = ("milk", "oil", "butter")
print(shopping_list.count("sandals"))
print(grocery_list.index("butter"))

#-----------Tuples are Immutable --------------------------------

#shopping_list[1] = "watermelon" 
#print(shopping_list) # ❌ This will cause an error
#You cannot change a tuple’s elements once it is created.

#------------------------------------------------------------------

# tuple1.sort()   # ❌ Tuples cannot be sorted (only lists can)
# tuple1.reverse() # ❌ Tuples cannot be reversed
# tuple1.append("mango") # ❌ Tuples cannot be modified (no append)
# tuple1.extend(["grape", "kiwi"]) # ❌ Tuples do not support extend
# tuple1.remove("banana") # ❌ Tuples do not support item removal
# deleted = tuple1.pop(1) # ❌ Tuples do not support pop
##❗ Why do these fail?
#Tuples are immutable → You cannot change, add, or remove items.
#These methods (sort(), reverse(), append(), etc.) only work on lists.

#Python is Type Hint Language
shopping_list:int = input("What do you want to add in your Shopping List?")
print(shopping_list,type(shopping_list))

#---------------Dictionaries in Python --------------------------------

todo_list = dict(
   house_chores = "brooming",
   school_work = "math",
   kitchen_chores = "cleaning dishes"
)
print(todo_list)

## Accessing Dictionary Values
print(todo_list["house_chores"])
print(todo_list.get("school_work"))
print(todo_list.get("home_work", "Not Found"))  # If key is missing, return "Not Found"

## Adding and Updating a Dictionary
todo_list["grocery"] = "milk"  # Adding a new key-value
todo_list["school_work"] = "english"  # Updating an existing value
print(todo_list)

## Deleting Dictionary Items
del todo_list["grocery"] # Removes 'grocery' from dictionary

school_work = todo_list.pop("school_work") # Removes and returns 'grocery'
print(school_work)

print(todo_list)

## Dictionary Methods
print(todo_list.keys())
print(todo_list.values())
print(todo_list.items())

# Updating dictionary
todo_list.update(dict(
   grocery = "milk"
))
print(todo_list)

# Clearing dictionary
todo_list.clear()
print(todo_list)

# Looping Through a Dictionary
todo_list = dict(
   house_chores = "brooming",
   school_work = "math",
   kitchen_chores = "cleaning dishes"
)
for key in todo_list:
   print(key)

for key,value in todo_list.items():
   print(f"{key} : {value}")
   
# Count the frequency of words in a sentence

sentence = "My name is Faria Mustaqim"
words = sentence.split()
word_count = dict()
for word in words:
   word_count[word] = word_count.get(word , 0) + 1
print(word_count)

#Practical Example
# Grocery List Dictionary
shopping_list = {
    "clips": 5,
    "bands": 3,
    "nail-polish": 2
}

# Add an item to the list
shopping_list["jeans"] = 1

# Update the quantity of an existing item
shopping_list["bands"] = 6

# Remove an item from the list
del shopping_list["nail-polish"]

# Print the updated grocery list
print("Updated Shopping List:")
for item, quantity in shopping_list.items():
    print(f"{item}: {quantity}")

#Checking if a Key Exists
todo_list = dict(
   house_chores = "brooming",
   school_work = "math",
   kitchen_chores = "cleaning dishes"
)
if "house_chores" in todo_list:
   print("House Chores found")
else:
   print("House Chores not found")

#Dictionary Length
todo_list = dict(
   house_chores = "brooming",
   school_work = "math",
   kitchen_chores = "cleaning dishes"
)
print(len(todo_list))

#Creating a Dictionary from Iterable
todo_list = [(" house_chores","brooming")]
new_dict = dict(todo_list)
print(new_dict)

#Copying a Dictionary
copied_dict = todo_list.copy()
print(copied_dict)

# Nested Dictionaries
nested_dict = {
   "house_chores" : {"brooming":"launch" , "mopping":"launch"},
   "kitchen_chores" : {"washing":"dishes" , "organize":"plates"}
}
print(nested_dict)
print("To-Do list :" ,nested_dict["house_chores"]["brooming"])