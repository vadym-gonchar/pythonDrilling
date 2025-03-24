# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # These lines were inside the if-continue block, which meant they never executed
    ind = line.find(':')
    # Convert the extracted number to float after stripping whitespace
    s = float(line[ind+1:].strip())
    # Was adding total to total instead of s
    total = total + s
    count = count + 1

# This print was incorrectly indented inside the loop
# Also added string formatting to make it cleaner
print(f'Average spam confidence: {total/count}')