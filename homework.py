import os
clear = os.system('clear');

def question():
	return raw_input('Wich function would you like to use? (upper, lower, capitalize, swapcase, lstrip) = ')

def again():
 	return raw_input('Try again? (yes/no) = ')

#Return a copy of the string with all the cased characters converted to uppercase.
def upper(name):
	print name.upper();
#Return a copy of the string with its first character capitalized and the rest lowercased.
def capitalize(name):
	print name.capitalize();
#Return a copy of the string with all the cased characters converted to lowercase.
def lower(name):
	print name.lower();
#Return a copy of the string with uppercase characters converted to lowercase and vice versa.
def swapcase(name):
	print name.swapcase();
#Return a copy of the string with leading characters removed.
def lstrip(name, chars):
	print 'Removed characters ' + chars + ', left:' + name.lstrip(chars);
#Converter
def converter(name):
    if function_to_use == 'upper':
        upper(name);
    elif function_to_use == 'lower':
        lower(name);
    elif function_to_use == 'capitalize':
        capitalize(name);
    elif function_to_use == 'swapcase':
        swapcase(name);
    elif function_to_use == 'lstrip':
        strip = raw_input('Enter leading characters to remove = ')
        lstrip(name,strip);
    else:
        print 'Command not found!'

#Question?
name = raw_input('Enter your name = ')
function_to_use = question()
converter(name);

#Try Again
while True:
    try_again = raw_input("Try again? (Y/N)")
    if try_again == "Y":
        name = raw_input('Enter your name = ')
        function_to_use = question()
        converter(name);
        pass
    elif try_again == "N":
        print "Bye!"
        break
    else:
        print"Please enter Y or N. Try again."
