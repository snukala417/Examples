#!
import argparse

parser = argparse.ArgumentParser(description='Demo')
parser.add_argument('a', help="enter integer a", type=int )
parser.add_argument('-i', help="enter integer i", type=int )

#parser.add_argument('-j', '--abc', type=int )

args = parser.parse_args()
print args.i
print args.a