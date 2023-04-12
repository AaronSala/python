from datetime import date
print('Pub entance age check')
year = int(input('input your year of birth: '))
age =int(date.today().year-year)
print (age)
if age<18:
    print("you are too young to be here")
elif age>18 and age<70:
    print('you are wellcome drink responsibly')
else:
    print('you are too old to be here. be safe at home')