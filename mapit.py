# Search google map. Address is picked from argv or clipboard

import webbrowser, sys, numpy, pandas, pyperclip

if len(sys.argv)>1:
	address=" ".join(sys.argv[1:])
else:
	address=pyperclip.paste()
url="https://www.google.com/maps/place/"+address
webbrowser.open(url)