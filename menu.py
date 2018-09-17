#!/usr/bin/python3.6
from char_suggestion import auto_complete_char
from file_ngrams import select_ngrams
from language import acronym_to_language, found_language
from tfidf import auto_complete_word

def menu():
    option = ""
    while option != "4":
        print("0. Détection de la langue")
        print("1. Suggestion d'un mot")
        print("2. Auto-complétion d'une phrase")
        print("3. Calcule des trigrammes à partir d'un dossier")
        print("4. Quitter\n")
        option = input("Choisissez une option: ")
        if option == "0":
            sentence = input("Saisissez une phrase:\n")
            print(acronym_to_language(found_language(sentence)))
        elif option == "1":
            sentence = input("Saisissez le début d'une phrase et d'un mot:\n")
            print(auto_complete_char(sentence))
        elif option == "2":
            sentence = input("Saisissez le début d'une phrase:\n")
            print(auto_complete_word(sentence))
        elif option == "3":
            path = input("Saisissez le path vers le dossier:\n")
            filename = input("Saisissez le nom du nouveau fichier:\n")
            select_ngrams(path, filename)
        elif option != "4":
            print("option non reconnue")
        print("\n")



menu()