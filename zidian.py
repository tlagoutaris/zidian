import requests
import json

queries = 0

splash_message = "Jiajia's Zidian\n\nEnter a word, and I will tell you what it means "

print(splash_message)

while True:

    if queries == 0:
        word = input(">> ")
    else:
        word = input("\n>> ")

    URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    query = requests.get(URL)

    if query.status_code == 200:

        data = query.json()

        # Initialize an empty list to store definitions
        definitions = []

        # Iterate over meanings
        for meaning in data[0]["meanings"]:
            for definition in meaning["definitions"]:
                definitions.append(definition["definition"])

        for index, definition in enumerate(definitions):
            print(f"Definition {index + 1}: {definition}")

        queries += 1

    elif query.status_code == 404:
        print(f'"{word}" is not known or spelled incorrectly. ')
    else:
        print("Request could not be processed. ")
        break


