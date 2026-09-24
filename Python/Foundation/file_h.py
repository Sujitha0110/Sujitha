ct = 1
while ct >= 0:
    std = input("Enter your name:")
    ct -= 1

# Method 1: Using basic open and read
file = open(r"C:\Users\AnudipCOA\Desktop\file_handling\std_details.txt", "r")
print(file.read())
file.close()  # Good practice: always close files opened with open()

# Method 2: Using context manager ('with' statement)
with open(r"C:\Users\AnudipCOA\Desktop\file_handling\std_details.txt", "r+") as file:
    content = file.write("Raj")
    print(content)