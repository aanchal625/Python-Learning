def n():
    name=input("Enter :")
    print("hello", name)
n()

#if a file is used as a module so we differentiate
#between main and function
if __name__== "__main__":
    n()