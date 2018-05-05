def add(num1=0, num2=0):
    return int(num1) + int(num2)

def sub(num1=0, num2=0):
    return int(num1) - int(num2)

def main():
    arg1 = 5
    arg2 = 8
    # Reference: https://gist.github.com/obfusk/208597ccc64bf9b436ed
    # Doc: https://www.digitalocean.com/community/tutorials/how-to-debug-python-with-an-interactive-console
    # Ctrl-Z to continue on Windows
    # Ctrl-d to continue on Windows
    import code; code.interact(local=dict(globals(), **locals()))
    addition = add(arg1, arg2)
    print addition
    subtraction = sub(arg1, arg2)
    import code; code.interact(local=dict(globals(), **locals()))
    print subtraction

if __name__ == '__main__':
    main()
