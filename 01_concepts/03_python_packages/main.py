# from mypackage import module1

# from mypackage.module2 import Module2

# module1.greet()  # here we are directly calling the greet from module
# Module2.greet("aman")  # here we are calling greet from module2


# import mypackage.module1  # we cannot do this

from mypackage import *

module1.greet()


# module2 is still accessible

from mypackage import module2

module2.Module2().greet("Aman singh")
