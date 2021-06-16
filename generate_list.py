from itertools import product

def work_around_detector(word, sub_dict):
    possibles = []
    for l in word.lower():
        ll = sub_dict.get(l, l)
        possibles.append( (l,) if ll == l else (l, ll) )
    return [ ''.join(t) for t in product(*possibles) ]

leet = {'a': '4', 'b': '8', 'e': '3', 'g': '6', 'i': '1', 'o': '0', 's': '5', 't': '7', 'z': '2'}
blocked_list=work_around_detector('lol',leet)
blocked_list+=work_around_detector('lolz',leet)
blocked_list+=work_around_detector('lel',leet)
blocked_list+=work_around_detector('lul',leet)
blocked_list+=work_around_detector('lulz',leet)
blocked_list+=work_around_detector('rofl',leet)
blocked_list+=work_around_detector('ha',leet)
blocked_list+=work_around_detector('haha',leet)
leet.update({'l': '|'})
blocked_list+=work_around_detector('lol',leet)
blocked_list+=work_around_detector('lolz',leet)
blocked_list+=work_around_detector('lel',leet)
blocked_list+=work_around_detector('lul',leet)
blocked_list+=work_around_detector('lulz',leet)
blocked_list+=work_around_detector('rofl',leet)
blocked_list+=work_around_detector('ha',leet)
blocked_list+=work_around_detector('haha',leet)
leet.update({'l': 'i'})
blocked_list+=work_around_detector('lol',leet)
blocked_list+=work_around_detector('lolz',leet)
blocked_list+=work_around_detector('lel',leet)
blocked_list+=work_around_detector('lul',leet)
blocked_list+=work_around_detector('lulz',leet)
blocked_list+=work_around_detector('rofl',leet)
blocked_list+=work_around_detector('ha',leet)
blocked_list+=work_around_detector('haha',leet)

print(len(blocked_list))
blocked_list = list(dict.fromkeys(blocked_list))
print(len(blocked_list))
print(blocked_list)