import requests

class Search:

    def __init__(self, user):
        self.user = user

        # API
        self.base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        self.url = ""

        # Search
        self.word = ""

        self.query_status_code = None

        # Search Condiitons
        self.end_search = False

        # Special commands
        self.special_commands = ["sv"]

    # Getters
    def get_url(self):
        return self.url

    def get_base_url(self):
        return self.base_url

    def get_word(self):
        return self.word

    def get_query_status_code(self):
        return self.query_status_code

    def get_search_condition(self):
        return self.end_search

    # Setters
    def set_word(self, word):
        self.word = word

    def set_url(self):
        self.url = self.base_url + self.get_word()

    def set_query_status_code(self, query_status_code):
        self.query_status_code = query_status_code

    # Methods
    def search(self):
        query = requests.get(self.get_url())
        word_data = query.json()

        # Initialize an empty list to store definitions
        definitions = []

        # Iterate over meanings
        for meaning in word_data[0]["meanings"]:
            for definition in meaning["definitions"]:
                definitions.append(definition["definition"])

        for index, definition in enumerate(definitions):
            print(f"Definition {index + 1}: {definition}")

    def parse_user_command(self, user_command):
        list = user_command.split()
        if list[0] == "sv":
            return "save"
        else:
            return "search"

    def update(self, word):
        self.set_word(word)
        self.set_url()
        query_status_code = self.find_query_status_code()
        self.set_query_status_code(query_status_code)

    def find_query_status_code(self):
        query = requests.get(self.get_url())
        return query.status_code

    # Utility
    def end_search(self):
        self.end_search = True


