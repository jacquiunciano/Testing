import urllib.request
import re

stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/emails.php')

for line in stream:
	decode = line.decode('UTF-8').strip()

	email = r'(([a-zA-Z\S0-9]*.)@([a-zA-Z\S]*.))'
	email_finder = re.compile(email)

	for match in email_finder.finditer(decode):
		print(match.group(0))
