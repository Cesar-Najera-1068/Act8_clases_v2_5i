class Informacion:

    def mi_lista(self):
        lista_Nomperros=["Boby","Dollar","Fany"]
        for x in lista_Nomperros:
            print(x)
    
    def mi_tupla(self):
        tupla_razas=("Pastor aleman", "Dalmata", "Husky")
        for r in tupla_razas:
            print(r)

    def mi_set(self):
        set_edades=(4,5,2)
        for e in set_edades:
            print(e)

    def mi_dicc(self):
        diccionario= {
            "Boby": "Edad: 4",
            "Dollar": "Edad: 5",
            "Fany": "Edad: 2"
        }
        for d, y in diccionario.items():
            print(d, y)

#Creando el objeto

datos=Informacion()
print("--------------------")
print("Listado de nombre de perros:")
datos.mi_lista()
print("--------------------")
print("Raza de los perros:")
datos.mi_tupla()
print("--------------------")
print("Edad de los perros:")
datos.mi_set()
print("--------------------")
print("Informacion de los perros:")
datos.mi_dicc()
