
# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min

age = int(input("How old are you in years?\n"))


# we might get a fraction part out of this
decades = age // 10  # whole number division, what happens to the fraction? are we rounding up or down?
years = age % 10  # get us the fraction part, modulus
print("decades: ", decades) # testing


print("You are " + str(decades) + " decades and " + str(years) + " years old.")

