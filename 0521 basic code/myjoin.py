print('a,b,c'.split(','))

print('this is my string'.split())

s = "this is my string"
print(s.split(maxsplit=1))

print('a' + 'b' + 'c')
print('do' * 2)

strings = ['do', 're', 'mi']
print(','.join(strings))

print('->'.join('string'))

print(''.join(['p', 'y', 't', 'h', 'o', 'n']))
print(', '.join(['foo', 'bar', 'baz', 'qux']))

print(list('corge'))
print(':'.join(list('corge')))
print(':'.join('corge'))

print('---'.join(['foo', str(23), 'bar']))
