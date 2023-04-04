""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import toolkit_config as cfg
import pandas as pd

SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')


