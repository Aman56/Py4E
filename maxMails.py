name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    line=line.rstrip()
    if line.startswith("From") and not line.startswith("From:"):
        words=line.split()
        key=words[1]
        d[key]=d.get(key,0)+1
bigword=None
bigcount=None
for k,v in d.items():
    if bigword is None or v>bigcount:
        bigword=k
        bigcount=v
print(bigword,bigcount)
