

def strcoding(source_string):
    un = ascii(source_string)
    un = un.replace('\'','')
    un = un.replace('u','')
    unlist = un.split('\\')
    unlist.remove(unlist[0])
    print(unlist)
    str_l = ''
    for unstr in unlist:
        unstr=unstr.upper()
        unstr ='&#x'+unstr+';'
        str_l = str_l + unstr
    return str_l


print(strcoding('中国代孕'))
