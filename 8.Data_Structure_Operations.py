"""
Operations on Strings, Lists , tuples and array :
  a. Creating lists/tuple/array and accessing list elements using index.
  b. Access the list/tuple element using –ve index.
  c. Extract specific element from list/tuple/array.
  d. Use len(), del(), remove() and range functions on list/tuple.
  e. Applying different searching and sorting algorithms on data (list)

"""
from array import *

arr = array("i", [2, 3, 4, 6, 8, 9, 15])
lst = ["Bark", "Meow", "Woof", "Roar","Moo","Buzz","Caw"]
tup = ("Bus", "Car", "Train", "Plane","Scooter","Metro","Cab")
print(arr)
print(lst)
print(tup)

print()

print("a. Creating lists/tuple/array and accessing list elements using index.")

print("Second element of list is : ", lst[1])
print("Third element of array is : ", arr[2])
print("Fourth element of tuple is : ", tup[3])
print()

print("b. Access the list/tuple element using –ve index.")

print("Second last element of list is : ", lst[-2])
print("Third last element of tuple is : ", tup[-3])
print()

print("c. Extract specific element from list/tuple/array.")

extract_elements = {2, 5, 'Meow', 'Car'}

# List extraction

for element in extract_elements:
    if element in lst:
        print(element)

# Tuple extraction

for element in extract_elements:
    if element in tup:
        print(element)

# Array extraction

for element in extract_elements:
    if element in arr:
        print(element)

print()

print("d. Use len(), del(), remove() and range functions on list/tuple.")

print()

print("Defined List is : ", lst)
print("Length of list is : ", len(lst))
del lst[2:4]
print("List after using del function : ", lst)
lst.remove("Moo")
print("List after using remove function : ", lst)
print()
print("Defined Tuple is : ", tup)
print("Length of tuple is : ", len(tup))

print()

print("e. Applying different searching and sorting algorithms on data (list)")

# SEARCHING


print()
