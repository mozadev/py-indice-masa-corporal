
peso_ideal=-1
debajoPesoIdeal=0
sobrepeso=1
class Persona:
    def __init__(self, nombre, edad, dni, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.sexo = sexo
        self.peso = peso
        self.altura = altura


    def calularIMC(self):
        pesoIdeal=self.peso/(self.altura*self.altura)
        if(pesoIdeal<20):
            return peso_ideal
        if (20<=pesoIdeal <= 25):
            return debajoPesoIdeal
        if (pesoIdeal>25):
            return sobrepeso

nombre=input("ingrese el nombre: ")
edad=int(input("ingrese la edad: "))
dni=int(input("ingrese dni: "))
sexo=input("ingrese sexo H hombre, M mujer: ")
peso=float(input("ingrese peso: "))
altura=float(input("ingrese altura: "))


Obj_persona=Persona(nombre,edad,dni,sexo,peso,altura)
resultado=Obj_persona.calularIMC()
print("nombre: "+Obj_persona.nombre+ " edad: "+str(Obj_persona.edad)+
      " dni: "+str(Obj_persona.dni)+" peso: "+str(Obj_persona.peso)+
      " altura:"+str(Obj_persona.altura)+" resultado del diagnostico: "+str(resultado))


