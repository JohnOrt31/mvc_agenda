from .contacto import Contacto
from .cita import Cita

class Model:
    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    def esta_id_cita(self, id_cita):
        for ci in self.citas:
            if ci.id_cita == id_cita:
                return True, ci
        return False, 0

    #Contacto Methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, direccion):
        e, c = self.esta_id(id_contacto)
        if not e:
            c = Contacto(id_contacto, nombre, tel, correo, direccion)
            self.contactos.append(c)
            return True, c
        return False, c

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)

        if e:
            return c
        return False

    def leer_todos_contactos(self):
        return self.contactos

    def leer_todas_citas(self):
        return self.citas

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e, c = self.esta_id(id_contacto)

        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != '':
                c.correo = n_correo
            if n_dir != '':
                c.direccion = n_dir
            return True, c
        return False, c

    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id(id_contacto)

        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            #ids_temp = [c.id_contacto for c in self.citas]
            #for c in range(len(ids_temp)):
            #for idc in ids_temp:
            for c in lista_temp:
                self.citas.remove(c)
                #if ids_temp[i] == id_contacto:
                    #self.citas.pop(i)
            return True, contacto
        return False
    
    #Cita Methods
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.esta_id_cita(id_cita)[0]:
            if self.esta_id(id_contacto)[0]:
                ci = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                self.citas.append(ci)
                return True
            print('No hay id')
            return False
        return False

    def leer_cita(self, id_cita):
        e, ci = self.esta_id_cita(id_cita)

        if e:
            return ci
        return False

    def actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto):
        e, ci = self.esta_id_cita(id_cita)
    
        if e:
            ci.id_contacto = n_id_contacto
            ci.lugar = n_lugar
            ci.fecha = n_fecha
            ci.hora = n_hora
            ci.asunto = n_asunto
            return True
        return False

    def borrar_cita(self, id_cita):
        e, ci = self.esta_id_cita(id_cita)

        if e:
            self.citas.remove(ci)
            return True
        return False

    def buscar_fecha(self, fecha):
        for fe in self.citas:
            if fe.fecha == fecha:
                return fe
        return False

    def leer_contacto_letra(self, letra):
        #lista = [c for c in self.contactos if  c.nombre.lower().startswith(letra.lower())]
        lista = []
        for c in self.contactos:
            if c.nombre[0].lower() == letra.lower():
            #if c.nombre.lower().startswith(letra):
                lista.append(c)
        return lista
    
    def leer_citas_fechas(self, fecha):
        #lista = [c for c in self.citas if c.fecha.startswith(fecha)]
        lista = []
        for c in self.citas:
            if c.fecha == fecha:
                lista.append(c)
        return lista
