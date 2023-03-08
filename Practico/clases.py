class usuario:
    def __init__(self,id,name,age,contactum,username,password):
        self.id=id
        self.name=name
        self.age=age
        self.contactum=contactum
        self.username=username
        self.password=password 
    def Añadir(self,add,update):
        self.add=add
        self.update=update
        
    
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_contactum(self):
        return self.contactum
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    
    def set_id(self,id):
        self.id=id
    
        
class regitrar(usuario):
    def __init__(self,id,name,age,contactum,username,password):
        usuario().__init__(self,id,name,age,contactum,username,password)
    print("Se registro un usuario.")
Usuario=usuario(119,"jose",18,3104157489,"ose",1234)
print(Usuario.get_id())
