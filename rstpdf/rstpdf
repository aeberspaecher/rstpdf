#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""A small script to convert reStructuredText to pdf using LaTeX.

Basically, this script only calls rst2latex and pdflatex (which need to be
installed). KOMA-Script document classes are being used.
"""

# TODO: implement "check" option

import os, sys
from optparse import OptionParser
import tempfile

if(__name__ == '__main__'):

    progUsage = "usage: %prog file"
    parser = OptionParser(usage=progUsage)
    parser.add_option("-s", "--size", action="store", default=12,
                      dest="fontsize", help="Fontsize in points. Defaults to 12.")
    
    (options, args) = parser.parse_args()

    rst2latexOptions = """--latex-preamble="\setcounter{secnumdepth}{3}" --table-style=booktabs --no-section-numbering --documentclass=scrartcl --documentoptions a4paper,%spt """%(options.fontsize)

    # - copy source file(s) to temporary directory
    # - call rst2latex
    # - adjust spacing a little
    # - run pdflatex twice
    # - copy result back
    path = tempfile.mkdtemp() + "/"
    print "Using temp path", path
    for fileName in args:
        os.system("cp %s %s"%(fileName, path))
        texFileName = fileName[:fileName.rfind(".")] + ".tex"
        pdfFileName = fileName[:fileName.rfind(".")] + ".pdf"
        print "name of tex file", texFileName, path+texFileName
        os.system("rst2latex %s %s %s"%(rst2latexOptions, path+fileName, path+texFileName))

        # alter source
        texFile = open("%s%s"%(path, texFileName), mode="r")
        lines = texFile.readlines()
        for i in range(len(lines)):
            if(lines[i].rfind("\\maketitle") > -1):
                lines[i] = ("\\maketitle\n\\vspace{-%sex}\n"%(15.0*float(options.fontsize)/12.0))
        newLines = ""
        newLines = newLines.join(lines)
        texFile.close()
        texFile = open("%s%s"%(path, texFileName), mode="w")
        texFile.write(newLines)
        texFile.close() # close and *write*!

        os.system("cd %s; pdflatex %s"%(path, path+texFileName))
        os.system("cd %s; pdflatex %s"%(path, path+texFileName))
        
        os.system("cp %s ."%(path+pdfFileName))

    

