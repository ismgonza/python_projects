#! python3.7

import sys
passwords = {
    'email': 'email123',
    'blog': 'blog123',
    'money': 'money123'
}

#print('the name of this script is: ', sys.argv[0])
#print('the arguments are : ', sys.argv)
#print('the are {} arguments'.format(len(sys.argv)))

if len(sys.argv) < 2:
    print('Usage: python pw.py [account]')
    sys.exit()
else:
    account = sys.argv[1]
    if account in passwords:
        print('The password for {} is {}'.format(account, passwords[account]))
    else:
        print('There are no accounts named {}'.format(account))
