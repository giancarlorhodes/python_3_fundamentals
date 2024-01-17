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
