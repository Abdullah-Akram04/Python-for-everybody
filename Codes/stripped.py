text = "X-DSPAM-Confidence:    0.8475"
apos = text.find(":")
piece = text[apos + 1:]

stripped = piece.strip()
flt = float(stripped)
print(flt)
