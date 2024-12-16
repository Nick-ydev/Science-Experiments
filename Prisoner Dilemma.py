import random

choices = ["Co-op","Deflect"]

class my_strategy:
    def __init__(self,name,response) -> None:
        self.name = name
        self.response = response
        self.track = []
        self.opponent_response = True
        self.gold = []

    def strat(self, name,opponent_response,i):
        if (name == "Tattoo"):
            if self.track == []:
                self.track.append(opponent_response)
                return True
            else:
                self.track.append(opponent_response)
                return self.track[-1]
        elif (name == "D5"):
            return (i+1)%5 != 0

    def run_strat(self, num_of_iters=50):
        for i in range(num_of_iters):
            self.gold.append(self.strat(self.name,self.opponent_response,i))

    def show_strat_output(self):
        return self.gold



gold = []
Tit4tat = my_strategy("Tattoo",True)
always_false = my_strategy("false", False)
defect_5th = my_strategy("D5",True)

#Tit4tat.run_strat()
defect_5th.run_strat()
#print(Tit4tat.show_strat_output())
print(defect_5th.show_strat_output())

"""
mystrategy 
-> name: strting
-> response: bool
-> track: list
-> strat: function
"""