# Command line calculator with argparse 
import argparse

parser = argparse.ArgumentParser(
    description="Simple Command Line Calculator")

parser.add_argument("num1", type=float, help="First no.")
parser.add_argument("operator",type=str,help="Operator(+, -, *, /)")
parser.add_argument("num2", type=float, help="Second no.")

args = parser.parse_args()

if args.operator == '+':
    result = args.num1 + args.num2
elif args.operator == '-':
    result = args.num1 - args.num2
elif args.operator == '*':
    result = args.num1 * args.num2
elif args.operator == '/':
    if args.num2 == 0:
        result = "Error: Division by zero"
    else:
        result = args.num1 / args.num2
else:
    result = "Error: Invalid operator. Use +, -, *, or /"

print("Result:", result)
