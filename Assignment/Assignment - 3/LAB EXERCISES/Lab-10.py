#Aim :- Write a Python program to handle file exceptions and use the finally block for closing the file.

file = None

try:
    file = open('demo.txt')

    content = file.read()
    print("Content is")
    print(content)

except FileNotFoundError:
    print("File does not exists!..")

except Exception as e:
    print(e)

finally:
    if file:
        file.close()
        print("File closed Successfully!..")
        
    print("Program Execution Completed")