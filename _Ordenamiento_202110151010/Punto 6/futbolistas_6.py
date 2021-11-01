futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),  
(14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), 
(6, "Iniesta"), (7, "Villa")]
# seccion a)
futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print(futbolistasTup)

#seccion c)
a = [4,7,11,4,9,5,11,7,3,5]
a.sort()
print(a)
b = [47,3,21,32.56,92]
b.sort()
print(b)
c = [8,43,17,6,40,16,18,97,11,7]
c.sort()
print(c)

#seccion d)
inventosTup = [(40,'Apple Airpods Pro'),(29,'Theranica Nerivio'),(70, 'Roli Lumi'),(95, 'Oculus Quest'),
(99,'Osso VR'),(55,'Bose Frames'),(80,'Eight Sleep Pod')]
inventosTup.sort(key=lambda inventos: inventos[0])
print(inventosTup)

