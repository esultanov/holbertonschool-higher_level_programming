#!/usr/bin/python3
for i in range(10):
    for d in range(i + 1, 10):
        print("{}".format(str(i) + str(d)), end="")
        if int(str(i) + str(d)) < 89:
            print(", ", end="")
print("")
