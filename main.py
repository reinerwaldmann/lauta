__author__ = 'vasilev_is'




def reqcc (req):
    for key, val in req.items():
        if val>0:
            return 1
    return 0

def ifexceeds (req, brdlen):
    for key, val in req.items():
        if key>brdlen:
            return 1
    return 0

def determine (required, boardLength):
    #цикл
    res=list()
    while reqcc (required):
        currentBoard={"parts":list(), "len":boardLength, "left":0}
        #список распила, длина, остаток
        while currentBoard["len"]:
            requiredkeys = sorted(list(required.keys()), key=int, reverse=True)

            for key in requiredkeys: #проходим по ключам, начиная с максимального
                while currentBoard["len"]>=key and required[key]>0: #если остаток больше ключа
                        currentBoard["len"]=currentBoard["len"]-key
                        required[key]=required[key]-1
                        currentBoard["parts"].append(key)


        res.append(currentBoard)
    return res



#входные данные
required = {2:4, 1.5:8, 0.5: 8}
boardLength=6


if ifexceeds(required, boardLength):
    print ("Один из размеров в списке запроса превышает размер доски")
    exit(0)


for v in determine(required, boardLength):
    print (v, "\n")





