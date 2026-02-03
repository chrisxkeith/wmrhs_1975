import csv
import datetime
import sys
import re

def log(message):
    script_name = sys.argv[0]
    print(str(datetime.datetime.now()) + '\t'+ script_name + ': ' + message)

class Extractor:
   
   def main(self):
        fn = "./classmates.txt"
        with open(fn, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        log(f"Read {len(lines)} lines from {fn}")
        i = 0
        skipCount = 0
        lines2 = []
        for line in lines:
            if (i % 2) == 0:
                lines2.append(line)
            else:
                if line.strip() != "":
                    log(f"Skipping line: {i}:{line.strip()}")
                    skipCount += 1
            i += 1
        log(f"Filtered to {len(lines2)} lines, skipped {skipCount} lines")

if '__main__' == __name__:
    Extractor().main()
