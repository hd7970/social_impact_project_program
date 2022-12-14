import variable_demo as vd
import conditional_demo as cd
import loop_demo as ld
import list_demo as ad


# not needed for video
def variables():
    while True:
        print("1. variable types")
        print("2. type changes")
        print("0. exit")
        user_in = input("please make a selection (0-9) : ")
        if user_in == '1':
            vd.variable_type()
            print("\n")
        elif user_in == '2':
            vd.type_change()
            print("\n")
        elif user_in == '3':
            vd.boolean_var()
            print("\n")
        elif user_in == '0':
            print("\n")
            return
        else:
            print("ERROR::invalid input!")


def conditionals():
    while True:
        print("1. if else statements")
        print("0. exit")
        user_in = input("please make a selection (0-9) : ")
        if user_in == '1':
            cd.elif_conditionals()
            print("\n")
        elif user_in == '0':
            print("\n")
            return
        else:
            print("ERROR::invalid input!")


def loops():
    while True:
        print("1. while loops")
        print("2. for loops")
        print("0. exit")
        user_in = input("please make a selection (0-9) : ")
        if user_in == '1':
            ld.while_loops()
            print("\n")
        elif user_in == '2':
            ld.for_loops()
            print("\n")
        elif user_in == '0':
            print("\n")
            return
        else:
            print("ERROR::invalid input!")


def lists():
    while True:
        print("1. types of lists")
        print("0. exit")
        user_in = input("please make a selection (0-9) : ")
        if user_in == '1':
            ad.lists_arrays()
            print("\n")
        elif user_in == '0':
            print("\n")
            return
        else:
            print("ERROR::invalid input!")


# This does not need to be shown in the video.  This is more so for making sure my code works, and is usable.
def main():
    while True:
        print("1. variable demos")
        print("2. conditional demos")
        print("3. loop demos")
        print("4. list demos")
        print("0. exit")
        user_in = input("please make a selection (0-9) : ")
        if user_in == '1':
            variables()
        elif user_in == '2':
            conditionals()
        if user_in == '3':
            loops()
        if user_in == '4':
            lists()
        elif user_in == '0':
            exit(0)
        else:
            print("ERROR::invalid input!")


# This single function call is what allows the program to run.
main()
