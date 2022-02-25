f = open('test1.txt', 'w')
lines = ['Line1', 'Line2', 'Line3']
content = '\n'.join(lines)
f.write(content)
f.close()
f = open('test1.txt','r')
print(f.read())
f.close()