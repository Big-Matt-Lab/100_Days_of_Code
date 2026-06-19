# let's see if code completion works

import sys


def out_put(name):
    print(f"Hello, {name}")


def user_name():
    return input("What is your name?: ")



def main():
    name = user_name()
    out_put(name)

    
if __name__=="__main__":
    main()
