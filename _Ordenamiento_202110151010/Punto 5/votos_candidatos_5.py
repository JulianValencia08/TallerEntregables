def candidato_ganador():
    voto = [0,1,2,3,4]
    print("El id del candidato es:")
    for i in range(len(voto) - 1, 0, -1):
        print(voto[i])

candidato_ganador()        
