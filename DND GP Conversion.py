import math

copper = 1
Silver = 10
Gold = 100
Plat = 1000
#           C ,S, G, P
Starting_gold = [100,50,3,5]

# print (Starting_gold[0])

total_C = Starting_gold[0]
S_C = Starting_gold[1] * Silver
G_C = Starting_gold[2] * Gold
P_C = Starting_gold[3] * Plat

Conv_Starting_gold = total_C + S_C + G_C + P_C
# print (Conv_Starting_gold)

Usage_gold = [50,10,14,0]

total_used_c = Usage_gold[0]
UsedS_C = Usage_gold[1] * Silver
usedG_C = Usage_gold[2] * Gold
usedP_C = Usage_gold[3] * Plat

Conv_usage_gold = total_used_c + UsedS_C + usedG_C + usedP_C
Final_conv_gold =[0,0,0,0]
# print(Conv_usage_gold)
for i in range(len(Starting_gold)):
    Final_conv_gold[i] = Starting_gold[i] - Usage_gold[i]

print(Final_conv_gold)

for i in range(len(Final_conv_gold)): #(0,4)
    while Final_conv_gold[i] < 0:
        Final_conv_gold[i+1] = Final_conv_gold[i+1] - 1
        print("SAD")
        if Final_conv_gold[i+1] < 0:
            Final_conv_gold[i-1] = Final_conv_gold[i-1] -10
            print(Final_conv_gold)
            


print(2 ** 16)
