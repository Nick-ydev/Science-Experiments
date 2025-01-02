
r = "CLIX"
length_r = len(r)
integer_r = 0

roman_dict = {"I":1,"V":5,"X":10,"L": 50,"C": 100,"D": 500,"M": 1000}
print("INput =",r)
for i in range(0, len(r)): #Adds all values as it is and converts to int
    integer_r += roman_dict[r[i]]
    print(integer_r)

#if these outliers exist in r then subtract
if "IV" in r or "IX" in r:
    integer_r -= 2
if "XL" in r or "XM" in r or "XC" in r:
    integer_r -= 20
if "CD" in r or "CM" in r:
    integer_r -= 200

print(integer_r, "Revised")