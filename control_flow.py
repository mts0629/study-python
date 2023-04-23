#!/usr/bin/env python
import typing

def main() -> None:
    # if statements
    x = int(input("Please enter an integer: "))
    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

    # for statement
    # Measure some strings:
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

    # Modify a collection while iterating over
    # that same collection
    # Create a simple collection
    users = {'Hans': 'active',
             'Éléonore': 'inactive',
             '景太郎': 'active'}

    # Strategy: Iterate over a copy
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]
    print(users)

    users = {'Hans': 'active',
             'Éléonore': 'inactive',
             '景太郎': 'active'}

    # Strategy: Create a new collection
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    print(active_users)

if __name__ == "__main__":
    main()
