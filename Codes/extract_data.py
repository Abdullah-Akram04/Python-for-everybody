import re

fname = input("Enter file name: ")
fh = open(fname)

total = 0

for line in fh:
    nums = re.findall('[0-9]+', line)
    for n in nums:
        total = total + int(n)

print(total)