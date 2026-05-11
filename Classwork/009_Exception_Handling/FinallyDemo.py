#finally :- always executble thy


def test():
    try:
        a = int(input("Enter Number = "))
        return a
    except Exception as e:
        return e
    finally:
        print("Program Ended")

print(test())