# we are going to see '\' in this Example

print (" I am 8'2\" tall ") # escaping double quotes inside a string
print ('I am 8\'2" tall') # escapting single quotes inside a string
tabby_cat ="\tI'm a  tabbed cat"
persian_cat = "I'm split\n on a line"
backslact_cat = "I'm \\ a \\ cat."

fat_cat = """
        this is multiline
        \t* cat food
        \t* fishies
        \t* catnip\n\t* Grass
        print
        """
print (tabby_cat)
print (persian_cat)
print (backslact_cat)
print (fat_cat)

# Escape sequence that python supports
\\ Backslash(\)
\' single quotes '
\" double quotes "
\n new line
\N{name}
\t Horizontal tab (TAB)
