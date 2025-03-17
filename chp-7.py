#---------SETS& FROZEN SETS --------------------

#A set in Python is a collection of unique items. Unlike lists or tuples, a set:
#✅ Does NOT allow duplicates
#✅ Has no fixed order (unordered)
#✅ Does NOT support indexing (no my_set[0])
#✅ Is mutable (you can add/remove items)

# Creating a set
my_set = {"apple", "banana", "cherry"}
empty_set = set()
print(my_set)

#Unique Elements
my_set = {"apple", "banana", "cherry", "cherry", "apple", "banana"}
print(my_set)

#Adding & Removing Items
#✅ add(item) – Adds an item
#✅ remove(item) – Removes an item (gives an error if not found)
#✅ discard(item) – Removes an item (NO error if not found)

my_set = {"apple", "banana", "cherry", "cherry", "apple", "banana", "kiwi", "mango", "watermelon"}
my_set.add("orange")
my_set.remove("apple")
my_set.discard("banana")
my_set.pop()
my_set.clear()
print(my_set)
print(len(my_set))

#Set Operations
#✅ Union (| or union()) → Combines two sets (removes duplicates)
#✅ **Intersection (& or `intersection()

set1 = {"apple", "banana", "cherry", "mango"}
set2 = {"kiwi", "mango", "watermelon", "grape"}
print(set1.union(set2))
print(set1 | set2)
print(set1.intersection(set2))
print(set1 & set2)
print(set1.difference(set2))
print(set1 - set2)
#Checking Membership (in Operator)
print("apple" in set1) 
#Set Symmetric Difference (^ or symmetric_difference())
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

#hashing
my_set = {10, 3, 5, 8}
print(my_set)  # Order is unpredictable

my_set.add(20)
print(my_set)  # Order may change

my_set.remove(10)
print(my_set)  # Order may change again

# Removing multiple elements at once
my_set.difference_update({3, 5})
print(my_set)  # Remaining elements


#🔥 Key Takeaways:
#✔ Sets remove duplicates automatically
#✔ Use union (|), intersection (&), difference (-), and symmetric difference (^) for set operations
#✔ Use remove() if you're sure an item exists, otherwise use discard()
#✔ Sets are unordered and do not support indexing
#✔ Understand hashing to predict how Python stores elements.
#✔ Be aware of rehashing and unordered behavior in sets.

# Creating a frozen set
my_frozenset = frozenset({"apple", "banana", "cherry"})
print(my_frozenset)
