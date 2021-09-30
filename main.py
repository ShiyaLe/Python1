""" Kieu List"""
    #Vi du ve List
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5 ]
    list3 = ["a", "b", "c", "d"]

    #Truy cap cac phan tu cua List
    list1 = ['physics', 'chemistry', 1997, 2000]
    list2 = [1, 2, 3, 4, 5, 6, 7 ]
    print("list1[0]: ", list1[0])
    print("list2[1:5]: ", list2[1:5])

    #Thay doi cac gia tri phan tu
    list = ['physics', 'chemistry', 1997, 2000]
    print("Value available at index 2 : ")
    print(list[2])
    list[2] = 2001
    print("New value available at index 2 : ")
    print(list[2])

    #Xoa phan tu cua List
    list1 = ['physics', 'chemistry', 1997, 2000]
    print(list1)
    del list1[2]
    print("After deleting value at index 2 : ")
    print(list1)

""" Kieu Tuples """
        #Khoi tao Tuples
        tup1 = ('physics', 'chemistry', 1997, 2000)
        tup2 = (1, 2, 3, 4, 5 )
        tup3 = "a", "b", "c", "d"
        tup1 = ()
        tup1 = (50,)

        #Truy cap cac phan tu Tuples
        tup1 = ('physics', 'chemistry', 1997, 2000)
        tup2 = (1, 2, 3, 4, 5, 6, 7 )
        print("tup1[0]: ", tup1[0])
        print("tup2[1:5]: ", tup2[1:5])

        #Thay doi gia tri phan tu Tuples
        tup1 = (12, 34.56)
        tup2 = ('abc', 'xyz')
        # Following action is not valid for tuples
        # tup1[0] = 100;
        # So let's create a new tuple as follows
        tup3 = tup1 + tup2
        print(tup3)

        #Xoa gia tri phan tu Tuples
        tup = ('physics', 'chemistry', 1997, 2000)
        print(tup)
        del tup
        print("After deleting tup : ")
        print(tup)
        #tup is no longer exist

""" Kieu Dictionary """
#Khoi tao va truy cap
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
#dict['Name']: Zara
#dict['Age']: 7

#Thay doi gia tri phan tu
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
#dict['Age']: 8
#dict['School']: DPS School

#Xoa phan tu
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name'] # remove entry with key 'Name'
dict.clear() # remove all entries in dict
del dict # delete entire dictionary

""" Kieu Set"""
#Khoi tao
# Same as {"a", "b", "c"}
Set = set(["a", "b", "c"])
print("Set: ")
print(Set)
# Adding element to the set
Set.add("d")
print("\nSet after adding: ")
print(Set)
#Set:
#set(['a', 'c', 'b'])
#Set after adding:
#set(['a', 'c', 'b', 'd'])

#Them phan tu
# Creating a Set
people = {"Jay", "Idrish", "Archi"}
print("People: ")
print(people)
people.add("Daxit")
for i in range(1, 6):
people.add(i)
print("\nSet after adding element:", end = " ")
print(people)
#People: {'Archi', 'Idrish', 'Jay'}
#Set after adding element: {1, 2, 3, 4, 5, 'Jay',
# 'Daxit', 'Archi', 'Idrish'}

#Bot phan tu
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.discard("Sun")
print(Days)
#set(['Wed', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])

#Xoa toan bo
set1 = {1,2,3,4,5,6}
print("Initial set")
print(set1)
# This method will remove
# all the elements of the set
set1.clear()
print("\nSet after using clear() function")
print(set1)
#Initial set
#{1, 2, 3, 4, 5, 6}
#Set after using clear() function
#set()

#Phep hop
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
# Union using union() function
population = people.union(vampires)
print("Union using union() function")
print(population)
# Union using "|" operator
population = people|dracula
print("\nUnion using '|' operator")
print(population)
#Union using union() function
#{'Jay', 'Karan', 'Idrish', 'Arjun', 'Archil'}
#Union using '|' operator
#{'Jay', 'Raju', 'Deepanshu', 'Idrish', 'Archil'}

#Phep giao
#set1 = set()
for i in range(5):
set1.add(i)
set2 = {3, 4, 5, 6, 7, 8}
# Intersection using intersection() function
set3 = set1.intersection(set2)
print("Intersection using intersection() function")
print(set3)
# Intersection using "&" operator
set3 = set1 & set2
print("\nIntersection using '&' operator")
print(set3)
#Intersection using intersection() function
#{3, 4}
#Intersection using '&' operator {3, 4}

#Phep lieu
set1 = set()
for i in range(5):
set1.add(i)
set2 = {3, 4, 5, 6, 7, 8}
# Difference of two sets using difference() function
set3 = set1.difference(set2)
print(" Difference of two sets using difference() function")
print(set3)
# Difference of two sets using '-' operator
set3 = set1 - set2
print("\nDifference of two sets using '-' operator")
print(set3)
#Difference of two sets using difference() function
#{0, 1, 2}
#Difference of two sets using '-' operator {0, 1, 2}

#Kiem tra tap con, tap cha
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
#True
#True

""" Kieu Date, time """
#Lay thoi gian hien tai
import time; # This is required to include time module.
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)
#Number of ticks since 12:00am, January 1, 1970: 7186862.73399
localtime = time.localtime(time.time())
print("Local current time :", localtime)
#Local current time : time.struct_time(tm_year=2013, tm_mon=7,
#tm_mday=17, tm_hour=21, tm_min=26, tm_sec=3,
#tm_wday=2, tm_yday=198, tm_isdst=0)

#Dinh dang thoi gian
import time;
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)
#Local current time : Tue Jan 13 10:17:09 2009

#Lay lich 1 thang
import calendar
cal = calendar.month(2008, 1)
print("Here is the calendar:")
print(cal)
#Here is the calendar:
# January 2008
#Mo Tu We Th Fr Sa Su
# 1 2 3 4 5 6
# 7 8 9 10 11 12 13
#14 15 16 17 18 19 20
#21 22 23 24 25 26 27
#28 29 30 31


