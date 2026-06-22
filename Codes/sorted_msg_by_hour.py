fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

counts = dict()

for line in fh:
    if not line.startswith("From "):
        continue

    words = line.split()
    time = words[5]          # e.g. 09:14:16
    hour = time.split(':')[0]  # extract "09"

    counts[hour] = counts.get(hour, 0) + 1

# sort by hour
for k, v in sorted(counts.items()):
    print(k, v)