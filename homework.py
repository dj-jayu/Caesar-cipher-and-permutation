def caesar_encription(s, key=0, dec=False):
    alphabet = 'abcdefghijklmnopqrstuvxwyz'
    new_str = []
    for letter in s.lower().replace(' ', ''):
        if dec:
            new_letter = alphabet[(ord(letter) - ord('a') + (ord('z')-ord('a')+1 - key))%(ord('z')-ord('a')+1)]
            new_str.append(new_letter)
        else:
            new_letter = alphabet[(ord(letter) - ord('a') + key)%(ord('z')-ord('a')+1)]
            new_str.append(new_letter)
    return ''.join(new_str)

result = caesar_encription('If you can meet with triumph and disaster, and treat those two impostors just the same.',key=7)

#result = caesar_encription('a',key=1)
print(f'caesar encription {result}')

result = caesar_encription('Lt wdas iwtht igjiwh id qt htau-tkxstci, iwpi paa btc pgt rgtpits tfjpa, iwpi iwtn pgt tcsdlts qn iwtxg Rgtpidg lxiw rtgipxc jcpaxtcpqat Gxvwih, iwpi pbdcv iwtht pgt Axut, Axqtgin pcs iwt ejghjxi du Wpeexcthh.', key=15, dec=True)
#result = caesar_encription('b', key=1, dec=True)

print(f'caesar decription: {result}')


