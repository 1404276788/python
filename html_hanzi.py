a='中国'
un=ascii(a)
un=un.replace('\'','')
print(str(un))
unlist=un.split('\\')
unlist.remove(unlist[0])
for unstr in unlist:
    unstr='&#x'+unstr+';'
    print(unstr)

