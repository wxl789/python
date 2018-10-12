def ChaRuPaiXu(list):
    n = len(list)
    for i in range(1,n):
        for j  in range(i,0,-1):
            if list[j] < list[j-1]:
                list[j-1],list[j] = list[j],list[j-1]
    print(list)

list1 = [1,5,4,2,0,9]
ChaRuPaiXu(list1)

