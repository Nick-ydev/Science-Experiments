import math

phrase = "Fox on the moon"
len_k = len(phrase)

if phrase[len_k-1] != " ":
    i = len_k -1
    while phrase[len_k-1] != " ": #Code gopes into infinite loop do not run for now

        i +=1
    print(i)
