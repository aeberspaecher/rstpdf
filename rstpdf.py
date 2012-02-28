#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""A small and dirty script to convert reStructuredText to PDF using LaTeX.

Basically, this script only calls rst2latex and pdflatex (which need to be
installed). KOMA-Script document classes are being used.
"""

# TODO: implement "check" option

import os, sys
import subprocess
from optparse import OptionParser
import tempfile

if(__name__ == '__main__'):

    progUsage = "usage: %prog file1 (file2) (file3)"
    parser = OptionParser(usage=progUsage)
    parser.add_option("-s", "--size", action="store", default=12,
                      dest="fontsize", help="Fontsize in points. Defaults to 12.")

    (options, args) = parser.parse_args()

    if(len(args) == 0):
        parser.error("Specify at least one file to convert!")
        sys.exit(1)

    rst2latexOptions = """--latex-preamble="\setcounter{secnumdepth}{3}" --table-style=booktabs --no-section-numbering --documentclass=scrartcl --documentoptions a4paper,%spt """%(options.fontsize)

    devnull = open(os.devnull)

    # - copy source file(s) to temporary directory
    # - call rst2latex
    # - adjust spacing a little
    # - run pdflatex twice
    # - copy result back
    path = tempfile.mkdtemp() + "/"
    #print "Using temp path", path
    for fileName in args:
        errorCode = subprocess.call("cp %s %s"%(fileName, path),
                                    cwd=os.environ["PWD"], shell=True)
        if(errorCode != 0):
            print("Copying rst file to temporary path failed!")
            sys.exit(1)
        texFileName = fileName[:fileName.rfind(".")] + ".tex"
        pdfFileName = fileName[:fileName.rfind(".")] + ".pdf"
        #print "Name of tex file", texFileName, path+texFileName
        print("Try conversion rst => tex.")
        errorCode = subprocess.call("rst2latex %s %s %s"%(rst2latexOptions,
                                          path+fileName, path+texFileName),
                                    cwd=path, shell=True)
        if(errorCode != 0):
            print("Conversion from rst to LaTeX failed!")

        # alter source - use less space. this is for taking notes, not writing books.
        texFile = open("%s%s"%(path, texFileName), mode="r")
        lines = texFile.readlines()
        for i in range(len(lines)):
            if(lines[i].rfind("\\maketitle") > -1):
                lines[i] = ("\\maketitle\n\\vspace{-%sex}\n"
                            %(15.0*float(options.fontsize)/12.0))
        newLines = ""
        newLines = newLines.join(lines)
        texFile.close()
        texFile = open("%s%s"%(path, texFileName), mode="w")
        texFile.write(newLines)
        texFile.close() # close and *write*!

        print("Try conversion tex => PDF.")
        errorCode = subprocess.call("pdflatex %s; pdflatex %s"
                                    %(path+texFileName, path+texFileName),
                                    cwd=path, shell=True)
        # output not supressed, may be helpful in error search

        errorCode = subprocess.call(["cp", path+pdfFileName, os.environ["PWD"]])
        if(errorCode != 0):
            print("Copying PDF file back failed!")
            sys.exit(1)
