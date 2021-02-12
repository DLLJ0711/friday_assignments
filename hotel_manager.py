hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

in_out = input('Are you checking "in" or "out"? ')

# for  in my_dicts:
#     for key in my_dict.items():
#         campaign_key = 'Campaign_Date'
#         if key == campaign_key:
#             if value == "":
#                 value = value["Another_Date"] 
#         else:
while True: 
    if in_out == "in":
        requested_floor = input('What floor would you prefer? ')
        requested_room = input('What room would you prefer? ')
        # if hotel.get('1')!= None:
        #     print ("This room is taken!")
        #     requested_floor = input('What floor would you prefer? ')
        #     requested_room = input('What room would you prefer? ')
        # number_occupants = input('How many occupants? ')
        name_occupants = list(map(str,input('What are their names? ').split(',')))
        hotel[requested_floor] = {requested_room: name_occupants}
        pprint(hotel)

    elif in_out == "out":
        floor_number = (input('What floor number? '))
        room_number = (input('What room number? '))
        hotel[floor_number][room_number]= None

        print(hotel)

# Write a program that does the following:

# * Display a menu asking whether to check in or check out.
# * Prompt the user for a floor number, then a room number.
#   * If checking in, ask for the number of occupants and what their names are.
#   * If checking out, remove the occupants from that room.
# * After checking in or out, display a list of all the occupants and their rooms.

# Additional Rules:

# * Do not allow anyone to check into a room that is _already occupied_!
# * Do not allow checking out of a room that _isn't occupied_!

# ### Hints

# * Start by writing down (_analog style, pen & paper, or in a text file_) all the steps you think a user will need to go through.
# * Use `input` to ask the user for their status (checking in/out), number of occupants, floor, and room numbers.
# * Use functions to break up your programs behaviors based on the responses.
#   * Functions should encapsulate the steps you outlined earlier.
#   * Examples _might_ include:
#     * Checking In
#     * Checking Out
#     * Assigning a room and floor during check in
#     * Clearing a room after check out
# * Use `while` loops and conditionals, `if...else` to determine if a room is available or not.
#   * For example `while occupants > 0 ...`
# * Start with just adding a single occupant to a room, _then_ add more.
# * A combination of a `for` loop and the `range()` function might be helpful when collecting a list of occupants names. [https://pynative.com/python-range-function/](https://pynative.com/python-range-function/)

# #### Bonus

# * Limit the max number of occupants in a room to 6.
# * Loop the program so that it goes back to the first question after displaying a list of all the occupants.
# * Import Python's `pprint` module for printing out the list of occupants. [https://docs.python.org/3/library/pprint.html](https://docs.python.org/3/library/pprint.html)