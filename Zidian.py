import Search
import Account

user = Account.Account()
Zidian = Search.Search(user)

first_message = "Hello, sorry to bother you, and sorry to be so intrusive, but may I have your name? \n"

if user.first_time_starting_program:
    print(first_message)
    name = input(">> ")
    user.set_name(name)
    user.first_time_starting_program_done()

splash_message = f"\n{user.get_name()}'s Zidian\n\nEnter a word, and I will tell you what it means "

print(splash_message)

while not Zidian.end_search:

    # 1. Get user command
    user_command = user.get_user_command()
    user_command_list = user_command.split()
    # 2. Parse user command -- determine the action
    type_of_command = Zidian.parse_user_command(user_command)
    # 3. If non-search, then do that command
    if type_of_command == "save":
        user.save_word(user_command_list[1])
    # 4. Else, check the query.status_code
    elif type_of_command == "search":
        word = user_command_list[0]
        Zidian.update(word)
        if Zidian.get_query_status_code() == 200:
            Zidian.search()
        # 6. Else if 404: print something but continue search
        elif Zidian.get_query_status_code() == 404:
            print(f'"{word}" is not known, or it is spelled incorrectly. ')
        # 7. Else: end_search()
        else:
            print("Request could not be processed. ")
            Zidian.end_search()







