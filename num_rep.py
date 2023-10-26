def convert_decimal_to_base(n_10, base):
    if base > 36:
        return 'Base larger than 36, running out of alphabet'
        
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    digits = [i if i < 10 else alphabet[i-10] for i in range(base)]
    remainders = []

    while n_10 > 0:
        remainders.insert(0, digits[n_10 % base])
        n_10 //= base

    return ''.join(str(i) for i in remainders)

test_values = [1157,5226,12166,12649]
for x in test_values:
    rep = convert_decimal_to_base(x,23)
    print(f'({rep})_23 = ({x})_10')