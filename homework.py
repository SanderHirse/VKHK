import os
clear = os.system('clear');

def question():
 	return raw_input('Which function would you like to use? (upper, lower, capitalize, swapcase, lstrip) = ')
    
#Converter
def converter(name):
    if function_to_use == 'upper':
        #Return a copy of the string with all the cased characters converted to uppercase.
        print name.upper();
    elif function_to_use == 'lower':
        #Return a copy of the string with uppercase characters converted to lowercase and vice versa.
        print name.lower();
    elif function_to_use == 'capitalize':
        #Return a copy of the string with its first character capitalized and the rest lowercased.
        print name.capitalize();
    elif function_to_use == 'swapcase':
        #Return a copy of the string with uppercase characters converted to lowercase and vice versa.
        print name.swapcase();
    elif function_to_use == 'lstrip':
        strip = raw_input('Enter leading characters to remove = ')
        #Return a copy of the string with leading characters removed.
        print 'Removed characters ' + chars + ', left:' + name.lstrip(chars);
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
        print"Sorry, that wasn't Y or N. Try again."
        
