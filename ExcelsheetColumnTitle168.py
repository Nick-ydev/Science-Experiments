
alphabet_dict = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",
                 9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",
                 17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",0:"Z",}

columnNumber = 52
col_name = ""

while columnNumber != 0:
     
    remainder = columnNumber % 26
    col_name = alphabet_dict[remainder] + col_name
    columnNumber = columnNumber // 26
    print(col_name,"1")
    if remainder == 0:
        col_name = col_name + "Z"

print(col_name)