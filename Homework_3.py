# remove_key.py

# Original dictionary
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print( myDict)

# Removing key 'a'
myDict.pop('a')

# Updated dictionary
print( myDict)

# check_key.py

# Given dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Input from user
key = int(input("Enter the key value which you want to check: "))

# Checking if key is in the dictionary
if key in d:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")

# max_min.py

# Given set
Set_Val = {2, 3, 5, 10, 15, 20}
print("Set Elements:", Set_Val)

# Finding max and min
print("Maximum value of the set is:", max(Set_Val))
print("Minimum value of the set is:", min(Set_Val))
