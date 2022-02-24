
from _typeshed import Self
from os import system
time = []

def input_data():
    h = int(input("hour ="))
    if 0 <= h <= 23:
        time.append(h)
    else:
        time.append(0)
    m = int(input("minute :"))
    if 0 <= m < 60:
        time.append(m)
    else:
        time.append(0)
    s = int(input("second :"))
    if 0 <= s < 60:
        time.append(s)
    return time

def Show_menu():
    print("""
______________________________
|                            |
|   1- ADD two time          |
|   2- Mines tow time        | 
|   3- time to second        |
|   4- second to time        | 
|   5- EXIT                  |   
|____________________________|""")

def Second_to_time(input_second):
    result = Time()
    result.hour=input_second//3600
    temp=input_second-3600*result.hour
    result.miniute=temp//60
    result.second=temp-60*result.miniute
    return result

class Time:

    def __init__(self, s = 0, m = 0, h = 0, d =0):
        self.second = s
        self.miniute = m
        self.hour = h
        self.day = d

    def Show_time():
        if Self.day == 0:
            print(Self.hour," : ",Self.miniute," : ",Self.second)
        else:
            print("Day = ",Self.day,"\n",Self.hour," : ", Self.miniute, " : ",Self.second)

    def Which_is_bigger(self, other):
        if self.hour > other.hour:
            return self 
        elif self.hour < other.hour:
            return other
        elif self.miniute > other.miniute:
            return self
        elif self.miniute < other.miniute:
            return other
        elif self.second > other.second:
            return self
        elif self.second < other.second:
            return other
        elif self.hour == other.hour and self.miniute == other.miniute and self.second == other.second:
            return Time()
    def Add_times(self, other):
        result = Time()
        second_result = self.second + other.second
        miniute_result = self.miniute + other.miniute
        hour_result = self.hour + other.hour
        while second_result >= 60:
            second_result -= 60
            miniute_result += 1
        while miniute_result >= 60:
            miniute_result -= 60
            hour_result += 1
        while hour_result >= 24:
            hour_result -= 24
            self.day += 1
        result(second_result, miniute_result, hour_result, result.day)
        result.Show_time()
        return result
    
    def Mines_times(self,other):
        result = Time()
        if self.Which_is_bigger() == self:
            if self.second < other.second:
                if self.miniute == 0:
                    self.hour -= 1
                    self.miniute += 59
                    self.second += 60
                else:
                    self.miniute -=1
                    self.second += 60
             
            second_result = self.second - other.second
            if self.miniute < other.miniute:
                self.hour -= 1
                self.miniute += 60
            miniute_result = self.miniute - other.miniute
            hour_result = self.hour - other.hour

        elif self.Which_is_bigger() == other:
            if self.second > other.second:
                if other.miniute == 0:
                    other.hour -= 1
                    other.miniute += 59
                    other.second += 60
                else:
                    other.miniute -=1
                    other.second += 60
            second_result = other.second - self.second
            miniute_result = other.miniute - self.miniute
            hour_result = other.hour - self.hour
        else:
            result = Time(0,0,0,0)
            result.Show_time()
            return result
        result(second_result, miniute_result, hour_result, result.day)
        result.Show_time()
        return result
    
    def Time_to_second(self):
        sec=int(self.hour)*3600 + int(self.miniute)*60+ int(self.second)
        print("Time convert to second = ",sec)
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Main /////////////////////////////////////#
while True:
    Show_menu()
    choice = int(input("\ninsert a number from menu :"))
    if choice == 1:
        system("cls")
        print("Data for first TIME object")
        input_data()
        time1 = Time(time(0),time(1),time(2),0)
        time.clear()
        print("Data for second TIME object")
        input_data()
        time2 = Time(time(0),time(1),time(2),0)
        time.clear()
        result = Time.Add_times(time1,time2)
    elif choice == 2:
        system("cls")
        print("Data for first TIME object")
        input_data()
        time1 = Time(time(0),time(1),time(2),0)
        time.clear()
        print("Data for second TIME object")
        input_data()
        time2 = Time(time(0),time(1),time(2),0)
        time.clear()
        result = Time.Add_times(time1,time2)
    elif choice == 3:
        system("cls")
        print("Data for TIME object")
        input_data()
        time_object = Time(time(0),time(1),time(2),0)
        time.clear()
        time_object.Time_to_second()
    elif choice == 4:
        system("cls")
        sec = int(input("Enter second for convert to time :"))
        time_object = Second_to_time(sec)
        time_object.Show_time()    
    elif choice == 5:
        exit()
    else:
        print("!! command not found !! ")
