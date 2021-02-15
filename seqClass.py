#!/usr/bin/env python
## just trying to see if new comments are visible in GitHub

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()


args.seq = args.seq.upper()                 # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not re.search('U',args.seq): ## to be sure there are not errors
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not re.search('T',args.seq): ## same as before
        print ('The sequence is RNA')
    elif re.search('T',args.seq) and re.search('U',args.seq):
    	print ('There may be an error in the sequence')
    else:
	print('The sequence can be either DNA or RNA')  ##we do not find T nor U bases along the sequence to be able to  distinguish between DNA or RNA
else:
    print('The sequence is neither DNA nor RNA') ##because none of the bases A,G,C,T,U are found

if args.motif:
  args.motif = args.motif.upper()
  print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
  if re.match(args.motif, args.seq):
    print("FOUND, YESSSS, PERFECT!")
  else:
    print("NOT FOUND, KEEP TRYING")
