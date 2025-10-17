## ==========================================================
##  Student Progression Outcome Predictor (Enhanced UI)
##  ----------------------------------------------------------
##  Student ID: 20230351
##  Date: 29/11/2023
##  ----------------------------------------------------------
##  I declare that my work contains no examples of misconduct,
##  such as plagiarism or collusion.
##  Any code taken from other sources is referenced.
## ==========================================================

from graphics import *

# ---------------------- GLOBALS ----------------------
progress_count = 0
trailing_count = 0
retriever_count = 0
excluded_count = 0
credits_data = []

# ---------------------- FILE HANDLING ----------------------
open('progression_data.txt', 'w').close()

def save_to_file(data):
    """Save progression data to file."""
    with open('progression_data.txt', 'a') as f:
        f.write(data + '\n')

