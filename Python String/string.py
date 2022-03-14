#code example strings 

s = 'hi'
print(s[1])
print(len(s))
print(s + ' There')

pi = 3.14 #text
text = 'The value of pi is ' + str(pi)

# ***String Methods***
s.lower(), s.upper() ##returns the lowercase or uppercase version of the string
s.strip() ##returns a string with whitespace removed from the start and end
s.isalpha(), s.isdigit(), s.isspace() ## tests if all the string chars are in the various character classes
s.startswith('other'), s.endswith('other') ##  tests if the string starts or ends with the given other string
s.find('other') ## searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
s.replace('old','new') ##  returns a string where all occurrences of 'old' have been replaced by 'new'
s.split('delim') ## returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
s.join(list) ## opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

## ***String Slice***

""" 
                                Hello

s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4
s[1:] is 'ello' -- omitting either index defaults to the start or end of the string
s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)
s[1:100] is 'ello' -- an index that is too big is truncated down to the string length
The standard zero-based index numbers give easy access to chars near the start of the string. As an alternative, Python uses negative numbers to give easy access to the chars at the end of the string: s[-1] is the last char 'o', s[-2] is 'l' the next-to-last char, and so on. Negative index numbers count back from the end of the string:

s[-1] is 'o' -- last char (1st from the end)
s[-4] is 'e' -- 4th from the end
s[:-3] is 'He' -- going up to but not including the last 3 chars.
s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

"""

##  ***String % *** 

"""Python has a printf()-like facility to put together a string. The % operator takes a printf-type format string on the left (%d int, %s string, %f/%g floating point), and the matching values in a tuple on the right (a tuple is made of values separated by commas, typically grouped inside parentheses):"""

text = (
    "%d little pigs come out, "
    "or I'll %s, and I'll %s, "
    "and I'll blow your %s down."
    % (3, 'huff', 'puff', 'house'))


## ***If Statement*** 

