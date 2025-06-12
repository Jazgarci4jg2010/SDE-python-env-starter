def escape_room():
    name = input('HELLO FRIEND. What is your name?: ')
    print(f'Hello {name}, welcome to the Escape Room!\n')
    choose_a_door()
 
def choose_a_door():
    door = input('What door would you like to go through? 1, 2, or 3?: ')
    if door == '2':
        print('You won!')
    else:
        print('Wrong! Leave')
 
escape_room()



