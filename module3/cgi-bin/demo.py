#!/usr/bin/env python

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<body>"
print "<h1>It works!</h1>"
print "<p>The web server software is running but no content has been added, yet.</p>"
for i in  range(5):
	print "<p>Hello there from python</p>"
print "</body></html>"
