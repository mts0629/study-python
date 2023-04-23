#!/usr/bin/env python

words = ['cat', 'window', 'defenestrate']

# for statements
# Measure the length of some strings
for w in words:
    print(w, len(w))

# A sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Modify a collection while iterating over theat same collection
# Strategy: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy: create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(users)
print(active_users)
