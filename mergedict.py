# Python script to merge two dictionaries
my_dict1={1: "blue", 2: "red", 3: "yellow"}
my_dict2={4: "green", 5: "black"}
print("Without Merge")
print(my_dict1)
print(my_dict2)
my_dict1.update(my_dict2)
print("After Merge")
print(my_dict1)