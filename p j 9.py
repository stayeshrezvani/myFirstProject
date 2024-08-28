try:
    age=int(input("how old are you?"))
    print("your age is %s year old:"%age)
except ValueError:
    print("hi my friend you must enter a integer try again:")
