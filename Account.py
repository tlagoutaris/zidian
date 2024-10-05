import requests

class Account:

    def __init__(self):
        self.username = "username"
        self.to_learn_words = []
        self.learning_words = []
        self.conflicting_words_list = []
        self.saved_words = []
        self.first_time_starting_program = True
        self.first_query = True

    # Flags
    def first_time_starting_program_done(self):
        self.first_time_starting_program = False

    def first_query_done(self):
        self.first_query = False

    # Getters
    def get_name(self):
        return self.username

    def get_saved_words(self):
        return self.saved_words

    # Setters
    def set_name(self, name):
        self.username = name

        # Methods
    def save_word(self, word):
        if word not in self.saved_words:
            self.saved_words.append(word)
            print(f'Saved word: "{word}" ')
        else:
            print(f'"{word} is already saved. ')

    def remove_word(self, word):
        self.saved_words.remove(word)

    def add_unknown_word(self, word):
        self.to_learn_words.append(word)

    def remove_unknown_word(self, word):
        self.to_learn_words.remove(word)

    def add_learning_word(self, word):
        self.learning_words.append(word)

    def remove_learning_word(self, word):
        self.learning_words.remove(word)

    def create_conflicting_words_set(self):

        done = False
        word_count = 0
        new_conflicting_list = []
        while not done:
            if word_count == 0:
                word = input("Enter ")
            else:
                word = input("Enter")

            new_conflicting_list.append(word)

            word_count += 1

        self.conflicting_words_list.append(new_conflicting_list)

    def get_user_command(self):
        if self.first_query:
            return input(">> ")
        else:
            return input("\n>> ")

    def print_saved_words(self):

        if len(self.saved_words) == 0:
            print("You have no saved words. ")

        for i in self.saved_words:
            print(self.saved_words[i])





