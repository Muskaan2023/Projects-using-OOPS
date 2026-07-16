class Time:
    def __init__(self,h,m,s):
        self.hours=h
        self.minutes=m
        self.seconds=s
    def __str__(self):
        return (f"{self.hours}:{self.minutes}:{self.seconds}")
    def __add__(self,other):
        hour=self.hours+other.hours
        minute=self.minutes+other.minutes
        second=self.seconds+other.seconds
        if second >= 60:
            minute += second // 60
            second = second % 60

        if minute >= 60:
            hour += minute // 60
            minute = minute % 60
        return Time(hour,minute,second)
print("Enter the time t1 values:")
h1=int(input("Enter the hour value:"))
m1=int(input("Enter the minute value:"))
s1=int(input("Enter the second value:"))
print("Enter the time t2 values:")
h2=int(input("Enter the hour value:"))
m2=int(input("Enter the minute value:"))
s2=int(input("Enter the second value:"))
t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
print(t1)
print(t2)
print(t1+t2)