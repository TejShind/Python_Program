"""
@Author: Tejaswini Shinde
@Date: 2022-04-29 8:20
@Last Modified by: Tejaswini Shinde
@Last Modified time: 4:20
@Title : Write a Stopwatch Program for measuring the time that elapses between the start and end clicks

"""
import time
def calculateTime(sec):
    """
        Description:
            Calculating time with time in HH:MM:SS(Hours:Mins:Seconds)
        Parameter:
            passing second as a parameter
        Return:
            Returning Lapsed time and convert in the formate hours,mins and seconds.
    """

    mins = sec // 60
    hours = mins // 60
    sec = sec % 60
   
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start : ")
start_time = time.time()

input("Press Enter to stop : ")
end_time = time.time()

time_lapsed = end_time - start_time
calculateTime(time_lapsed) 