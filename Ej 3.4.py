import os
import mysql.connector
from mysql.connector import errorcode
import json

cursor = None
cnx = None

Tabla_Personajes = []
Tabla_Select_Personalizada = []

Campos_Validos = ['nombre', 'poder', 'raza', 'habilidad']

def Conectar_SQL():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='',
            host='localhost',
            database='mortalkombat'
        )
        cursor = cnx.cursor(dictionary=True)
        print("Conexión establecida con Mortal Kombat")
    except mysql.connector.Error as err:
        print("Error:", err)

def Crear_Tabla_Principal():
    global Tabla_Personajes
    consulta = """
    SELECT p.id_personaje, p.nombre, p.poder,
           r.nombre_raza AS raza,
           h.nombre_habilidad AS habilidad
    FROM personajes p
    INNER JOIN razas r ON p.raza = r.id_raza
    INNER JOIN habilidades h ON p.habilidad = h.id_habilidad;
    """
    cursor.execute(consulta)
    Tabla_Personajes = cursor.fetchall()

def Imprimir_Tabla(tabla, titulo):
    if not tabla:
        print(f"{titulo}: vacío")
        return

    encabezados = list(tabla[0].keys())
    anchuras = [max(len(str(fila[c])) for fila in tabla + [dict(zip(encabezados, encabezados))]) for c in encabezados]

    print(f"\n--- {titulo} ---")
    header = " | ".join(encabezados[i].ljust(anchuras[i]) for i in range(len(encabezados)))
    print(header)
    print("-" * len(header))

    for fila in tabla:
        print(" | ".join(str(fila[c]).ljust(anchuras[i]) for i, c in enumerate(encabezados)))

def Imprimir_Personajes():
    Imprimir_Tabla(Tabla_Personajes, "Personajes de Mortal Kombat")

def Crear_Json():
    os.makedirs("archivos", exist_ok=True)
    ruta = "archivos/personajes.json"
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(Tabla_Personajes, f, indent=4, ensure_ascii=False)
    print("JSON creado:", ruta)

def Select_Personalizado():
    campos = input("Ingrese los campos separados por coma (ej: nombre, poder, raza): ")
    sql = f"SELECT {campos} FROM personajes;"
    cursor.execute(sql)
    Tabla = cursor.fetchall()
    Imprimir_Tabla(Tabla, "Resultado del SELECT")

def Actualizar_Valor():
    idp = int(input("ID del personaje a actualizar: "))
    campo = input("Campo a modificar (nombre, poder, raza, habilidad): ")
    while campo not in Campos_Validos:
        campo = input("Ingrese un campo válido: ")
    nuevo = input("Nuevo valor: ")
    sql = f"UPDATE personajes SET {campo} = %s WHERE id_personaje = %s"
    cursor.execute(sql, (nuevo, idp))
    cnx.commit()
    print("Dato actualizado con éxito")
    Crear_Tabla_Principal()

def Insertar_Datos():
    while True:
        print("\nInsertar en:")
        print("1. Razas/Reinos")
        print("2. Habilidades")
        print("3. Personajes")
        print("0. Volver")
        op = int(input("-> "))

        if op == 1:
            nombre = input("Nombre del nuevo reino/raza: ")
            cursor.execute("INSERT INTO razas (nombre_raza) VALUES (%s)", (nombre,))
            cnx.commit()
            print("Raza/Reino agregado")

        elif op == 2:
            nombre = input("Nombre de la nueva habilidad: ")
            cursor.execute("INSERT INTO habilidades (nombre_habilidad) VALUES (%s)", (nombre,))
            cnx.commit()
            print("Habilidad agregada")

        elif op == 3:
            nombre = input("Nombre del personaje: ")
            poder = int(input("Poder: "))
            raza = int(input("ID de raza/reino: "))
            hab = int(input("ID de habilidad: "))
            cursor.execute(
                "INSERT INTO personajes (nombre, poder, raza, habilidad) VALUES (%s, %s, %s, %s)",
                (nombre, poder, raza, hab)
            )
            cnx.commit()
            Crear_Tabla_Principal()
            print("Personaje agregado")

        elif op == 0:
            break

def main():
    Conectar_SQL()
    Crear_Tabla_Principal()

    while True:
        print("\n--- MENÚ MORTAL KOMBAT ---")
        print("1. Imprimir tabla de personajes")
        print("2. Crear JSON")
        print("3. SELECT personalizado")
        print("4. Actualizar un valor")
        print("5. Insertar datos")
        print("0. Salir")
        opcion = int(input("-> "))

        if opcion == 1:
            Imprimir_Personajes()
        elif opcion == 2:
            Crear_Json()
        elif opcion == 3:
            Select_Personalizado()
        elif opcion == 4:
            Actualizar_Valor()
        elif opcion == 5:
            Insertar_Datos()
        elif opcion == 0:
            print("Saliendo...")
            break

    cnx.close()

main()
