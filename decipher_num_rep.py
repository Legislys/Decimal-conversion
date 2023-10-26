def convert_base_to_decimal(n,base):
    print(f'({n})_{base} = ({int(str(n), base)})_10')

test_values = ['mak', '5h2i','fghj','a0b0c']
for x in test_values:
    convert_base_to_decimal(x,23)