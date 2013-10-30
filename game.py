import os;

clear = lambda: os.system('clear');
clear();

#Game name
print 'Welcome to "CaveGame" \n Made by Mihkel Baranov and Markus Land'

mynum = raw_input('Press any key to continue')

loading = 0;

warrior_class = 1;
mage_class = 2;
ranger_class = 3;

for loading in range(0,11):
    print 'Generating unique story', loading
    if loading == 10:

    	username = raw_input ('Enter your character name = ');
    	print 'Your character name is :', username;
    	char_class = raw_input ('Choose your class (1 - Warrior, 2 - Mage, 3 - Ranger) = ');
    	

     	print 'Your character class is', char_class
    	if char_class == '1':
    		print 'You choosed Warrior, ', username, '';
    		raw_input('Your are ready to play! \n Press any key to start your journey!');
    	if char_class == '2':
    		print 'You choosed Mage, ', username, '';
    		raw_input('Your are ready to play! \n Press any key to start your journey!');
    	if char_class == '3':
    		print 'You choosed Ranger, ', username, '';
    		raw_input('Your are ready to play! \n Press any key to start your journey!');
clear();

# Game Shitty Story:
raw_input('Long, long time ago in a Deep Forrest of Ilosgard \n there was a cave - press enter to continue');
clear();
raw_input('This Ordinary looking cave looked like a ordinary \n cave, - press enter to continue');
clear();
raw_input('Nothing special about it, but inside it was nothing \n like an ordinary cave - press enter to continue')
clear();
raw_input('it was special, Infused by Dark powers of Iloswag - press enter to continue')
clear();
print 'So... yeah... you are here (in front of the cave entrance) \n What to you do next?';
first_option = raw_input('(1 - Explore the cave), (2 - Leave, like lil b...) = ')

#If you entered the cave ehk Game Logics
if first_option == '1':
	clear();
	print 'You entered into the "CAVE"';
	second_option = raw_input('Do you want to take your shoes off? - yes/no = ' )
	if second_option == 'yes':
		raw_input('Walls are dirty and theres mud on the ground\n but your new Nikes didin\'t get dirty - press enter to continue')
	else:
		raw_input('Walls are dirty and theres mud on the ground \n also.. your new Nikes got dirty - press enter to continue')
	clear();

	third_option = raw_input('What to you do next? (1 - Move on, 2 - Go back, 3 - put your Nikes back on) = ');
	if third_option == '1':
		raw_input('You move on and on and on... until you get tired... zzzzzz')
	if third_option == '2':
		raw_input('I cant allow you to do that!')
	if third_option == '3':
		raw_input('You put your Nikes back on and start moving on')




else:
	print 'Noob'
	clear();


    

