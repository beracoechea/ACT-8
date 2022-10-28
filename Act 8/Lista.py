from particulas import Particula
import json

class Lista:

    def __init__ (self):
            self.__Lista = []

    def agregar_final(self, particulas:Particula ):
            self.__Lista.append(particulas)
        
     
    def agregar_inicio(self, particulas:Particula ):
            self.__Lista.insert(0, particulas)
            

    def mostrar(self):
            for particulas in self.__Lista:
                print(particulas)

    def __str__(self):
        return "".join(
           str(particulas) + '\n' for particulas in self.__Lista

        )

    def guardar (self, ubicacion):
        try:

                with open(ubicacion, 'w') as archivo:
                     lista = [particulas.to_dict() for particulas in self.__Lista]
                 
                     json.dump(lista, archivo,indent=11)
                return 1
        except:
                return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                 lista = json.load(archivo)
                 self.__Lista = [Particula(**particulas) for particulas in lista]
            return 1
        except:
           return 0        
    def __len__(self):
        return len(self.__Lista)
          
    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__Lista):
                 Particula = self.__Lista[self.cont]
                 self.cont += 1
                 return Particula
        else :
                raise StopIteration

 

