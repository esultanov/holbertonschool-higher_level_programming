#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        ops = ['+', '-', '*', '/']
        b = int(sys.argv[3])
        if op in ops:
            if sys.argv[2] == '+':
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            elif sys.argv[2] == '-':
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            elif sys.argv[2] == '*':
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            else:
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
