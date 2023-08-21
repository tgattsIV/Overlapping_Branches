#Import modules
import os
import re
import sys
import glob
import time
import subprocess
import argparse
import pandas as pd
import numpy as np

working_dir = sys.path[0]+'/'
os.chdir(working_dir)

#Set up an argumanet parser
parser = argparse.ArgumentParser(description='Network step')

parser.add_argument('-f', '--FilePath', type=str, metavar='', required=True, help='Filepath to the unfiltered ERC results')

filePath = args.FilePath

csvData = pd.read_csv('filePath', delimiter='\t')

OBranchAverage = sum(csvData['Overlapping_branches'])/len(csvData['Overlapping_branches'])

print(str(OBranchAverage) + ' average overlapping branches.')
