import sqlite3
fichier="C:/Users/pierre/Desktop/ECAM/Informatique/Base de donnée/exercice1.sq3"
conn=sqlite3.connect(fichier)
cur=conn.cursor()
print("Bonjour bienvenue dans la base de donnée musique")
N=int(input("Combien de compositeurs voulez-vous rentrer : "))
a=0
while a<N :
    C=input("Mettez le nom du compositeur : ")
    B=int(input("Mettez l'année de naissance du compositeur : "))
    print("Si le compositeur n'est pas décédé veuillez mettre 0")
    M=int(input("Mettez l'année de mort du compositeur : "))
    data =[(C,B,M)]
    for tu in data :
        cur.execute("INSERT INTO Compositeurs(comp,a_naiss,a_mort) Values(?,?,?)",tu)
    a=a+1
conn.commit()
conn.close()