##########################################
#
#  Treatment of strings with Python
#
#  Written by M.Yagyu, 10 May 2019
#
##########################################


# program string

##
##  Basic of string
##

print("Good morning!")
print("")

str="""
Good morning
Good afternoon
Good evening
"""

print(str)
print("")

###
### Connection of strings
###

tmp='Good'
tmp2=' Morning'
tmp3=' Afternoon'
tmp4=' Evening'

str2=tmp+tmp2
str3=tmp+tmp3
str4=tmp+tmp4

print(str2)
print(str3)
print(str4)

print("")

###
### Replacement of strings
###

print(str2.replace('Morning','Job!!'))
print("")

###
### Searching of strings
###

print('J' in str2)
print('M' in str2)


# end program
