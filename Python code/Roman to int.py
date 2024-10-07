
# value_I = 1
# value_V = 5
# value_X = 10
# value_L = 50
# value_C = 100
# value_D = 500
# value_M = 1000
r = "MCMXVI"
length_r = len(r)
integer_r = 0

thisdict = {
  "I": 1,
  "V": 5,
  "X": 10,
  "L": 50,
  "C": 100,
  "D": 500,
  "M": 1000
}
#project abandoned midway due to manual labour
for i in range (0,length_r):
    if r[i] == "I" and (i+1)< length_r and r[i+1] == "V":
        integer_r = integer_r + (thisdict["V"] - thisdict["I"])
    elif r[i] == "I" and (i+1)< length_r and r[i+1] == "X":
        integer_r = thisdict["X"] - thisdict["I"]
    elif r[i] == "I":
        integer_r = integer_r + thisdict["I"]
    elif r[i] == "X" and (i+1)< length_r and r[i+1] == "L":
        integer_r = thisdict["L"] - thisdict["X"]
    elif r[i] == "X" and (i+1)< length_r and r[i+1] == "C":
        integer_r = thisdict["C"] - thisdict["X"]
    elif r[i] == "X":
        integer_r = integer_r + thisdict["X"]
    elif r[i] == "C" and (i+1)< length_r and r[i+1] == "D":
        integer_r = thisdict["D"] - thisdict["C"]
    elif r[i] == "C" and (i+1)< length_r and r[i+1] == "M":
        integer_r = thisdict["M"] - thisdict["C"]
        if (i+1) < length_r:
            if r[i] == "C":
                integer_r = integer_r + thisdict["C"]
            elif r[i] == "M":
                integer_r = integer_r + thisdict["M"]
            elif r[i] == "V" :
                integer_r = integer_r + thisdict["V"]
            elif r[i] == "L" :
                integer_r = integer_r + thisdict["L"]
            elif r[i] == "D" :
                integer_r = integer_r + thisdict["D"]

print(integer_r)
