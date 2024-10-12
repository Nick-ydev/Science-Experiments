Project taken from the book https://automatetheboringstuff.com/ by AlSweigart in attempt to get better understanding of the language.

Link :https://inventwithpython.com/bigbookpython/project2.html

Description.
-   The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that two people will have the same birthday even in a small group of people. In a group of 70 people, there’s a 99.9 percent chance of two people having a matching birthday. But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday. This program performs several probability experiments to determine the percentages for groups of different sizes

~~Dictionary with names of month
Dictionary with dates~~ Did not work out.
Made a dictionary of months
Made a Dictionary of {Month : No. of days}

Function to generate birthdays. 
-  Call month
-  Upper limit = value associated with that month.
-  Make a pair
-  Call function N times and store the values in a list.

Function to check for duplicates
-  Call generated birthdays list
-  Count for all elements in list
-  return if count is more than 2

Finally iterate the birthdays 100,000 times to calculate probability %.


