#!/usr/bin/env python

import re

# Find patterns by regex
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# Substitute patterns by regex
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# Substitute patterns by string method
print('tea for too'.replace('too', 'two'))
