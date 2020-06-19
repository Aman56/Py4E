# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total, count=0,0
for line in fh:
    lin = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        pos=line.find('0')
        val=line[pos:]
        total = total+float(val)
        count = count+1
avg = total/count
print('Average spam confidence:',avg)
