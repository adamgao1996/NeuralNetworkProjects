import numpy  as np
import pandas as pd

my_list = [1,2,3]
arr = np.array(my_list)

t = np.arange(0,10,2)
print t

print np.zeros((3,5))
print np.ones((3,5))

print np.linspace(0,11,50)

print np.random.randint(0,10,(3,3))

np.random.seed(101)
arr = np.random.randint(0,100,10)
print arr.max()
print arr.mean()
print arr.argmax()

arr.reshape(2,5)

mat = np.arange(0,100).reshape(10,10)
print mat

print mat[4,9]
print mat[:,0]
print mat[5,:]
print mat[0:3,0:3]
myfilter=mat > 50
print mat[myfilter]

df = pd.read_csv('Tensorflow-Bootcamp-master/00-Crash-Course-Basics/salaries.csv')

print df