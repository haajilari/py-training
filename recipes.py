class Recipe():

    def __init__ (self, dish,items,time)-> None:
        self.dish=dish
        self.items=items
        self.time=time
        
    def constants(self):
        print("The dish is: ", self.dish +"has "+ str(self.items) +" items and the time taken is: ", str(self.time) + " minutes")


pizza = Recipe("Pizza", ["cheese", "tomato sauce", "dough"], 30)
pasta=Recipe("pasta", ["pasta", "tomato sauce", "olive oil"], 20)

print(pizza.items)    
print(pasta.items)
