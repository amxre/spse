#!/usr/bin/env python

import classdemo # use methods defined in the classdemo.py file
# or 
from classdemo import Scientific # importing specific subclass

# without instantiating a classdemo object
print 'Quick Add a+b: %d' % classdemo.quickAdd(10,20)

# instantiating a classdemo object and assigning it to a variable
instantiate = classdemo.Scientific(5,6)

print '%d' % instantiate.power()

# Using the specific subclass you imported using "from"

instantiate2 = Scientific(5,6)

print '%d' % instantiate2.power()

