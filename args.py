import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a", action="store_true", help="This is the 'a' variable")
parser.add_argument("--b", action="store_const", const=10,
                    help="This is the 'b' variable")

args = parser.parse_args()
a = args.a
b = args.b

print(a)
print(b)