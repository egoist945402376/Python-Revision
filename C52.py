print(ord('A'))
print(chr(66366))

print('ABC'.encode('ascii'))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
a = 3
b = 1
print(f'{a:2d}-{b:02d}')

s1 = 72
s2 = 85

up = (s2 - s1) / s1 * 100
msg = 'The up is '
print(msg + '%.1f' %up)
print(f'{msg}{up:.1f}%')

enc = '中文'.encode('utf-8')
print(enc)
dec = enc.decode('utf-8')
print(dec)
