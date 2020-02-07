days = "sun mon tue wed thu fri sat"
months = "\n jan \n feb \n mar \n apr \n may \n jun \n jul \n aug \n sep \n oct \n nov \n dec"
# \n always type in a new line
print ("days in a week : ", days)
print ("months in a year : ", months)

print ("""
        This is an Example for 3 double quotes
        you can try typing multiple lines,
        3
        or 4
        or 5
        or even 6
        """
        )


Selenium will return None when getting the text if the element is not visible.

Python None

And it can not be changed from SeleniumLibrary side, because Selenium mimics what real users do and see.
And real users can not see the text of the hidden element.

And it does not matter how the element is searched from the DOM if element is not visible.

But there are ways to overcome the limitation of the Selenium,
example with JavaScript: document.getElementById("myBtn").textContent;

Selenium (and SeleniumLibrary) has one very specific purpose: test UI as user sees it.
It should not be used to test application logic or other complex stuff. That should do in other levels.
