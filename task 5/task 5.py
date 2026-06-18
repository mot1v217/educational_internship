h, w = list(map(int, input().split(' ')))
string = ''
for _ in range(h):
    string += ''.join(input().split(' '))

first = string.find('1')
last = string.rfind('1')

hfirst = first // h
wfirst = first % h

hlast = last // h
wlast = last % h

print(hfirst - 1, wfirst - 1, hlast + 1, wlast + 1)