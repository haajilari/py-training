def d():
    animal = "Dog"
    def e():
        nonlocal animal
        animal = "Cat"
        print("Inside e: ", animal)

    print("Inside d: ", animal)
    e()
    print("Inside d after calling e: ", animal)

animal = "Cow"
d()
print("Global animal: ", animal)