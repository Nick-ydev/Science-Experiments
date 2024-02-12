
r = "IV"
length_r = len(r)
integer_r = 0

roman_dict = {"I":1,"V":5,"X":10,"L": 50,"C": 100,"D": 500,"M": 1000}
roman_list = ["I","V","X","L","C","D","M"]

position_I= roman_list.index('I')
position_V= roman_list.index('V')
position_X= roman_list.index('X')
position_L= roman_list.index('L')
position_C= roman_list.index('C')
position_D= roman_list.index('D')
position_M= roman_list.index('M')

for i in range(0, len(r)):
    if r[i] in roman_list:
        posi = roman_list.index(r[i])
    integer_r += roman_dict[r[i]]
    #print(integer_r)
    print(posi)
