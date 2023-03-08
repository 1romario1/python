"""Escriba una clase Empleado que tenga como propiedades nombre,cargo,salario, escriba metodos constructores,
setters y getters escriba un metodo que permita calcular cuanto gana el empleado en una hora un metodo para 
saber cuanto recibe de incremento si el salario sube con el IPC.Si gana el minimo se le aumenta el ipc+3%
Un metodo que reciba una cantidad de horas extras y calcule el salario incementando las extras.No puede hacer
mas de dos horas darias y trabaja de lunes a viernes.Valide"""
class Empleado:
    def __init__(self,nombre, cargo, salario,horas):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
        self.horas=horas
    def get_salario(self):
        return self.salario
    def get_nombre(self):
        return self.nombre
    def get_cargo(self):
        return self.cargo
    def get_horas(self):
        return self.horas
    
    def set_salario(self, salario,horas):
        self.salario=salario*horas
        
        
Empleado1=Empleado("juan","gerente de ventas",50000,2)  
print(Empleado1.get_salario())

#no lo eh terminado
