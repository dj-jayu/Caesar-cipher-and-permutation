def caesar_encription(s, key=0, dec=False):
    alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
    words = s.lower().split(' ')
    new_text = []
    for word in words:
        new_str = []
        for letter in word:
            if letter in (',','.'):
                new_str.append(letter)
                continue
            if dec:
                new_letter = alphabet[(ord(letter) - ord('a') + (ord('z')-ord('a')+1 - key))%(ord('z')-ord('a')+1)]
                new_str.append(new_letter)
                
            else:
                new_letter = alphabet[(ord(letter) - ord('a') + key)%(ord('z')-ord('a')+1)]
                new_str.append(new_letter)
        new_text.append(''.join(new_str))  
    return ' '.join(new_text)

result = caesar_encription('If you can meet with triumph and disaster, and treat those two impostors just the same.',key=7)

#result = caesar_encription('a',key=1)
#print(f'caesar encription {result}')

result = caesar_encription('Lt wdas iwtht igjiwh id qt htau-tkxstci, iwpi paa btc pgt rgtpits tfjpa, iwpi iwtn pgt tcsdlts qn iwtxg Rgtpidg lxiw rtgipxc jcpaxtcpqat Gxvwih, iwpi pbdcv iwtht pgt Axut, Axqtgin pcs iwt ejghjxi du Wpeexcthh.', key=15, dec=True)
#result = caesar_encription('b', key=1, dec=True)

#print(f'caesar decription: {result}')

def permut(s, l, rule, dec=False):
    if dec:
        rule = invert_rule(rule)
    final_text = []
    for i in range(0, len(s), l):
        block = s[i:i+l]
        block = rearrange(block, l, rule)
        final_text.append(block)
    return ''.join(final_text)

def rearrange(block, l, rule):
    final_block = []
    for number in rule:
        final_block.append(block[number-1])
    return ''.join(final_block)

def invert_rule(permutation):
    inverse = [0] * len(permutation)
    
    for i, x in enumerate(permutation):
        inverse[x - 1] = i + 1
    
    return inverse

result = permut('Dulce et decorum est pro patria mori', 6, (5,4,6,1,3,2))
print(f'permuted:{result}')

result = permut('Iofy un awt  otste ehret ueem aesru ao f ,mna cwtahw oh th erseta  hsiirnefi,osr  ntohei sqsula', 5, (1,3,5,4,2), dec=False)
print(result)

print(permut(permut('abcde', 5, (3,2,5,1,4), dec=True), 5, (3,2,5,1,4)))
