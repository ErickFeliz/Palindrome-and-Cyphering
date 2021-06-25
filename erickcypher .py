#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Imagine a program where a user inputs a word.

#The program then checks that word to see if it's a palindrome. Then, it returns the input in ERICKCYPHER, which is where every letter in the word gets shifted by the length of the word squared.

#Here's an example:

#Please input a word: madam

# Palindrome? YES

# Original UTF-8: \x6d\x61\x64\x61\x6d
# Word length: 5
# Squared root of 5: 25
# Value shift of 25: \x86\x7a\x7d\x7a\x86
# ERICKCYPHER: Æº}zÆ

# Python program to check if a given string is a rotation
# of a palindrome


	 
# A utility function to check if a string str is palindrome
def palindrome_checker(string):
 
    # Start from leftmost and rightmost corners of str
    l = 0
    h = len(string) - 1
 
    # Keep comparing characters while they are same
    while h > l:
        l+= 1 
        h-= 1
        if string[l-1] != string[h + 1]:
            return False
 
    # If we reach here, then all characters were matching   
    return True

#ERICKCYPHER converter function

def ERICKCYPHER(plain_text):
	cypher_text = ''
	length = len(plain_text)
	
	for l in plain_text:
		cypher_char = chr(ord(l)+(length**2))
		
		cypher_text += cypher_char
	
	return cypher_text
	
def unERICKCYPHER(cypher_text):
	plain_text = ''
	length = len(cypher_text)
	
	for l in cypher_text:
		plain_char = chr(ord(l)-(length**2))
		
		plain_text += plain_char
		
	return plain_text

#entry point of the program
while True:
	user_input = input('Please input a word:\t')
	if(palindrome_checker(user_input)): 
		print('Yes, it is palindrome')
	else:
		print('It is not palindrome')
	print(ERICKCYPHER(user_input))
	
	print(unERICKCYPHER(ERICKCYPHER(user_input)))
	
