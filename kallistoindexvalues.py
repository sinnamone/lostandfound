from Bio import SeqIO
import numpy as np
import optparse
import traceback
import sys

parser = optparse.OptionParser(usage='python kallistoindexvalues.py -f <(cat *.fastq)', version='1.0',
                               description="Estimated average and standard deviation of fragment length")
parser.add_option('-f', action="store", dest="input",
                  help='input concatenated fastq')
options, args = parser.parse_args()


def kallistoindexvalues(fastaconcatenate):
    try:
        a = []
        for seq_record in SeqIO.parse(fastaconcatenate, "fastq"):
            a.append((len(seq_record)))
    except traceback:
        sys.exit(1)
    else:
        return np.mean(a), np.std(a)


if __name__ == '__main__':
    print(kallistoindexvalues(options.input))
