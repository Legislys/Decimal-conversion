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


"""
Szanowny Panie doktorze, 

jestem studentem I roku Matematyki stosowanej grupy 3. Uzgodniliśmy, że nie muszę uczestniczyć w laboratoriach. Nie jestem w stanie zapisać się już dziś do projektu, wyświetla się komunikat, że nie należę do grupy lab. czwartek, co uniemożliwia mi przesłanie zadanie przez platformę Wikamp. Dlatego załączam link do githuba z rozwiązaniami: https://github.com/Legislys/Decimal-conversion

 Z poważaniem,
Aleksander Węsierski
"""
