#1.)
#Asking for the number
num = int(input("Enter a number (1-7): "))
#The days of the week
if 1 == num: 
    print('The day you\'ve selected is: Monday.')
elif 2 == num: 
    print('The day you\'ve selected is: Tuesday.')
elif 3 == num: 
    print('The day you\'ve selected is: Wednesday.')
elif 4 == num: 
    print('The day you\'ve selected is: Thursday.')
elif 5 == num: 
    print('The day you\'ve selected is: Friday.')
elif 6 == num:
    print('The day you\'ve selected is: Saturday.')
elif 7 == num:
    print('The day you\'ve selected is: Sunday.')
else:
    print('Please enter a proper number (1-7)')
#------------------------------------------------------------

#2.)
#Rectangle inputs
leng1 = int(input('Please enter the lenght of rectangle 1: '))
wid1 = int(input('Please enter the width of rectangle 1: '))
leng2 = int(input('Please enter the lenght of rectangle 2: '))
wid2 = int(input('Please enter the width of rectangle 2: '))
#Area formulas
area1 = leng1 * wid1
area2 = leng2 * wid2
#The results
if area1 > area2:
    print('Rectangle 1 has the larger area.')
elif area1 == area2:
    print('Rectangle 1 and rectangle 2 have the same area.')
else:
    print('Rectangle 2 has the larger area.')
#------------------------------------------------------------

#3.)
#What is you age?
age = int(input('Please enter you age: '))
#The results
if age <= 1:
    print('Your age bracket is infant')
elif 1 < age < 13:
    print('Your age bracket is child')
elif 13 <= age < 20:
    print('Your age bracket is teenager')
else:
    print('Your age bracket is Adult')
#------------------------------------------------------------

#4.)
#The number input
num = int(input('Please enter a number (1-10): '))
#The output to roman numerals
if 1 == num: 
    print('The Roman numeral version of that number is: I')
elif 2 == num: 
    print('The Roman numeral version of that number is: II')
elif 3 == num: 
    print('The Roman numeral version of that number is: III')
elif 4 == num: 
    print('The Roman numeral version of that number is: IV')
elif 5 == num: 
    print('The Roman numeral version of that number is: V')
elif 6 == num:
    print('The Roman numeral version of that number is: VI')
elif 7 == num:
    print('The Roman numeral version of that number is: VII')
elif 8 == num:
    print('The Roman numeral version of that number is: VIII')
elif 9 == num:
    print('The Roman numeral version of that number is: IX.')
elif 10 == num:
    print('The Roman numeral version of that number is: X.')
else:
    print('Please enter a proper number (1-10)')
#------------------------------------------------------------

#5.)
#Weight input
mass = float(input('Please enter the mass of the object: '))
#Weight formula
weight = mass * 9.8
#How heavy is it?
if weight > 500: 
    print(f'This object is weighs {weight:,.2f}lbs, and is too heavy')
elif weight < 100: 
    print(f'This object is weighs {weight:,.2f}lbs, and is too light')
else:
    print(f'This object is weighs {weight:,.2f}lbs, and is good to go.')
#------------------------------------------------------------

#6.)
#Dates
print('In the following prompt please enter the month, day'
      ', and year that will fit this format: mm/dd/yy')
month = int(input('Please enter the month as a digit value: '))
day = int(input('Please enter the day: '))
year = int(input('Please enter the last two digits of the year: '))
#The output
if year == month * day: 
    print('This date is magic')
else: 
    print('This date is not magic')
#------------------------------------------------------------

#7.)
#color input
color1 = input('Please enter the name of a primary color: ')
color2 = input('Please enter a different primary color: ')
#Color mixes
if (color1 == 'yellow' and color2 == 'blue') or (color1 == 'blue' and color2 == 'yellow'):
    print('These two colors make Green!')
elif (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
    print('These two colors make Purple!')
elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
    print('These two colors make Orange!')
else:
    print('Error: Please select two different primary colors')
#------------------------------------------------------------

#8.)
#Hotdog inputs
attend = int(input('How many people are attending the cookout?: '))
meal = int(input('How many hotdogs will each person get?: '))
#Food variables, I had to look up that inverse function to get the value to always round up
#I think I overcomplicated the problem and was struggling lol
totaleat = (attend * meal) 
buybun = -(-totaleat // 8)
buydog = -(-totaleat //10)
leftdog =  (buydog * 10) - totaleat
leftbun = (buybun * 8) - totaleat
#The output
print(f'You will need to buy {buydog} packages of hotdogs')
print(f'You will have {leftdog} hotdogs left over')
print(f'You will need to buy {buybun} packages of hotdog buns')
print(f'You will have {leftbun} hotdog buns left over')
#------------------------------------------------------------

#9.)
#Roulette wheels
pocket = int(input('Please enter a pocket number (0-36): '))
#The output
if 0 <= pocket <= 36:
    if pocket == 0:
        print(f'Pocket {pocket} is green')
    elif 1 <= pocket <= 10:
        if pocket % 2 == 0:
            print(f'Pocket {pocket} is black')
        else:
            print(f'Pocket {pocket} is red')
    elif 11 <= pocket <= 18:
        if pocket % 2 == 0:
            print(f'Pocket {pocket} is black')
        else:
            print(f'Pocket {pocket} is red') 
    elif 19 <= pocket <= 28:
        if pocket % 2 == 0:
            print(f'Pocket {pocket} is black')
        else:
            print(f'Pocket {pocket} is red')
    elif 29 <= pocket <= 36:
        if pocket % 2 == 0:
            print(f'Pocket {pocket} is black')
        else:
            print(f'Pocket {pocket} is red')
else:
    print('Error: Please select a number 0-36')

#------------------------------------------------------------

#10.)
#Lots of coins
pnny = int(input('Enter the total amount of Pennies: '))
nickl = int(input('Enter the total amount of Nickels: '))
dime = int(input('Enter the total amount of Dimes: '))
quart = int(input('Enter the total amount of Quarters: '))
#converting coins to cents
centsPnny = pnny * 1
centsNickl = nickl * 5
centsDime = dime * 10
centsQuart = quart * 25
centsTotal = centsPnny + centsDime + centsNickl + centsQuart
#the output
if centsTotal == 100:
    print('The coins add up to $1!\n'
          'You\'ve won the game!')
elif centsTotal < 100:
    print('Sorry, the coins entered are less than $1.')
else:
    print('Sorry, the coins entered are more than $1.')
#------------------------------------------------------------

#11.)
#Book purchases
books = int(input('Enter the amount of books purchased for the month: '))
#the output
if 1 <= books <= 3:
    print('You have earned 5 points this month.')
elif 4 <= books <= 5:
    print('You have earned 15 points this month.')
elif 6 <= books <= 7:
    print('You have earned 30 points this month.')
elif 8 <= books:
    print('You have earned 60 points this month.')
else:
    print('You have earned 0 points this month.')
#------------------------------------------------------------

#12.)
#Software purchases
softPkg = float(input('Please enter the total package amount: '))
#price
price = (99 * softPkg)
#discounts
disc10 = (price * .10)
disc20 = (price * .20)
disc30 = (price * .30)
disc40 = (price * .40)
#final price
price10 = price - disc10
price20 = price - disc10
price30 = price - disc10
price40 = price - disc10
#the output
if 10 <= softPkg <= 19:
    print(f'You will receive a 10% discount!\n'
          f'You saved {disc10:,.2f} with this order\n'
          f'Your new total is: {price10:,.2f}')
elif 20 <= softPkg <= 49:
    print(f'You will receive a 20% discount!\n'
          f'You saved {disc20:,.2f} with this order\n'
          f'Your new total is: {price20:,.2f}')
elif 50 <= softPkg <= 99:
    print(f'You will receive a 30% discount!\n'
          f'You saved {disc30:,.2f} with this order\n'
          f'Your new total is: {price30:,.2f}')
elif softPkg >= 100:
    print(f'You will receive a 40% discount!\n'
          f'You saved {disc40:,.2f} with this order\n'
          f'Your new total is: {price40:,.2f}')
else:
    print(f'Your total is: {price:,.2f}')
#------------------------------------------------------------

#13.)
#Weight check
weight = float(input('Please enter the package weight in pounds: '))
#price
rateLowest = weight * 1.50
rateSmall = weight * 3.00
rateMed = weight * 4.00
rateLarge = weight * 4.75
#the output
if weight <= 2:
    print(f'Shipping this item will cost {rateLowest:.2f}')
if 2 < weight <= 6:
    print(f'Shipping this item will cost {rateSmall:.2f}')
if 6 < weight <= 10:
    print(f'Shipping this item will cost {rateMed:.2f}')
if weight >= 10:
    print(f'Shipping this item will cost {rateLarge:.2f}')
#------------------------------------------------------------

#14.)
#Time inputs
sec = int(input("Enter the number of seconds: "))
#minute formulas
if sec < 3600:
    min = sec // 60
    sec = sec % 60
    print(f'This equals: {min} minute(s), {sec} second(s)')

#Hour formulas
elif 3600 <= sec < 84600:
    hours = sec // 3600
    min = (sec % 3600) // 60
    sec = (sec % 3600) % 60
    print(f'This equals {hours} hour(s), {min} minute(s), {sec} second(s)')

#day formulas
else:
    days = sec // 86400
    hours = (sec % 86400) // 3600
    min = ((sec % 86400) % 3600) // 60
    sec = ((sec % 86400) % 3600) % 60
    print(f'This equals {days} day(s), {hours} hours(s), {min} minute(s), {sec} second(s)')
#------------------------------------------------------------

#15.)
#Year inputs
year = int(input("Please enter a year: "))

#year formulas
if year % 100 == 0:
    if year % 400 == 0:
        print(f'In {year} Febrary has 29 days')
    else:
        print(f'In {year} February has 28 days')
else:
    if year % 4 == 0:
        print(f'In {year} Febrary has 29 days')
    else:
        print(f'In {year} February has 28 days')
#------------------------------------------------------------

#16.)
#Wifi troubleshooting
print('Reboot the computer and try to connect')
probcomp = input("Did that fix the problem?: ")
#branch start. This is probably very messy and
#and all those variations overcomplicate it
#but it's just something I felt was right, so sorry about that
if probcomp == "no" or "No" or "NO" or "N" or "nO" or "n":
    print('Reboot the router and try to connect')
    probrouter = input("Did that fix the problem?: ")
    if probrouter == "no" or "No" or "NO" or "N" or "nO" or "n":
        print('Make sure the cables between the router & modem are plugged in firmly.')
        probcable = input("Did that fix the problem?: ")
        if probcable == "no" or "No" or "NO" or "N" or "nO" or "n":
            print('Move the router to a new loacation and try to connect.')
            probmove = input('Did that fix the problem?: ')
            if probmove == "no" or "No" or "NO" or "N" or "nO" or "n":
                print('Get a new router')
#------------------------------------------------------------

#17.)
#Restaurants
vegetar = input('Is anyone in your party a vegetarian (Yes/No)?: ')
vegan = input('Is anyone in your party a vegan (Yes/No)?: ')
gluten = input('Is anyone in your party a gluten-free (Yes/No)?: ')
# Lots of ifs
if vegetar == "Yes" and vegan == "No" and gluten == "No":
    print('Your restaurant choices are:\n' 
          'Main Street Pizza Company\n'
          'Corner Café\n'
          'Mama\'s Fine Italian\n'
          'The Chef\'s Kitchen')
elif vegetar == "Yes" and vegan == "Yes" and gluten == "No":
    print('Your restaurant choices are:\n' 
          'Corner Café\n'
          'The Chef\'s Kitchen')
elif vegetar == "Yes" and vegan == "Yes" and gluten == "Yes":
    print('Your restaurant choices are:\n' 
          'Corner Café')
elif vegetar == "Yes" and vegan == "No" and gluten == "Yes":
    print('Your restaurant choices are:\n' 
          'Main Street Pizza Company\n'
          'Corner Café\n'
          'The Chef\'s Kitchen')
elif vegetar == "No" and vegan == "Yes" and gluten == "Yes":
    print('Your restaurant choices are:\n' 
          'Corner Café\n'
          'The Chef\'s Kitchen')
elif vegetar == "No" and vegan == "No" and gluten == "Yes":
    print('Your restaurant choices are:\n' 
          'Main Street Pizza Company\n'
          'Corner Café\n'
          'The Chef\'s Kitchen')
else:
    print('Your restaurant choices are:\n' 
          'Joe\'s Gourmet Burgers\n'
          'Main Street Pizza Company\n'
          'Corner Café\n'
          'Mama\'s Fine Italian\n'
          'The Chef\'s Kitchen')