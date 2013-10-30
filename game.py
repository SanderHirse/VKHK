print 'Welcome to "CaveGame"'

mynum = raw_input('Press any key to continue')

loading = 0;

warrior_class = 1;
mage_class = 2;
ranger_class = 3;

for loading in range(0,101):
    print 'Loading detail id', loading
    if loading == 100:

    	username = raw_input ('Enter your character name = ');

    	char_class = raw_input ('Choose your class (1 - Warrior, 2 - Mage, 3 - Ranger) = ');
    	if char_class == 1:
    		print 'test'
    	#if char_class == 1:
    	#	raw_input('You choosed', warrior_class, 'Press any key to start your journey!');
    	#if char_class == 2:
    	#	raw_input('You choosed', mage_class, 'Press any key to start your journey!');
    	#if char_class == 3:
    	#	raw_input('You choosed', ranger_class, 'Press any key to start your journey!');





