from model.model import Model
from view.view import View

class Controller:
    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contracto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, direccion):
        b, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, direccion)
        if b:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e, c = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        
        if e:
            self.view.actualizar_contacto(c)
        else:
            self.view.contacto_no_existen(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
            

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contacto_letra(letra)
        self.view.mostrar_contactos(c)



    #Cita controllers
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        b, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if b:
            self.view.crear_cita(c)
        else:
            self.view.cita_ya_existe(c)
        
    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)
    
    def leer_todas_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)
    
    def actualizar_cita(self, id_cita, id_contacto = '', lugar = '', fecha = '', hora = '', asunto = ''):
        e = self.model.actualizar_cita(self, id_cita, n_id_contacto, n_lugar, n_fecha, n_hora, n_asunto)
        
        if e:
            self.view.modificar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)


############### Ejte ... yo tengo... otros ... datos #############3
    def insertar_contactos(self):
        self.agregar_contacto(1, 'Juan Perez', '464-123-1234', 'jp@gmail.com', 'Arteaga No. 5, San Miguel, Salamanca')
        self.agregar_contacto(2, 'Amanda Leon', '464-987-1234', 'al@gmail.com', 'Villapaldo No.9 Paraiso, Celaya')
        self.agregar_contacto(3, 'Jessica Mendoza', '461-912-1234', 'jm@gmail.com', 'Girasol No.12 Manzanos, Guanajuato')

    def insertar_citas(self): 
        pass

    def start(self):
        #Display a welcome message
        self.view.start()
        self.menu()
        self.view.end()
        #Insert data in mdoel
        #self.insertar_contactos()
        #self.insertar_citas()
        # Show all contacts in DB
        #self.leer_todos_contactos()
        #self.leer_contactos_letra('a')


    def menu(self):
        #Display menu
        self.view.menu()
        o = input('Seleciona una opcion (1-9): ')
        if o == '1':
            self.insertar_contactos()
            self.return_menu()
            

        elif o == '2':
            self.leer_todos_contactos()
            self.return_menu()

        elif o == '3':
            self.actualizar_contacto(3, 'Jessica Mendoza', '461-912-1234', 'lachola@gmail.com', 'Girasol No.12 Arboleada Guanajuato')
            self.return_menu()

        elif o == '9':
            self.view.end()
        
        else:
            self.view.opcion_no_valida()

    def return_menu(self):
        inp = input('Deseas elegir otra opción? \ns: Si \nn: No \n')
        
        if inp == 's':
            self.menu()
        elif inp == 'n': 
            pass