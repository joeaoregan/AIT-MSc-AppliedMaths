def HelloWorld():
    print("Hello World")

def main():
    myList = {1,2,3,4,5,6}
    for item in myList:
        print(item)
    HelloWorld()

if __name__ =="__main__":   # Better structure for coding
    main()

# Python does a big chunk of work in a small script
# However, sometimes scripts will be substantial, and
# you are better off defining main
# In a test situation, if asked for main, do it this way
