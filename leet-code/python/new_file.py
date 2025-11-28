import sys

args = sys.argv[1:]
args[0] = ("0" * (5 - len(args[0]))) + args[0][:-1]

filename = "_".join(args).lower() + ".py"
with open(filename, 'x') as fp:
    pass