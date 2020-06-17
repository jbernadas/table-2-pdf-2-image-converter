# This is a HTML to PDF converter that converts all the files inside htmlResults directory into PDF.
# The results of the conversion is placed inside the pdfResults directory.
# Uses the following dependencies: os, pdfkit, pdfcrowd, wkhtmltopdf
# (the first 3 installed with pip, last one, wkhtmltopdf, is downloaded and added to path environment)

import os
import pdfkit
import pdfcrowd

# Our target directory
inputDir = "./htmlResults"

# Increment variable (must use 1000 or else not sorting properly)
i = 1000

# Loops through target directory
for filename in os.listdir(inputDir):
    # looks for files that end with .html
    if filename.endswith(".html"):
        # use pdfkit to output the PDF files to pdfResults dir
        pdfkit.from_file(os.path.join(inputDir, filename),
                         "./pdfResults/table{}.pdf".format(i))
        # increment by one
        i += 1
        # go on
        continue
    else:
        continue
