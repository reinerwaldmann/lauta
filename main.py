__author__ = 'vasilev_is'

import  copy


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


def makeIncPrts(ilst):
    lst=copy.deepcopy(ilst)
    sum=0
    for i in range (0, len (lst)):
        sum+=lst[i]
        lst[i]=sum
    return lst

def determine (required, boardLength):
    #цикл
    res=list()
    while reqcc (required):
        currentBoard={"parts":list(), "len":boardLength, "left":0}
        #список распила, длина, остаток
        requiredkeys = sorted(list(required.keys()), key=int, reverse=True)

        for key in requiredkeys: #проходим по ключам, начиная с максимального
            while currentBoard["len"]>=key and required[key]>0: #если остаток больше ключа
                    currentBoard["len"]=currentBoard["len"]-key
                    required[key]=required[key]-1
                    currentBoard["parts"].append(key)

        currentBoard["left"] = currentBoard["len"]


        currentBoard["sawmap"]=makeIncPrts(currentBoard["parts"])


        currentBoard["left"]=round (currentBoard["left"],2)
        currentBoard["sawmap"] = list (map (lambda x: round (x,2), currentBoard["sawmap"]  ))




        res.append(currentBoard)


    return res




def wrapper (required, boardLength):
    """
    Возвращает карты распила
    :param required: список запроса - таблица длина детали к количеству таких деталей
    :param boardLength: длина материала
    :return: текстовую запись
    """
    if ifexceeds(required, boardLength):
        print ("Один из размеров в списке запроса превышает размер материала")
        exit(0)

    detlist=determine(required, boardLength);


    print ("Количество досок", len (detlist))

    for v in detlist:
        print (v["left"].__str__().rjust(5),"\t"  ,  v["sawmap"].__str__().rjust(5), "\n")





#входные данные
boardLength=6

print ("Ширина 0.3")
required = {2:2*2, 1.5:5*3, 0.3: 5*2}
wrapper (required, boardLength)

print ("Ширина 0.4")
required = {2:2*2, 1.5:5*3, 0.4: 5*2}
wrapper (required, boardLength)

print ("Ширина 0.5")
required = {2:2*2, 1.5:5*3, 0.5: 5*2}
wrapper (required, boardLength)




#print (makeIncPrts([0.5,0.4,0.4,0.4,0.3]  )  )