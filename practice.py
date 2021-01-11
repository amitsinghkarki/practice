#scipy
import scipy
print('scipy:{}'.format(scipy.__version__))

#numpy
import numpy
print('numpy:{}'.format(numpy.__version__))

#lists

mylist=[1,2,3]
print("zeorth VALUE:{0}".format(mylist[0]))
mylist.append(4)
print("list lenght:{0}".format(len(mylist)))
for value in mylist:
    print (value)

#dictionary
mydict={
     'a': 1,
     'b': 2,
     'c': 3,
     'd': 4 
     }
print("A value:{0}".format(mydict['a']))   
mydict['a']=15
print("A value:{0}".format(mydict['a']))   
print("Keys:{0}".format(mydict.keys()))
print("values:{0}".format(mydict.values()))
for key in mydict.keys():
    print (mydict[key])
    
