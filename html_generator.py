# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:58:12 2019

@author: Nils
"""

names = ["Lovelace", "Darwin", "Curie", "Hawking"]

output_fh = open("list.html", "w")



scaffold_start = """<!DOCTYPE html>
<html>
<head>
<title>Titel dieser wunderbaren Seite</title>
</head>
<body>

<h1>Eine grossartige Überschrift</h1>

<p>Ein weniger toller Abschnitt.</p>
<ul>
"""

output_fh.write(scaffold_start)

scaffold_middle = ""

for name in names:
    scaffold_middle = scaffold_middle + "<li>" + name + "</li>"

output_fh.write(scaffold_middle)




scaffold_end = """

</ul>

</body>

</html>"""



output_fh.write(scaffold_end)
output_fh.close()