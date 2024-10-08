import random

starting_prompts = {"userM1":["Tissues","Money","Bottle",""],
                    "userF2":["Sheep","Flamingo","giraffee","Turkey"],
                    "userM3":["Lamb","Seal","Falcon","Firefly"],
                    "userF4":["jellyfish","Bhains","parrot",""],
                    "userM5":["Cuckatoo","Seagull","Owl",""],
                    "userF6":["Wolf","woodpecker","koyal","Crow"],}

#IDK how to qassgin a userr to a key in a dictionary

prompts_dict = {'chidiya': 'Y', 'bottle': 'N', 'kangaroo': 'N', 'falcon': 'Y', 'bhains': 'N'}

#
'''
for i in range(0,5):
    prompt = input("Enter object name")
    fly_nofly = input("Enter answer")

    prompts_dict[prompt] = fly_nofly
'''
prompts_list = prompts_dict.keys()
print(prompts_list)