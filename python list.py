# List length
fruits = ["apple", "banana","pawpaw"]
print(len(fruits))

# The list() construtor
fruits = list(("apple", "banana","pawpaw"))
print(fruits)

# Access list item (accessing refering to index number)
fruits = ["apple", "banana","pawpaw"]
print(fruits[3])

# Accessing refering to negative index
fruits = ["apple", "banana","pawpaw"]
print(fruits[-2])

#Ranges of indexes
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
print(fruits[1:3])

fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
print(fruits[:3])

fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
print(fruits[2:])

#Range of negative indexes
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
print(fruits[-1:-4])

# Check if item is in the list
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
if "banana" in fruits:
 print("yes 'banana' is in the fruits list")

 #change item value
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
fruits[4] = 'smoothies'
print(fruits)

#change a range of item value
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
fruits[1:4] = ["cashew", "mango", "pineapple"]
print(fruits)

#insert item
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
fruits.insert(3, "lemon")
print(fruits)

#Add list item (append item)
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
fruits.append("sugar cane")
print(fruits)

#extend item
fruits = ["apple", "kiwi","water melon" "banana","pawpaw"]
vegetables = ["carrot", "cabbage"]
fruits.extend(vegetables)
print(fruits)

#Remove list item


