import sys

args = sys.argv[1:]
if len(args) == 1:
    args = args[0].split()

args[0] = ("0" * (5 - len(args[0]))) + args[0][:-1]

to_remove = []
for i in range(1, len(args)):
    if len(args[i]) == 1 and not args[i].isalnum():
        to_remove.append(i)

for i in reversed(to_remove):
    args.pop(i)

filename = "_".join(args).lower() + ".py"
with open(filename, 'x') as fp:
    pass