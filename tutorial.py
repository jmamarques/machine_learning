# This is a sample Python script.
import calendar
import sys
import random
import re
import time  # This is required to include time module.
import pymysql


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def check_value():
    print('The value of __name__ is ' + __name__)


def check_str():
    str = 'HelloWorld'

    print(str[2:5])
    print(str[2:])
    print(str * 2)


# Press the green button in the gutter to run the script.
def check_dir():
    dict = {"top": 10}
    print(dict)
    print(dict.keys())
    dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'}
    print("Variable Type : %s" % type(dict))
    pass


def check_for():
    for i in range(1, 5):
        print(i)
    pass


def check_iter():
    list = [1, 2, 3, 4]
    it = iter(list)  # this builds an iterator object
    print(next(it))  # prints next available element in iterator
    # Iterator object can be traversed using regular for statement
    for x in it:
        print(x, end=" ")


def fibonacci(n):  # generator function
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


def check_fibonacci():
    f = fibonacci(5)  # f is iterator object
    while True:
        try:
            print(next(f))
        except StopIteration:
            # sys.exit()
            break


def check_random():
    print("returns a random number from range(100) : ", random.choice(range(100)))
    print("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
    print("returns random character from string 'Hello World' : ", random.choice('Hello World'))
    # randomly select an odd number between 1-100
    print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
    # First random number
    print("random() : ", random.random())
    random.seed()
    print("random number with default seed", random.random())
    random.seed(10)
    print("random number with int seed", random.random())
    random.seed("hello", 2)
    print("random number with string seed", random.random())
    list = [20, 16, 10, 5]
    random.shuffle(list)
    print("Reshuffled list : ", list)
    print("Random Float uniform(5, 10) : ", random.uniform(5, 10))
    print("Random Float uniform(7, 14) : ", random.uniform(7, 14))


def check_time():
    ticks = time.time()
    print("Number of ticks since 12:00am, January 1, 1970:", ticks)
    print(time.localtime())
    localtime = time.asctime(time.localtime(time.time()))
    print("Local current time :", localtime)
    cal = calendar.month(2016, 2)
    print("Here is the calendar:")
    print(cal)
    pass


def check_regex():
    line = "Cats are smarter than dogs";

    matchObj = re.match(r'dogs', line, re.M | re.I)
    if matchObj:
        print("match --> matchObj.group() : ", matchObj.group())
    else:
        print("No match!!")

    searchObj = re.search(r'dogs', line, re.M | re.I)

    if searchObj:
        print("search --> searchObj.group() : ", searchObj.group())
    else:
        print("Nothing found!!")
    phone = "2004-959-559 # This is Phone Number"

    # Delete Python-style comments
    num = re.sub(r'#.*$', "", phone)
    print("Phone Num : ", num)

    # Remove anything other than digits
    num = re.sub(r'\D', "", phone)
    print("Phone Num : ", num)
    pass


def check_db():
    # Open database connection
    db = pymysql.connect(host='192.168.0.197', user='crypto', password='crypto12')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Database version : %s " % data)

    # disconnect from server
    db.close()
    pass


if __name__ == '__main__':
    print_hi('PyCharm')
    check_value()
    check_str()
    check_dir()
    check_for()
    check_iter()
    check_fibonacci()
    check_random()
    check_time()
    check_regex()
    check_db()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
