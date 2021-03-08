import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--aa",type=int,default=0)

args = parser.parse_args()

print(args.aa^10)