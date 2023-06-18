#!/usr/bin/env python

# Raise multiple exceptions together with ExceptionGroup
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)

# f()

# try:
#     f()
# except ExceptionGroup as e:
#     print(f'caught {type(e)}: e') # caught <class 'ExceptionGroup'>: e

# Nested exception groups
def f():
    raise ExceptionGroup(
        "group1", [
            OSError(1), SystemError(2),
            ExceptionGroup("group2", [OSError(3), RecursionError(4)])
        ])

# Select the exception that match a certain type with `except*`
# RecursionError(4) in f() is re-raised
try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")

# Test class
class Test():
    def __init__(self, num):
        self.num = num

    def run(self):
        print(f"{10 / self.num}")

# Catch multiple exceptions raised by the program
excs = []
for test in [Test(1), Test(2), Test(0)]:
    try:
        test.run()
    except Exception as e:
        excs.append(e)
# And re-raise them
if excs:
    # Exceptions nested in an exception group must be instances
    raise ExceptionGroup("Test Failures", excs)
