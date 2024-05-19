def caesar_encription(s, key=0, dec=False):
    new_str = []
    for letter in s:
        if not dec:
            new_str.append(chr(ord(letter)+key))
        else:
            new_str.append(chr(ord(letter)-key))
    return ''.join(new_str)

result = caesar_encription('If you can meet with triumph and disaster, and treat those two impostors just the same.',key=7)

print(f'caesar encription {result}')

result = caesar_encription('Lt wdas iwtht igjiwh id qt htau-tkxstci, iwpi paa btc pgt rgtpits tfjpa, iwpi iwtn pgt tcsdlts qn iwtxg Rgtpidg lxiw rtgipxc jcpaxtcpqat Gxvwih, iwpi pbdcv iwtht pgt Axut, Axqtgin pcs iwt ejghjxi du Wpeexcthh.', k=15, dec=True)

print(f'caesar decription: {result}')


