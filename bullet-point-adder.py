#! /usr/local/bin/python3
# bullet-point-adder.py - Adds Wikipedia bullet points to the start of each line
# of the text on the clipboard and returns it

import pyperclip

text = pyperclip.paste()
lines = text.split('\n')
text = ''

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
    
# print(lines)
text = '\n'.join(lines)
# print(text)
pyperclip.copy(text)
