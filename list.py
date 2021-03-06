import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
x = [1,23,56,2345,57]
print("Anirudh", args.accumulate(x))
#baby_1 = [0,0,0,0,0]
#baby_2 = [1,2,3,4,5]
#expert = "Million numbers"  