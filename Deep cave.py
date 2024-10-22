import re

tunnel_wall = 30
tunnel_length = 100
space = "||1       1||"

# for i in range (tunnel):
#     print(space.rjust(i,"#"))
#     print(space.ljust(tunnel-1,"#"))


def tunnel_row_maker(tunnel_width,upper_bound,lower_bound):
    for i in range(tunnel_width):
        if lower_bound < i and upper_bound > i: # lower_bound < i < upper_bound
            print(" ",end="")
        else:
            print("#",end="")
    
    print()

def tunnel_maker(tunnel_length,tunnel_wall,upper_bound=15,lower_bound=10):
    flag = True
    for i in range (tunnel_length):
        tunnel_row_maker(tunnel_wall,upper_bound,lower_bound)

        if  upper_bound < tunnel_wall -1 and flag:
            upper_bound +=1
            lower_bound +=1
        elif upper_bound == tunnel_wall-1:
            flag = not flag
            upper_bound -=1
            lower_bound -=1
        elif lower_bound > 0 and not flag:
            upper_bound -=1
            lower_bound -=1
        elif lower_bound == 0:
            flag = not flag
            upper_bound +=1
            lower_bound +=1

tunnel_maker(tunnel_length,tunnel_wall,20,5)
        
