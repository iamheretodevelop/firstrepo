
total = 0
# Use a while loop to take numbers from a user until they give a "q"
while True:
    user_input = input("Enter a number to add or q to finish: ")
    if user_input == "q":
        break
    else:
        total += int(user_input)

# Print the total out
print("The sum is:", total)