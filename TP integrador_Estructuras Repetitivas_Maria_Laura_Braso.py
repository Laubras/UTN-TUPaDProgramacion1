# Ejercicio 1: “Caja del Kiosco”

while True:

    nombre_cliente = input("Ingrese el nombre del cliente: ")

    if nombre_cliente == "":
        print("Error! Ingreso el campo vacio.")

    elif nombre_cliente.isdigit():
        print("Error! No puede ingresar números para el nombre del cliente.")

    elif not nombre_cliente.isalpha():
        print("Error! El nombre solo puede contener letras.")
    
    else:
        print(f"Nombre ingresado: {nombre_cliente.title()}")
        break

while True:

    cantidad_de_productos_a_comprar = input("Ingrese cantidad de productos del pedido: ")

    if cantidad_de_productos_a_comprar == "":
        print("Error! Ingreso el campo vacio.")

    elif cantidad_de_productos_a_comprar.isalpha():
        print("Error! No puede ingresar letras para la cantidad de productos del pedido.")

    elif not cantidad_de_productos_a_comprar.isdigit():
        print("Error! La cantidad de productos solo puede contener números enteros positivos.")

    elif int(cantidad_de_productos_a_comprar) == 0:
        print("Error! La cantidad de productos debe ser mayor a cero.")

    else:
        cantidad_de_productos_a_comprar = int(cantidad_de_productos_a_comprar)
        print(f"La cantidad de productos ingresados es: {cantidad_de_productos_a_comprar}")
        break  

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1, cantidad_de_productos_a_comprar + 1):

    while True:
        precio_producto = input(f"Ingrese el precio del producto {i}: ")

        if precio_producto == "":
            print("Error! Ingreso el campo vacio.")

        elif not precio_producto.isdigit():
            print("Error! El precio ingresado del producto solo puede contener números enteros positivos.")

        elif int(precio_producto) == 0:
            print("Error! El precio debe ser mayor a cero.")
            
        else:
            precio_producto = int(precio_producto)
            print(f"Precio ingresado para el producto {i}: {precio_producto}")
            break

    total_sin_descuento += precio_producto
    precio_con_descuento = precio_producto

    while True:
        tiene_descuento = input("¿El producto tiene descuento? (S/N): ").upper()
        match tiene_descuento:
            case "S":
                precio_producto = precio_producto - (precio_producto * 0.10)
                print(f"Precio con descuento: {precio_producto:.2f}")
                break
            case "N":
                print(f"Precio sin descuento: {precio_producto:.2f}")
                break
            case _:
                print("Opción incorrecta. Ingrese S o N.")

    total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_de_productos_a_comprar

print(f"\nTotal sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# Ejercicio 2: “Acceso al Campus y Menú Seguro”

import random

usuario_correcto = "alumno"
clave_correcta = "python123"

acceso_concedido = False

for intento in range(1, 4):
    print(f"Intento {intento}/3")
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su contraseña: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso_concedido = True
        break

    elif usuario == usuario_correcto and clave != clave_correcta:
        print("Error: clave incorrecta.")


    elif usuario != usuario_correcto and clave == clave_correcta:
        print("Error: usuario incorrecto.")

    else:
        print("Error: clave y usuario incorrectos.")

if not acceso_concedido:
    print("Cuenta bloqueada.")

if acceso_concedido:
    while True:
        print("""Menú:
1) Estado
2) Cambiar clave
3) Mensaje
4) Salir
        """)

        elija_opcion = input("Ingrese una opción: ")

        if not elija_opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion_elegida = int(elija_opcion)

        if opcion_elegida < 1 or opcion_elegida > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion_elegida == 1:
            print("Estado: Inscripto.")
        elif opcion_elegida == 2:
            intentos_clave = 3
            clave_cambiada = False

            while intentos_clave > 0:
                nueva_clave = input("Ingrese la nueva clave: ")
                confirmar_clave = input("Confirme la nueva clave: ")

                if nueva_clave == confirmar_clave:
                    clave_correcta = nueva_clave
                    print("Clave actualizada con éxito.")
                    clave_cambiada = True
                    break
                else:
                    intentos_clave -= 1
                    print(f"Error: las claves no coinciden. Intentos restantes: {intentos_clave}")
            if not clave_cambiada:
                print("No se pudo cambiar la clave.")
        elif opcion_elegida == 3:
            print('"Carpe Diem" Aprovecha el tiempo.')
        elif opcion_elegida == 4:
            print("Saliendo...")
            break

# Ejercicio 3: (Alta) — “Agenda de Turnos con Nombres (sin listas)”

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre_operador = input("Ingrese su nombre: ")

while not nombre_operador.isalpha():
    print("Error: Ingrese solo letras: ")
    nombre_operador = input("Ingrese su nombre: ")

while True:
    print("""Menú:
    1. Reservar turno
    2. Cancelar turno
    3. Ver agenda del día
    4. Ver resumen general
    5. Cerrar sistema
    """)

    opcion_menu = input("Ingrese una opción: ")

    while not opcion_menu.isdigit() or int(opcion_menu) < 1 or int(opcion_menu) > 5:
        print("Error: Debe ingresar un número entre 1 y 5.")
        opcion_menu = input("Ingrese una opción: ")
    opcion_menu = int(opcion_menu)

    if opcion_menu == 1:
        dia = input("Elija un día: (1) Lunes (2) Martes: ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: debe ingresar un número entre 1 y 2.")
            dia = input("Elija un día: (1) Lunes (2) Martes: ")
        dia = int(dia)

        paciente = input("Ingrese el nombre del paciente: ")
        while not paciente.isalpha():
            print("Debe ingresar solo letras.")
            paciente = input("Ingrese el nombre del paciente: ")

        if dia == 1:
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: ese paciente ya tiene un turno reservado el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado: Lunes - Turno 1 - {paciente}")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno reservado: Lunes - Turno 2 - {paciente}")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno reservado: Lunes - Turno 3 - {paciente}")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno reservado: Lunes - Turno 4 - {paciente}")
            else:
                print("No hay turnos disponibles el lunes.")
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: ese paciente ya tiene un turno reservado el martes.")
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno reservado: Martes - Turno 1 - {paciente}")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno reservado: Martes - Turno 2 - {paciente}")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno reservado: Martes - Turno 3 - {paciente}")
            else:
                print("No hay turnos disponibles el martes.")

    elif opcion_menu == 2:
        cancelar_paciente = input("Ingrese el nombre del paciente a cancelar: ")
        while not cancelar_paciente.isalpha():
            print("Error: debe ingresar solo letras.")
            cancelar_paciente = input("Ingrese el nombre del paciente a cancelar: ")

        if cancelar_paciente == lunes1:
            lunes1 = ""
            print("Turno cancelado: Lunes, turno 1.")
        elif cancelar_paciente == lunes2:
            lunes2 = ""
            print("Turno cancelado: Lunes, turno 2.")
        elif cancelar_paciente == lunes3:
            lunes3 = ""
            print("Turno cancelado: Lunes, turno 3.")
        elif cancelar_paciente == lunes4:
            lunes4 = ""
            print("Turno cancelado: Lunes, turno 4.")
        elif cancelar_paciente == martes1:
            martes1 = ""
            print("Turno cancelado: Martes, turno 1.")
        elif cancelar_paciente == martes2:
            martes2 = ""
            print("Turno cancelado: Martes, turno 2.")
        elif cancelar_paciente == martes3:
            martes3 = ""
            print("Turno cancelado: Martes, turno 3.")
        else:
            print("No se encontró un turno con ese nombre.")

    elif opcion_menu == 3:
        dia = input("Elija el día (1=Lunes, 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: Debe ingresar 1 o 2.")
            dia = input("Elija el día (1=Lunes, 2=Martes): ")

        dia = int(dia)

        if dia == 1:
            print("Agenda del Lunes:")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", lunes1)

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", lunes2)

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", lunes3)

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print("Turno 4:", lunes4)

        elif dia == 2:
            print("Agenda del Martes:")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print("Turno 1:", martes1)

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print("Turno 2:", martes2)

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print("Turno 3:", martes3)

    elif opcion_menu == 4:
        ocupados_lunes = 0
        libres_lunes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1

        if lunes2 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1

        if lunes3 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1

        if lunes4 != "":
            ocupados_lunes += 1
        else:
            libres_lunes += 1

        ocupados_martes = 0
        libres_martes = 0

        if martes1 != "":
            ocupados_martes += 1
        else:
            libres_martes += 1

        if martes2 != "":
            ocupados_martes += 1
        else:
            libres_martes += 1

        if martes3 != "":
            ocupados_martes += 1
        else:
            libres_martes += 1

        print("Resumen general:")
        print("Lunes -> Ocupados:", ocupados_lunes, "| Disponibles:", libres_lunes)
        print("Martes -> Ocupados:", ocupados_martes, "| Disponibles:", libres_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos reservados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos reservados: Martes")
        else:
            print("Empate entre Lunes y Martes.")

    elif opcion_menu == 5:
        print("Cerrando el sistema...")
        break

# Ejercicio 4: “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
bloqueado = False

print("""Historia:
Sos un agente que intenta abrir una bóveda con 3 cerraduras.
Tenés energía y tiempo limitados.
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.""")

while True:
    nombre_agente = input("Ingrese su nombre de agente: ")
    if not nombre_agente.isalpha():
        print("Error: El nombre debe ser solo letras.")
    else:
        break

print(f"\nBienvenido, agente {nombre_agente.title()}. ¡Que comience la misión!\n")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):

    print("----------------------------------------")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA' if alarma else 'apagada'}")
    print("""Menú:
1. Forzar cerradura
2. Hackear panel
3. Descansar""")

    opcion_juego = input("Ingrese una opción: ")
    while (not opcion_juego.isdigit()) or (opcion_juego.isdigit() and (int(opcion_juego) != 1 and int(opcion_juego) != 2 and int(opcion_juego) != 3)):
        print("Error: Ingrese un número entre 1 y 3.")
        opcion_juego = input("Ingrese una opción: ")

    opcion_juego = int(opcion_juego)

    if opcion_juego == 1:
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            alarma = True
            print("¡La cerradura se trabó! Alarma activada. No se abrió ninguna cerradura.")
            forzar_seguidas = 0
        else:
            if energia < 40:
                print("Riesgo de alarma: la energía está por debajo de 40.")
                numero_riesgo = input("Elija un número (1-3): ")
                while (not numero_riesgo.isdigit()) or (numero_riesgo.isdigit() and (int(numero_riesgo) != 1 and int(numero_riesgo) != 2 and int(numero_riesgo) != 3)):
                    print("Error: Ingrese un número entre 1 y 3.")
                    numero_riesgo = input("Elija un número (1-3): ")
                numero_riesgo = int(numero_riesgo)

                if numero_riesgo == 3:
                    alarma = True
                    print("¡Activaste la alarma! No se abrió ninguna cerradura.")
                else:
                    cerraduras_abiertas += 1
                    print("¡Cerradura forzada con éxito!")
            else:
                cerraduras_abiertas += 1
                print("¡Cerradura forzada con éxito!")

    elif opcion_juego == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3

        print("Hackeando panel...")
        for paso in range(4):
            codigo_parcial += "A"
            print(f"Paso {paso + 1}/4 -> código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Se abrió una cerradura automáticamente.")

    elif opcion_juego == 3:
        forzar_seguidas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1

        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma sigue activa y te quitó energía extra.")
        else:
            print("Descansaste y recuperaste energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        break

print("\n----------------------------------------")
print(f"Estado final -> Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")

if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! Agente {nombre_agente}, abriste la bóveda a tiempo.")
elif bloqueado:
    print("DERROTA: el sistema se bloqueó por la alarma. La bóveda quedó cerrada.")
elif energia <= 0:
    print("DERROTA: te quedaste sin energía.")
elif tiempo <= 0:
    print("DERROTA: se acabó el tiempo.")

# Ejercicio 5: Escape Room: “La Arena del Gladiador”

print("--- BIENVENIDO A LA ARENA ---")

nombre_gladiador = input("Nombre del Gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("Nombre del Gladiador: ")


vida_gladiador = 100
vida_enemigo = 100
pociones = 3
danio_ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:

    turno_gladiador = True
    print(f"\n{nombre_gladiador.title()} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    seleccion = input("Opción: ")
    while not seleccion.isdigit():
        print("Error: Ingrese un número válido.")
        seleccion = input("Opción: ")

    while seleccion not in ("1", "2", "3"):
        print("Error: La opción debe ser 1, 2 o 3.")
        seleccion = input("Opción: ")

    seleccion = int(seleccion)

    if seleccion == 1:
        if vida_enemigo < 20:
            danio_final = danio_ataque_pesado * 1.5
            print("¡Golpe Crítico!")
        else:
            danio_final = float(danio_ataque_pesado)
        vida_enemigo -= danio_final
        print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

    elif seleccion == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")

    elif seleccion == 3:
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print("Usaste una poción y recuperaste 30 puntos de vida.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    turno_gladiador = False

    if vida_enemigo > 0:
        vida_gladiador -= danio_enemigo
        print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

    if vida_gladiador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

print("\n=== FIN DEL COMBATE ===")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador.title()} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")