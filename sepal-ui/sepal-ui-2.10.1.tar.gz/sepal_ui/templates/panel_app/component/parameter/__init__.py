# if you only have few widgets, a module is not necessary and you can simply use a parameter.py file
# in a big module with lot of custom parameter, it can make sense to split things in separate files for the sake of maintenance

# if you use a module import all the functions here to only have 1 call to make
from .directory import *
