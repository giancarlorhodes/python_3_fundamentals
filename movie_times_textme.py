

# Python 3 Fundamentals, by Sarah Holderness, Pluralsight, 2h 55min 
# TODO - build a tomatoes rating API - basically, is the movies good or not

# dictionary in Python
# _dictAcronyms = {'LOL':'laugh out loud', 'IDK':'I don\'t know', 'TBH': 
# 'to be honest'}
#print(_dictAcronyms)


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

# _dictMovieTestData = {'specialkey': m1} 
# print(_dictMovieTestData)


# example of list of lists structure
#menus = [["Egg Sandwich", "Bagel", "Coffee"], ["BLT","PB and J", "Turkey Sandwich"],
#["Soup","Salad","Speghetti","Taco"]]
#print(menus)
#print(menus[1][2])

# how about dictionary of lists
#_dict_menus = {"breakfast": ["Egg Sandwich", "Bagel", "Coffee"], "lunch": 
#["BLT","PB and J", "Turkey Sandwich"]}

#print("Breakfast menu:\t", _dict_menus["breakfast"])
#print("Lunch menu:\t", _dict_menus["lunch"])
#for key, value in _dict_menus.items():
#    print(key, ":", value)


print("Text 616616 to get movie times show in your area")
print("Way easier than going to a crappy website\n")

_continue = True
while _continue:
    _choice = input("Modes are Q (quit), A (admin), 616616 (movie inquiry): ").upper()
    print("choice is " + _choice)
    if _choice == "616616":
               
        _inner_continue = True
        while _inner_continue:
            _user = input().upper()
            if (_user == "TODAY"):
                print("print all movies for today.")
                
            elif (_user == "PURCHASE"):
                print("buying a ticket")
             
            elif (_user == "MENU"):
                print("TODAY - list movies today, PURCHASE - purchase tickets, "
                "MENU - list commands")
            else:
                _inner_continue = False

    elif _choice == "Q":
        _continue = False

   


print("ending program ...")