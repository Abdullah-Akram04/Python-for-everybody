fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)

counts = 0

for line in fh:
    if not line.startswith("From "):
        continue

    words = line.split()
    email = words[1]

    counts[email] = counts.get(email, 0) + 1

# find the most prolific sender
big_count = None
big_email = None

for email, count in counts.items():
    if big_count is None or count > big_count:
        big_email = email
        big_count = count

print(big_email, big_count)