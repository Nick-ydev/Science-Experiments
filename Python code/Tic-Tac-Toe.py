import pprint  

theboard = {
"top-L":" ","top-M":" ","top-R":" ",
"mid-L":" ","mid-M":" ","mid-R":" ",
"low-L":" ","low-M":" ","low-R":" ",
}

print(theboard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

string_in = "My name is Anthony Gonsalves"

for i in range(len(string_in)):
    chunk = string_in[i:i+4]
    print(chunk)

'''
turn = 'X'
for i in range (9):
    printBoard(theboard)
    print("Turn for" + turn + "Where do you wanna play?")
    position = input()
    theboard[position] = turn
    if turn == "X":
        turn = "O"
    else: turn = "X"
'''