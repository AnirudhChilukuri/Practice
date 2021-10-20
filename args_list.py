import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--para1", type=int, nargs='+')
args = vars(parser.parse_args())

print(sum(args['para1']))