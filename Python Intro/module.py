#!usr/bin/env python 

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Return the String 's' repeat 3 time 
    If exclaim is true, add exclamation marks
    """

    result = s + s + s 
    if exclaim:
        result = result + '!!!'
    return result


def main():
    print(repeat('Yay', False))
    print(repeat('Woo Hoo', False))

if __name__ == '__main__':
    main()

