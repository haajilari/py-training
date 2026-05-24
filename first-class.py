class MyFirstClass:
    index = "Author-Book"

    def __init__(self):
        print("Who wrote this?")  # Move the print statement into the constructor

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        print(philosopher + " wrote the book: " + book)

# Instantiate the class
whodunnit = MyFirstClass()
# Call the method with parameters
whodunnit.hand_list("Sun Tzu", "The Art of War")