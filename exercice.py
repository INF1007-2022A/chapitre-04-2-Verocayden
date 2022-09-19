#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	first_part = name[0:name.find("-")]
	return first_part.capitalize()

def get_random_sentence(animals, adjectives, fruits):
	animal_choice = random.choice(animals)
	adjective_choice = random.choice(adjectives)
	fruit_choice = random.choice(fruits)
	random_sentence = f"Aujourd’hui, j’ai vu un {animal_choice} s’emparer d’un panier {adjective_choice} plein de {fruit_choice}."
	return random_sentence

def encrypt(text, shift): # Débug le débordement
	new_text = ""
	for letter in text:
		ord_letter = ord(letter)
		if 97 <= ord_letter <= 122: # minuscules
			ord_letter -= 32
		if 65 <= ord_letter <= 90:
			ord_letter += shift
			if ord_letter > 90:
				ord_letter = 64 + (ord_letter % 90)
		new_text += chr(ord_letter)
	return new_text

def decrypt(encrypted_text, shift):
	new_text = ""
	for letter in encrypted_text:
		ord_letter = ord(letter)
		if 97 <= ord_letter <= 122: # minuscules
			ord_letter -= 32
		if 65 <= ord_letter <= 90:
			ord_letter -= shift
			if ord_letter < 65:
				ord_letter = 91 - (65 % ord_letter) # Corriger
		new_text += chr(ord_letter)
	return new_text


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
