#Aim :- Write a Python program to access elements at different index positions. 

my_list = [10,20,30,40,50,60,70]

# Access elements using index positions
print("First Element of Index = ",my_list[0])
print("Second Element of Index = ",my_list[1])
print("Third Element of Index = ",my_list[2])

print("\n")

# Access last element using negative index
print("Last Element of Index is = ",my_list[-1])
print("Second last Element of Index is = ",my_list[-2])

print("\n")

# Access multiple elements using slicing
print("Multiple Elements slicing 1 to 6 = ",my_list[1:6])

print("\n")

# Loop through list using index
for i in range(len(my_list)):
    print(f"Element at index {i} is {my_list[i]}")

