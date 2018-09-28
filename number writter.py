def func(x):
    x = int(x)
    if(x == 0):
        print("zero")
        return
    if(x < 10):
        if(x == 1):
            print("one"),
        if(x == 2):
            print("two"),
        if(x == 3):
            print("three"),
        if(x == 4):
            print("four"),
        if(x == 5):
            print("five"),
        if(x == 6):
            print("six"),
        if(x == 7):
            print("seven"),
        if(x == 8):
            print("eight"),
        if(x == 9):
            print("nine"),
    if(x < 20 and x > 9):
        if(x == 10):
            print("ten")
        if(x == 11):
            print("eleven")
        if(x == 12):
            print("twelve")
        if(x == 13):
            print("thirteen")
        if(x == 14):
            print("fourteen")
        if(x == 15):
            print("fifteen")
        if(x == 16):
            print("sixteen")
        if(x == 17):
            print("seventeen")
        if(x == 18):
            print("eighteen")
        if(x == 19):
            print("ninteen")
    if(x < 30 and x > 19):
        print("twenty"),
        if(x % 10 != 0):
            func(x % 10)
    if(x < 40 and x > 29):
        print("thirty"),
        if(x % 10 != 0):
            func(x % 10)
    if(x < 50 and x > 39):
        print("forty"),
        if(x % 10 != 0):
            func(x % 10)
    if(x < 60 and x > 49):
        print("fifty"),
        if(x % 10 != 0):
            func(x % 10)
    if(x < 70 and x > 59):
        print("sixty"),
        if(x % 10 != 0):
            func(x % 10)
    if(x < 80 and x > 69):
        print("seventy"),
        if(x % 10 != 0):
            func(x % 10)
    if(x < 90 and x > 79):
        print("eighty"),
        if(x % 10 != 0):
            func(x % 10)
    if(x < 100 and x > 89):
        print("ninety"),
        if(x % 10 != 0):
            func(x % 10)
    if(x > 99 and x < 1000):
        func(x / 100)
        print("hundred"),
        if(x % 10 != 0):
            func(x % 100)
    if(x > 999 and x < 1000000):
        func(x / 1000)
        print("thousand")
        if(x % 1000 != 0):
            func(x % 1000)
    if(x > 999999 and x < 1000000000):
        func(x / 1000000)
        print("million")
        if(x % 1000000 != 0):
            func(x % 1000000)
    if(x > 999999999 and x < 1000000000000):
        func(x / 1000000000)
        print("billion")
        if(x % 1000000000 != 0):
            func(x % 1000000000)

while(True):
    x = raw_input("say something")
    func(x)
    print("")
    print("")
        
