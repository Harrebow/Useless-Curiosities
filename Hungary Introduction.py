def introduction(first_name, last_name, country):
    if country == "Hungary":
        print("Hello, my name is", last_name, first_name)
    else:
        print("Hello, my name is", first_name, last_name)

introduction(input("please enter your first name: "), input("please enter your last name: "), input("please enter your country: "))
