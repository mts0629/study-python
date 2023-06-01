#!/usr/bin/env python

def scope_test():
    def do_local():
        spam = "local spam" # Bind in local scope

    def do_nonlocal():
        nonlocal spam # Bind in outer scope
        spam = "nonlocal spam"

    def do_global():
        global spam # Bind in module scope
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam) # "test spam"

    do_nonlocal()
    print("After nonlocal assignment:", spam) # "nonlocal spam"

    do_global()
    print("After global assignment:", spam) # "nonlocal spam"

scope_test()
print("In global scope:", spam) # "global spam", there's no previous binding
                                # for `spam` before global assignment
