prenume=['Mihai','George','Ana','Dan','Ion','Geta','Vio']
virsta=[14,23,15,14,12,41,39]
for n in range(0,len(prenume)):
    print(prenume[n],'virsta de',virsta[n],'ani')
    n+=1
prenume.extend([34,23])
print('Adaugati:(Andreea,Ioan)',prenume)
print('Adaugati:34 23', virsta)
prenume.pop(2)
virsta.pop(2)
print('Serge Ana:',prenume)
print('Sterge virsta lua Ana',virsta)
print('Afisati primele nume:',prenume [0:3])
print('Afisati numele din dreapta si stinga',prenume[::-1])
print('Afisati elementul 2 si 4',prenume[2],prenume[4])
print('Afisati elementul 2 si 4 de la virsta',virsta[2],virsta[4])
print('Afisati de la 0 la 5 elemente de la virsta',virsta[0:5])
print('Afisati elementelede la 0 la 5 de la nume',prenume[0:5])