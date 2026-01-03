# import mymodule as md

# classobj = md.BasicAlgebra()  # gives error
# classobj = md.BasicAlgebra    # this is ok (if we are importing module , we just access class it by .(dot))

# print(classobj.power(2, 4))

from mymodule import BasicAlgebra

obj = (
    BasicAlgebra()
)  # if we are importing class from a module we need to give bracket to create obj

print(obj.power(2, 4))
