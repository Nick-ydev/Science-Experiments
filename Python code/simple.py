# import math 

# for i in range (1,999):
#     if i % 23 == 0:
#         print (i)
#     if str(23) in str (i):
#         print (i)

# for i in range (1,99):
#     #print (list(str(i)))
#     v = list(map(int,list(str(i))))
#     if sum(v) == 23:
#         print (i)

# v = [x*y for x in range (1,9) for y in range (1,9)]
# print ([x for x in v if x %3 == 0])

Nums = [1,46,32,53,3,32]
Nums_2 = Nums
print(Nums_2)

# for i in range(len(Final_conv_gold)): #(0,4)
    
#         while Final_conv_gold[i] < 0:
#             if i < 3:
#                 Final_conv_gold[i+1] = Final_conv_gold[i+1] -1
#             if (Final_conv_gold[i+1] < 0 ):
#                 print ("Not enough currency")
#             Final_conv_gold[i] = Final_conv_gold[i] + 10
#             if Final_conv_gold[i] < 0:
#                 print ("Not enough currency")
#             if i < 3:
#                 if (Final_conv_gold[i+1] -1) < 0:
#                     if (Final_conv_gold[i-1] -10) < 0:
#                         print ("Not enough currency")
#                     else:
#                         Final_conv_gold[i-1] -10
#                 else:
#                     (Final_conv_gold[i+1] -1)