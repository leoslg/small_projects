"""array of bytes"""

import array as arr
import time

print("\n")
print("CREATING ARRAYS, WAIT A SECOND!\n\n")
time.sleep(2)

# Integer
arr_int = arr.array("i", [1, 3, 4, 5])

# Float
arr_float = arr.array("f", [1.1, 3.3, 4.4, 5.5])

# String
arr_str = arr.array("u", ["a", "b", "c", "d"])

# Bytes
arr_bytes = bytearray([1, 2, 3, 4])

print("HERE! THE ARRAY'S\n\n")

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

print("Bytes Array: ", end="")
for i in range(len(arr_bytes)):
    print(arr_bytes[i], end=" ")
print("\n")

print("THE ARRAY OPERATIONS\n\n")

print("Adding an element at index: ")
print("ArrayBeforeInsert: ", end="")
for i in range(len(arr_int)):
    print(arr_int[i], end=" ")
print("\n")

arr_int.insert(1, 2)

print("ArrayAfterInsert: ", end="")
for i in range(len(arr_int)):
    print(arr_int[i], end=" ")
print("\n")
print("\n")


print("Adding an element in the end of array: ")
print("ArrayBeforeAppend: ", end="")
for i in range(len(arr_float)):
    print(f"{arr_float[i]:.2f}", end=" ")
print("\n")

arr_float.append(6.6)

print("ArrayAfterAppend: ", end="")
for i in range(len(arr_float)):
    print(f"{arr_float[i]:.2f}", end=" ")
print("\n")
print("\n")

print("Acessing an element: ")
print("A integer element: ", arr_int[3])
print("A float element: ", arr_float[3])
print("A string element: ", arr_str[3])
# print("A bytes element: ", arr_bytes[3])
print("\n")

print("Removing an element, using pop method: ")
print("ArrayBeforeRemove: ", end="")
for i in range(len(arr_str)):
    print(arr_str[i], end=" ")
print("\n")
arr_str.pop(3)

print("ArrayAfterRemove: ", end="")
for i in range(len(arr_str)):
    print(arr_str[i], end=" ")
print("\n")
print("\n")

print("Removing an element, using remove method: ")
print("ArrayBeforeRemove: ", end="")
for i in range(len(arr_int)):
    print(arr_int[i], end=" ")
print("\n")

arr_int.remove(2)

print("ArrayAfterRemove: ", end="")
for i in range(len(arr_int)):
    print(arr_int[i], end=" ")
print("\n")
print("\n")

print("Slicing an array: ")
print("ArrayBeforeSlice: ", end="")
for i in range(len(arr_int)):
    print(arr_int[i], end=" ")
print("\n")

sliced_arr = arr_int[1:3]

print("ArrayAfterSlice(using range[1:3]): ", end="")
print(sliced_arr)
print("\n")

sliced_arr = arr_int[2:]

print("ArrayAfterSlice(using range[2:]): ", end="")
print(sliced_arr)
print("\n")
print("\n")

print("Searching an element: ")
print("Index of 'b' element in string array: ", arr_str.index('b'))
print("\n")

print("Update an element: ")
print("ArrayBeforeUpdate: ", end="")
for i in range(len(arr_float)):
    print(f"{arr_float[i]:.2f}", end=" ")
print("\n")

arr_float[3] = 8.8

print("ArrayAfterUpdate: ", end="")
for i in range(len(arr_float)):
    print(f"{arr_float[i]:.2f}", end=" ")
print("\n")
print("\n")

print("Reverse an array: ")
print("ArrayBeforeReverse: ", end="")
for i in range(len(arr_float)):
    print(f"{arr_float[i]:.2f}", end=" ")
print("\n")

arr_float.reverse()

print("ArrayAfterReverse: ", end="")
for i in range(len(arr_float)):
    print(f"{arr_float[i]:.2f}", end=" ")
print("\n")
print("\n")

print("Counting an array: ")

print("Counting a ocurrences of '4.40' in float array: ", arr_float.count(3.30))
print("\n")
