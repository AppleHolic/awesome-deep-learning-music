# -*- coding: utf-8 -*-
#!/usr/bin/python
#
# Authors   Yann Bayle
# E-mails   bayle.yann@live.fr
# License   MIT
# Created   16/08/2017
# Updated   16/08/2017
# Version   1.0.0
#

"""
Description of dl4m.py
======================

Parse dl4m.csv to create a simple and readable ReadMe.md table.

"""

import os
import sys


def main(filen="dl4m.tsv"):
    """Description of main
    Parse dl4m.csv to create a simple and readable ReadMe.md table.
    """
    if not os.path.isfile(filen):
        print("Invalid input file name provided")
        sys.exit()
    articles = ""
    with open(filen, "r", encoding="utf-8") as filep:
        # Skip csv header
        next(filep)
        for line in filep:
            row = line.split("\t")
            articles += "| [" + row[0] + "](" + row[4] + ") | "
            if len(row[5]) > 1:
                if "No" in row[5]:
                    articles += "No "
                else:
                    if "github" in row[5]:
                        articles += "[GitHub"
                    else:
                        articles += "[Website"
                    articles += "](" + row[4] + ") "
            articles += "|\n"
    with open("paste_in_ReadMe.md", "w") as filep:
        filep.write(articles)


if __name__ == "__main__":
    main()