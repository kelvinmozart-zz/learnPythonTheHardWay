#Exercise 10: What Was That?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

print ("\n\n")
while True:     #Comment this part before run the code
    for i in ["/","-","|","\\","|"]:    #then later
        print ("%s\r" % i,)             #try this part
