## FOR and IN 

## Range

## print the numbers from 0 through 99
for i in range(100):
    print(i)

## While Loop

  ## Access every 3rd element in a list
i = 0
while i < len(a):
    print (a[i])
    i = i + 3

## List Methods
list.append(elem) ## 
list.insert(index, elem) ## 
list.extend(list2) ## 
list.index(elem) ##
list.remove(elem) ##
list.sort() ##
list.reverse() ##
list.pop(index) ##

list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print (list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print (list.index('curly') )   ## 2
list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print (list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']


## List Build Up
list = []          ## Start as the empty list
list.append('a')   ## Use append() to add elements
list.append('b')

## List Slices
list = ['a', 'b', 'c', 'd']
print (list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print (list)         ## ['z', 'c', 'd']