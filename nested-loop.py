num_list = [33, 42, 5, 66, 77, 22, 16, 79, 36, 62, 78, 43, 88, 39, 53, 67, 89, 11]

# Step 5: Create counter outside the loop
count = 0

# Step 4: For loop with enumerate
for index, num in enumerate(num_list):
    # Step 6: Increment counter on every iteration
    count += 1
    
    # Step 1 & 2: Original printing logic replaced by new condition
    if num == 36:
        print('Number found at position:', index)
        break  # Step 8: Break after finding the number
    elif num > 45:
        print("Over 45")
    else:
        print("Under 45")

# Step 7: Print the final count
print("Total numbers processed:", count)