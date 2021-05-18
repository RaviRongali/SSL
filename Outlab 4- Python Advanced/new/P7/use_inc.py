import numpy as np
import sys
from argparse import ArgumentParser
from inc import ang_to_vec, vec_to_ang

parser = ArgumentParser()
parser.add_argument('input_filename')
parser.add_argument('output_filename')
parser.add_argument('a2v', type=int)
args = parser.parse_args()

in_array = np.loadtxt(args.input_filename, delimiter=",")
try:
    out_array = (vec_to_ang if args.a2v else ang_to_vec)(in_array)
except AssertionError:
    sys.exit(1)

np.savetxt(args.output_filename, out_array, delimiter=",")
