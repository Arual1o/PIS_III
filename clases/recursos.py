class recurso:
    def __init__(self,id,tipo_recurso,descripcion,imagen,recurso,link,fecha):
        self.id=id
        self.tipo_recurso=tipo_recurso
        self.descripcion=descripcion
        self.imagen=imagen
        self.recurso=recurso
        self.link=link
        self.fecha=fecha
    
    def id(self):
        return self.id
    
    def tipo_recurso(self):
        return self.tipo_recurso
    
    def descripcion(self):
        return self.descripcion
    
    def imagen (self):
        return self.imagen
    
    def recurso (self):
        return self.recurso
    
    def link (self):
        return self.link
    
    def fecha (self):
        return self.fecha