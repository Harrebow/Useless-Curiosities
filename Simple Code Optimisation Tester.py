import datetime
a = []

def test():
    count = 0
    for i in range(0, 100001):
        if i % 2 != 0:
            count+=1
            print(i)
    
    # count = 0
    # i = 1
    # while i < 100001:
    #     if i % 2 != 0:
    #         count+=1
    #         print(i)
    #     i += 1

    # i=1
    # while i != 100001:
    #     print(i)
    #     i+=2


y = datetime.datetime.now()
test()
x = datetime.datetime.now()
z=x-y
a.append(z)
y = datetime.datetime.now()
test()
x = datetime.datetime.now()
z=x-y
a.append(z)
y = datetime.datetime.now()
test()
x = datetime.datetime.now()
z=x-y
a.append(z)

print(a)
