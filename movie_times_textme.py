# TODO - build a tomatoes rating API - basically, is the movies good or not



# dictionary in Python
_dictAcronyms = {'LOL':'laugh out loud', 'IDK':'I don\'t know', 'TBH': 
'to be honest'}
#print(_dictAcronyms)

print("Text 616616 to get movie times show in your area")
print("Way easier than going to a crappy website")


class TimeAndDay:    
    date = str("01/15/2024")    # mm/dd/yyyy
    time = str("13:00:15")       # military start time

    def __init__(self,inStrmmddyyyy,inStrTimeMilitary):
        self.date = inStrmmddyyyy
        self.time = inStrTimeMilitary

class Movie:
    movieKey = 0     # primary key int 
    movieName = "not_set"
    moveRating = "not_set"    # G, PG, PG-13, R, NR, not_set
    movieTimesandDays = None  # TODO - needs to be list of objects

    def __init__(self, inObjTD):
        self.movieTimesandDays = inObjTD



t1 = TimeAndDay("01/15/2024","13:15:00")
m1 = Movie(t1)

_dictMovieTestData = {'specialkey': m1} 
print(_dictMovieTestData)


# example of list of lists structure
menus = [["Egg Sandwich", "Bagel", "Coffee"], ["BLT","PB and J", "Turkey Sandwich"],
["Soup","Salad","Speghetti","Taco"]]
print(menus)
#print(menus[1][2])

# how about dictionary of lists
_dict_menus = {"breakfast": ["Egg Sandwich", "Bagel", "Coffee"], "lunch": 
["BLT","PB and J", "Turkey Sandwich"]}

#print("Breakfast menu:\t", _dict_menus["breakfast"])
#print("Lunch menu:\t", _dict_menus["lunch"])

for key, value in _dict_menus.items():
    print(key, ":", value)

