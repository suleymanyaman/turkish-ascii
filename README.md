# turkish-ascii
A Python library that helps the Turkish users to capitalize the characters. Python's default .capitalize() and .upper_case() methods don't support some upper-case Turkish letters.

The use of the module is very simple. Import the methods and pass the string or string object that you want to format as argument. The methods give the output as a return value.

Ex: 

>>>from turkish import capitalize

>>capitalize("istanbul")

'İstanbul'
(As a return value in Python IDLE)

>>>from turkish import capitalize

>>>print(capitalize("istanbul"))

İstanbul


>>>from turkish import upper_caser

>>>string = "Lorem ipsum dolor sit amet, id sea nisl option oportere."

>>>upper_caser(string)

'LOREM İPSUM DOLOR SİT AMET, İD SEA NİSL OPTİON OPORTERE.'


