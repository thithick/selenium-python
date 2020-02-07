# formatter = "%r %r %r %r "
# print formatter % (1,2,3,4)
# print formatter % ("one","two","three","four")
# print formatter % (True, False, False, True)
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % ( "I had this thing.", "That you could type up right."
#                 "But it didn't sing.",
#                 "So I said goodnight."
                # )

formatter = ("%r %r %r %r")
# from python 3 , all print function should have the function brackets
# this printing formatter pricisely reduce typing the date type declaring %d,%s,%r
print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
