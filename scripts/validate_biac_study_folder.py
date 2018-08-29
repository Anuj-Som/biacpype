import sys, os
import logging
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../"))
from biacpype.util.validation import verify_biac_path
from biacpype.util.constants import set_paths


STUDY_PATH = "/Volumes/lj146/Documents/CBT.01/"


### validation begins ###
set_paths(STUDY_PATH=STUDY_PATH)
verify_biac_path()
