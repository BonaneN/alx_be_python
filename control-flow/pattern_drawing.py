size = int(input("Enter the size of the pattern: "))
row = 0
    
#Use while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    # Print newline after each row
    print()
    row += 1
