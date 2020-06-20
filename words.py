fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for each in words:
        if each not in lst:
            lst.append(each)
lst.sort()
print(lst)
