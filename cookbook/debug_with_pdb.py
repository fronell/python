"""
Reference: https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

Commands:

Help: h
Print variable: p variable
Pretty print variable: pp variable
Show line in code: l
Next statement: n
Step into function: s
Goto end of current function: r
Continue to end or next set_trace: c
Set breakpoint on line number: b line_num
Set breakpoint on line number in file: b file:lin_num i.e. fib.py:4
Set breakpoint on function: b function i.e. add
Set breakpoint on function in module: b module:function i.e. main:add
Set breakpoint on condition (break when high > 10): b break fib.py:4, high > 10
Set variable that is a pdb command: !variable i.e. !b = 'test'
Quit: q
"""

import pdb

def add(num1=0, num2=0):
    return int(num1) + int(num2)

def sub(num1=0, num2=0):
    return int(num1) - int(num2)

def main():
    arg1 = 5
    arg2 = 8
    pdb.set_trace() # <-- Break point added here
    addition = add(arg1, arg2)
    print addition
    subtraction = sub(arg1, arg2)
    pdb.set_trace()
    print subtraction

if __name__ == '__main__':
    main()
