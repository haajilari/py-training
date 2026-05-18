favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for dessert in favorites:
#     print('One of my favorite desserts is', dessert)


# count = 0

# while count < len(favorites):
#     print('One of my favorite desserts is', favorites[count]);
#     count += 1


# for dessert in favorites:
#     if dessert == 'Pudding':
#         print('Yes one of my favorite desserts is', dessert)
#         break 
#     else:
#         print('No sorry, not a dessert on my list')
#         break

# for dessert in favorites:
#     if dessert == 'Churros':
#         continue
#     print('Other desserts I like are', dessert) 


# for dessert in favorites:
#     if dessert == 'Churros':
#         pass
#     print('Other desserts I like are', dessert) 


for dessert in favorites:
    if dessert == 'Churros':
        print('Yes, one of my favorite desserts is', dessert)
        break
else:  # This else belongs to the for loop, not the if statement
    print('No sorry, not a dessert on my list')