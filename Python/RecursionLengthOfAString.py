def length(txt):
	if txt == "":
		return 0
	else:
		return 1 + length(txt[1:])