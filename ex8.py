# 13 Jan, 2018
# 20 Jan, 2018
# 30 Jan, 2018



# assign a string to formatter
formatter = " {} {} {} {} "

# print f-string ( inserting 1, 2, 3, 4 in string formatter)
print(formatter.format(1, 2, 3, 4))
# print f-string ( inserting one, two, three, four in string formatter)
print(formatter.format("one", "two", "three", "four"))
# print f-string ( inserting True, false, false, true in string formatter)
print(formatter.format(True, False, False, True))
# print f-string ( inserting formatter in string formatter)
print(formatter.format(formatter, formatter, formatter, formatter))
# print f-string ( inserting some string in string formatter)
print(formatter.format(
                 "ankit",
                 "amit",
                 "ashish",
                 "sanjeev"
                  ))
