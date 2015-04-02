#!/usr/bin/env python

# shopping_list = [
#     "hotdogs",
#     "gloves",
#     "hamburgers",
#     "bread"
# ]
# 
# 
# for item in shopping_list:
#     print "I want %s" % item

set_a = [
    12,
    32,
    -5,
    99,
    10394,
    832
]

set_b = [
    38,
    22,
    43,
    -9,
    11,
    -2929
]

# ticket = ("airplane", 37, "$399.99")  # immutable
# ticket_type, seatnumber, price = ticket

# print "I am flying on a %s in seat number %s, I paid %s for it" % ticket

len_of_a = range(len(set_a))

for idx in len_of_a:
    a = set_a[idx]
    b = set_b[idx]
    solution  = a + b
    print "%s + %s = %s" % (a, b, solution)


