import re

file1 = open('d:\_projects\_important_documents\_Certificates\HPEFY21.p12', 'r')
strings = re.findall(r'\0', file1.read())
file1.close()
file2 = open('d:\_projects\_important_documents\_Certificates\check.txt', 'w+')
for item in strings:
    line_to_write = re.match(item, file2.read())
    if line_to_write == None:
        file2.write(item)
        file2.write('\n')
    else:
        pass
