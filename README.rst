======
rstpdf
======

About
=====

rstpdf is a small wrapper around rst2latex. It copies the rst file to be
converted as well as the included figures to a temporary directory and calls
rst2latex and pdflatex there. Also, the script makes a few changes to the
documents layout (KOMA-Script is used).

Usage
=====

Call the script in a shell::

  ./rstpdf.py file.rst

Options:

 - ``-s 10``: Use a 10 point font.
