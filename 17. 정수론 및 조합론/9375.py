for _ in range(int(input())):
    cloth = {}

    for _ in range(int(input())):
        clname , cltype = map(str,input().split())

        if cltype in cloth.keys():
            cloth[cltype] +=1
        else:
            cloth[cltype] = 1
    
    ans  =1
    for k in cloth.values():
        ans *=(int(k)+1)
    
    print(ans -1)


    