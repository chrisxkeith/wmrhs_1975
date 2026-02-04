import csv
import datetime
import sys
import re

def log(message):
    script_name = sys.argv[0]
    print(str(datetime.datetime.now()) + '\t'+ script_name + ': ' + message)

class Extractor:

    classmates = []
   
    def addClassmate(self, lines):
        classmate = {}
        classmate["name"] = lines[0]
        for line in lines[1:]:
            if re.match(r'^\S+@\S+\.\S+$', line):
                classmate["email"] = line
            elif re.match(r'^\+?\d[\d -]{7,}\d$', line):
                classmate["phone"] = line
            else:
                if not classmate.get("info"):
                    classmate["info"] = line
                else:
                    classmate["info"] += " " + line
        self.classmates.append(classmate)

    def writeCSV(self):
        fn = "./classmates.csv"
        with open(fn, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'email', 'phone', 'info']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for classmate in self.classmates:
                writer.writerow(classmate)
        log(f"Wrote {len(self.classmates)} classmates to {fn}")

    def main(self):
        fn = "./classmates.txt"
        with open(fn, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        log(f"Read {len(lines)} lines from {fn}")
        cmLines = []
        for line in lines:
            line = line.strip()
            if line:
                if line[0] == '#':
                    self.addClassmate(cmLines)
                    cmLines = []
                else:
                    cmLines.append(line)
        log(f"classmates found: {len(self.classmates)}")
        self.writeCSV()

if '__main__' == __name__:
    Extractor().main()
