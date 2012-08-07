rstpdf
======

About
-----

rstpdf is a small wrapper around rst2latex. It copies the rst file to be
converted as well as the included figures and images to a temporary
directory and calls rst2latex and pdflatex there. Also, the script makes a
few changes to the documents layout (KOMA-Script is used).

Usage
-----

Call the script in a shell::

  ./rstpdf.py file.rst

Options:

 - ``-s 10`` or ``--size=10``: use a 10 point font.
 - ``-l`` or ``--landscape``: use landscape orientation.
 - ``-t`` or ``--two-column``: use a two-column layout.

Known annoyances
----------------

The option  ``--two-colum`` does not work if tables are used due to some
restriction of the LaTeX table environment used by rst2latex.
