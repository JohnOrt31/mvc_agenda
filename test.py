from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

#c = Contacto(1, 'Jonathan Ortega', '464-651-9093', 'jonny.ort31@gmail.com', 'Clementina Deschamps 132, Salamanca, Gto',)
#d =  Cita(1, 1, 'Parque Bicentenario', '02-02-2020', '18:40', 'Hacer el delicioso')
"""
contactos = []
c = contactos
"""
#c1 = Contacto(1, 'Jonathan Ortega', '464-651-9093', 'jonny.ort31@gmail.com', 'Clementina Deschamps 132, Salamanca, Gto')
#c2 = Contacto(2, 'Diego Rosas', '464-651-9093', 'diego.rosas@gmail.com', 'Clementina Deschamps 132, Salamanca, Gto')

#t1 = Cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase SI')

"""
print(c.id_contacto)
print(c.nombre)
print(c.tel)
print(c.correo)
print(c.direccion)

print(d.id_cita)
print(d.id_contacto)
print(d.lugar)
print(d.fecha)
print(d.hora)
print(d.asunto)
"""

#contactos.append(c1)
#contactos.append(c2)

#guess = input('Ingrese nombre completo: ')
"""
for c in contactos:
    if guess.lower() == c.nombre.lower():
        print('Si está')
        break
else:
    print('No está')

    if (c.nombre == guess):
        print('Si está')
        print(c.nombre)
        print(c.tel)
        print(c.correo)
        print(c.direccion)
        
    elif(c==contactos[-1]):
        print('No está')
        
"""

#m = Model()
#m.agregar_contacto(1, 'Jonathan Ortega', '464-651-9093', 'jonny.ort31@gmail.com', 'Clementina Deschamps 132, Salamanca, Gto')
#m.agregar_contacto(2, 'Diego Rosas', '464-651-9093', 'diego.rosas@gmail.com', 'Clementina Deschamps 132, Salamanca, Gto')

"""
m.actualizar_contacto(2, n_nombre='Iván Rocha')
s = m.leer_todos_contactos()
for c in s:
    print(c.nombre, c.tel)

s = m.leer_contacto_letra('j')
for c in s:
    print(c.nombre, c.tel)

s = m.leer_contacto(1)
print(s.nombre)
s = m.leer_contacto(2)
print(s.nombre)

m.actualizar_contacto(2, 'Jose Vilchis','123-456-7890','mar@gmail.com','Casa Chola, Salamanca, Gto')
s = m.leer_contacto(2)
print(s.nombre)

print('\n')
"""

"""
s = m.borrar_contacto(1)
print(s)
s = m.borrar_contacto(1)
print(s)


s = m.agregar_cita(1, 2, 'Aula 310', '20-02-2020', '14:00', 'Clase SI')

print(s)

cita = m.leer_cita(1)
print(cita.lugar)
print(cita.hora)
print(cita.asunto)
print('\n')

m.actualizar_cita(1, 2, 'Aula 210', '21-02-2020', '14:00', 'Clase DM')
cita = m.leer_cita(1)
print(cita.lugar)
print(cita.hora)
print(cita.asunto)


cita = m.borrar_cita(1)
print(cita)
cita = m.borrar_cita(1)
print(cita)

fecha = input('\nIngresa fecha(DD-MM-YYYY): ')
s = m.buscar_fecha(fecha)
print('\n')
print(s.fecha)
print(s.lugar)
print(s.hora)
print(s.asunto)

"""
"""
m.agregar_cita(1, 2, 'Aula 310', '20-02-2020', '14:00', 'Clase SI')
m.agregar_cita(2, 1, 'Aula 300', '20-02-2020', '14:00', 'Clase DM')
s = m.leer_todas_citas()
for c in s:
    print(c.id_cita, c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
"""
"""
m.borrar_contacto(1)
s = m.leer_todas_citas()
for c in s:
    print(c.id_cita, c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
"""

"""
m.agregar_cita(1, 2, 'Aula 310', '20-02-2020', '14:00', 'Clase SI')
m.agregar_cita(2, 2, 'Aula 110', '2-03-2020', '14:00', 'Clase DM')


v = View()

#Contactos
s = m.leer_todos_contactos()
v.mostrar_contactos(s)

c = m.leer_contacto(1)
v.mostrar_contacto(c)

f,c = m.borrar_contacto(1)
if f:
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)

s = m.leer_todos_contactos()
v.mostrar_contactos(s)

#Citas
s = m.leer_todas_citas()
v.mostrar_citas(s)

c = m.leer_cita(1)
v.mostrar_cita(c)

e, ci = m.borrar_cita(1)
if e:
    v.borrar_cita(ci)
else:
    v.cita_no_existe(1)

s = m.leer_todas_citas()
v.mostrar_citas(s)

"""
cr = Controller()
cr.start()













