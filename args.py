import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--a", default=1, type=int, help="This is the 'a' variable")
parser.add_argument("--site",
                    required=True, type=str, help="Enter a site")

args = parser.parse_args()

ed = args.site

print(args.site)