strs = ['aa', 'BB', 'zz', 'CC']
print (sorted(strs) ) ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print (sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']

## **Custom Sorting With key=**

## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).

def MyFn(s):
  return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print (sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']

## **sort() method**
alist.sort()            ## correct
alist = blist.sort()    ## NO incorrect, sort() returns None

## Tuples

tuple = (1, 2, 'hi')
print (len(tuple))  ## 3
print (tuple[2])    ## hi
tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works

## List Comprehensions (optional)
  ## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]
## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
## ['APPLE', 'BANANA']