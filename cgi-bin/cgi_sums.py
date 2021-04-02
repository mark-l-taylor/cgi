#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
listval = map(int, form.getlist('operand'))

print("Content-type: text/plain")
print()
print(sum(listval))
