#! /usr/local/bin/python3
# password-manager.py - an insecure toy app to store and retrieve passwords. 

import sys, pyperclip

PASSWORDS = {'email': 'F7ydsaoiujhasuiDUSA8',
             'blog': 'j)AS*DAS(DUJSAIDOSA(SA)*D)',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: python3 password-manager.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]    # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard!')
else:
    print('There is no account named ' + account)
