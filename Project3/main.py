print('''
        ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

print("You're in a cave where you found a map that tells you there's treasure buried underneath a tree just across a nearby lake. But first you need to exit the cave. You're at a cross road. Where do you want to go?")
direction = input("\tType \"left\" or \"right\"\n").lower()

if direction != "left":
    print("Oh no! You stepped on a trap which unleashed an array of fire arrows at you. Game over.")
    raise SystemExit


print("It was just a straight path leading outside. After a brief walk, you arrived at the lake but you see a boat in the distance heading your way. According to your estimate, it may take over 30 minutes to arrive. Will you swim across to make some progress on your own or will you wait for the boat to arrive and ask the captain to help you out?")
decision = input("\tType \"swim\" or \"wait\"\n").lower()

if decision != "wait":
    print("Uh oh! You didn't notice the paranhas and the electric eels nearby. You were stunned by the eels as the paranhas dug into your flesh. Sleep with the fishies! Game over.")
    raise SystemExit

print("Your estimate was off and it actually only took 10 minutes for the ship to arrive! Luckily the captain was nice enough to let you aboard the ship. The lake is vast; good thing you didn't overestimate your stamina. It will take about 30 minutes to reach your destination so the captain sent you to the cabin. However, you forgot which room you were assigned to. There are three doors, each color coded. Which will you choose?")
door = input("\tType \"red\", \"yellow\", or \"blue\"\n").lower()

if door == "red":
    print("Woah! This room isn't quite finished; you didn't notice in time due to your lack of patience and simply walked in without looking where your foot is. Your foot was stabbed by nails as you fell to the cold, hard ground causing a vibration that shook an unstable stack of barrels. You were crushed under immense weight. Game over.")
    raise SystemExit
elif door != "yellow":
    print("Yikes. You walked into a room of business men having a serious and highly illegal conversation. There can be no witnesses. You were shot on sight. Game over.")
    raise SystemExit

print("With an educated guess, you made it into the right room. After a light nap, you were informed by the captain that you reached your destination. Lo and behold, after exiting the ship and digging a small hole by the tree, you found a piece of moldy bread! Congratulations, you win!")

