The Big Book of Small Python Projects list

#59 ROCK PAPER SCISSORS
Link: https://inventwithpython.com/bigbookpython/project59.html

First to 5 wins
-	Implement a while loop to track User wins vs Computer wins
-	Break if either reaches 5
For Computer guess, RNG from a list of [Rock, Paper, Scissors]

Truth Table

|User guess |Computer guess| Outcome|
|-----------|--------------|--------|
|R	|P	|Loss
|R	|S	|Win
R	|R	|Tie
P	|S	|Loss
P	|R	|Win
P	|P	|Tie
S	|R	|Loss
S	|P	|Win
S	|S	|Tie

If / elif statements for every outcome and record the outcome as User/Computer Win.

Compressed truth table

|User guess	|Computer guess	|Outcome	Result|
|-----------|---------------|---------------|
R	|R	|Draw,Ties += 1
P	|P		
S	|S		
R	|S	|Win,User wins += 1
P	|R		
S	|P		
For all else	|Loss	|Computer wins += 1

Finally print all outcomes, User wins = X, Comp wins = Y, draws = Z.
