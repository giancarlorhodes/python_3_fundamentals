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
    movieTomatoMeter = "not_set"  # review system
    movieTimesandDays = None  # TODO - needs to be list of objects

    def __init__(self, inStrName, inStrRating, inStrPercentTomato, inListDaysAndTimes):
        self.movieTimesandDays = inListDaysAndTimes


t1 = TimeAndDay("01/15/2024","13:15:00")
t2 = TimeAndDay("01/16/2024","13:15:00")
t3 = TimeAndDay("01/17/2024","13:15:00")
m1 = Movie("Mean Girls", "PG-13", "70%", [t1,t2,t3])

t2 = TimeAndDay("01/16/2024","17:00:00") # reassignment
t3 = TimeAndDay("01/17/2024","17:00:00") # reassignment
m2 = Movie("The Beekeeper", "R", "69%", [t2,t3]) # reassignment

t1 = TimeAndDay("01/16/2024","13:00:00")
t2 = TimeAndDay("01/16/2024","17:00:00")
t3 = TimeAndDay("01/16/2024","21:00:00")
m3 = Movie("Wonka", "PG", "83%", [t1,t2,t3])

_dictMovieTestData = {}
_dictMovieTestData['MOCOL00001'] = m1 
_dictMovieTestData['MOCOL00002'] = m2
_dictMovieTestData['MOCOL00003'] = m3
print("Length of dictionary:", len(_dictMovieTestData))
for key, value in _dictMovieTestData.items():
    print(key, ":", value)


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
print("Modes are Q (quit), A (admin), 616616 (movie inquiry): ")
while _continue:
    _choice = input().upper()
    print("choice is: " + _choice)
    if _choice == "616616":
        print("ALL - list all movies, TODAY - list movies today, PURCHASE - purchase tickets, "
        "MENU - list commands")       
        _inner_continue = True
        while _inner_continue:
            _user = input().upper()
            if (_user == "TODAY"):
                print("TODO - only print today movies")               
            elif (_user == "ALL"):
                for key, value in _dictMovieTestData.items():
                    print(key, ":", value)
            elif (_user == "PURCHASE"):
                print("buying a ticket")
             
            elif (_user == "MENU"):
                print("TODAY - list movies today, PURCHASE - purchase tickets, "
                "MENU - list commands")
            else:
                _inner_continue = False

    elif (_choice == "A"):
        print("Administror mode ...")
        print("Modes are Q (quit), A (admin), 616616 (movie inquiry): ")

    elif _choice == "Q":
        print("quitting mode ...")
        print("Modes are Q (quit), A (admin), 616616 (movie inquiry): ")
        _continue = False

   


print("ending program ...")