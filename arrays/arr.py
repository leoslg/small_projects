"""array of bytes"""

import array as arr

print("\n")
print("CREATING ARRAYS\n\n")

# Integer
arr_int = arr.array('i', [1, 3, 4, 5])

# Float
arr_float = arr.array('f', [1.1, 3.3, 4.4, 5.5])

# String
arr_str = arr.array('u', ['a', 'b', 'c', 'd', 'e'])


print("Integer Array: ", end="")
for i in range(len(arr_int)):
    print(arr_int[i], end=" ")
print("\n")

print("Float Array: ", end="")
for i in range(len(arr_float)):
    print(f"{arr_float[i]:.2f}", end=" ")
print("\n")

print("String Array: ", end="")
for i in range(len(arr_str)):
    print(arr_str[i], end=" ")
print("\n")
# 
# print("ARRAY OPERATIONS\n\n")
# 
# print("Adding an element at index: ")
# print("ArrayBeforeInsert: ", end="")
# for i in range(0,5):
#     print(arr_int[i], end=" ")
# 
# arr_int.insert(1, 2)
# 
# print("ArrayAfterInsert: ", end="")
# for i in range(0,5):
#     print(arr_int[i], end=" ")
# print("\n")
# 
# 
# print("Adding an element in the end of array: ")
# print("ArrayBeforeAppend: ", end="")
# for i in range(0,5):
#     print(arr_int[i], end=" ")
# 
# arr_int.append(6)
# 
# print("ArrayAfterAppend: ", end="")
# for i in range(0,6):
#     print(arr_int[i], end=" ")
# print("\n")
# 
# 
# print("NewArray: ", end="")
# for i in range(0,5):
#     print(arr_int[i], end=" ")
# print("\n")
# 
# print("PopElement: ", end="")
# print(arr_int.pop(3))
# print("\n")
# 
# print("ArrayPopped: ", end="")
# for i in range(0,4):
#     print(arr_int[i], end=" ")
# print("\n")
# 
# arr_int.remove(3)
# 
# print("ArrayAfterRemove: ", end="")
# for i in range(0,3):
#     print(arr_int[i], end=" ")
# print("\n")
# 