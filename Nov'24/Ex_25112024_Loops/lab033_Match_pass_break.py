# pass - pass the code and move further
# break - break the flow
# match -
city = input("enter city name")
match city:
    case ("firefox"):
        print("i know")
    case ("ifkf"):
        print("u know")
    case _:
        print("joke")
