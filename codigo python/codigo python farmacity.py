import mysql.connector
from mysql.connector import errorcode
from datetime import date, timedelta

cnx = None
cursor = None

def conectar_base():
    global cnx, cursor
    try:
        cnx = mysql.connector.connect(user="root",password="",host="localhost",database="farmacity")
        cursor = cnx.cursor(dictionary=True)
        print("conexion establecida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("usuario o contraseña incorrectos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("la base de datos no existe")
        else:
            print(err)

def select_medicamentos():
    cursor.execute("select * from medicamentos")
    return cursor.fetchall()

def select_ventas():
    cursor.execute("select * from ventas")
    return cursor.fetchall()

def mostrar_medicamento_por_id(id_medicamento):
    sql = "select * from medicamentos where id_medicamentos = %s"
    cursor.execute(sql, (id_medicamento,))
    return cursor.fetchone()

def mostrar_venta_por_id(id_venta):
    sql = """
        select ventas.id_venta, medicamentos.nombre, medicamentos.categoria,
               ventas.fecha, ventas.cantidad
        from ventas
        inner join medicamentos
            on ventas.id_medicamento = medicamentos.id_medicamentos
        where ventas.id_venta = %s
    """
    cursor.execute(sql, (id_venta,))
    return cursor.fetchone()

def insertar_medicamento(nombre, categoria, precio, stock):
    sql = """
        insert into medicamentos (nombre, categoria, precio, stock)
        values (%s, %s, %s, %s)
    """
    cursor.execute(sql, (nombre, categoria, precio, stock))
    cnx.commit()
    return cursor.lastrowid

def insertar_venta(id_medicamento, fecha, cantidad):
    sql = """
        insert into ventas (id_medicamento, fecha, cantidad)
        values (%s, %s, %s)
    """
    cursor.execute(sql, (id_medicamento, fecha, cantidad))
    cnx.commit()
    return cursor.lastrowid


def eliminar_medicamento(id_medicamento):
    cursor.execute(
        "delete from medicamentos where id_medicamentos = %s",
        (id_medicamento,)
    )
    cnx.commit()

def eliminar_venta(id_venta):
    cursor.execute(
        "delete from ventas where id_venta = %s",
        (id_venta,)
    )
    cnx.commit()

def calcular_total_ventas():
    sql = """
        select sum(ventas.cantidad * medicamentos.precio) as total
        from ventas
        inner join medicamentos
            on ventas.id_medicamento = medicamentos.id_medicamentos
    """
    cursor.execute(sql)
    r = cursor.fetchone()
    return r["total"] if r["total"] else 0

def reporte_top_5_mas_vendidos():
    sql = """
        select medicamentos.nombre, sum(ventas.cantidad) as total_vendido
        from ventas
        inner join medicamentos
            on ventas.id_medicamento = medicamentos.id_medicamentos
        group by medicamentos.nombre
        order by total_vendido desc
        limit 5
    """
    cursor.execute(sql)
    datos = cursor.fetchall()

    with open("top_5_medicamentos.txt", "w", encoding="utf-8") as f:
        f.write("TOP 5 MEDICAMENTOS MAS VENDIDOS\n\n")
        for d in datos:
            f.write(f"{d['nombre']} - {d['total_vendido']} unidades\n")

def reporte_stock_critico():
    cursor.execute(
        "select nombre, stock from medicamentos where stock < 10"
    )
    datos = cursor.fetchall()

    with open("stock_critico.txt", "w", encoding="utf-8") as f:
        f.write("MEDICAMENTOS CON STOCK CRITICO (<10)\n\n")
        for d in datos:
            f.write(f"{d['nombre']} - stock: {d['stock']}\n")

def reporte_mas_vendidos_ultimo_mes():
    hace_un_mes = date.today() - timedelta(days=30)

    sql = """
        select medicamentos.nombre, count(ventas.id_venta) as ventas_realizadas
        from ventas
        inner join medicamentos
            on ventas.id_medicamento = medicamentos.id_medicamentos
        where ventas.fecha >= %s
        group by medicamentos.nombre
        having ventas_realizadas > 5
    """
    cursor.execute(sql, (hace_un_mes,))
    datos = cursor.fetchall()

    with open("mas_vendidos_ultimo_mes.txt", "w", encoding="utf-8") as f:
        f.write("MEDICAMENTOS MAS VENDIDOS EN EL ULTIMO MES\n\n")
        for d in datos:
            f.write(f"{d['nombre']} - ventas: {d['ventas_realizadas']}\n")

def menu():
    while True:
        print("\n========== FARMACITY ==========")
        print("1. listar medicamentos")
        print("2. agregar medicamento")
        print("3. registrar venta")
        print("4. mostrar medicamento por id")
        print("5. mostrar venta por id")
        print("6. calcular total de ventas")
        print("7. eliminar medicamento")
        print("8. eliminar venta")
        print("9. generar reportes")
        print("0. salir")
        print("================================")

        opc = input("opcion: ")

        if opc == "1":
            for d in select_medicamentos():
                print(d)

        elif opc == "2":
            n = input("nombre: ")
            c = input("categoria: ")
            p = float(input("precio: "))
            s = int(input("stock: "))
            print("id creado:", insertar_medicamento(n, c, p, s))

        elif opc == "3":
            idm = int(input("id medicamento: "))
            f = input("fecha (aaaa-mm-dd): ")
            cant = int(input("cantidad: "))
            print("id venta:", insertar_venta(idm, f, cant))

        elif opc == "4":
            print(mostrar_medicamento_por_id(int(input("id: "))))

        elif opc == "5":
            print(mostrar_venta_por_id(int(input("id: "))))

        elif opc == "6":
            print("total vendido: $", calcular_total_ventas())

        elif opc == "7":
            eliminar_medicamento(int(input("id: ")))
            print("medicamento eliminado")

        elif opc == "8":
            eliminar_venta(int(input("id: ")))
            print("venta eliminada")

        elif opc == "9":
            reporte_top_5_mas_vendidos()
            reporte_stock_critico()
            reporte_mas_vendidos_ultimo_mes()
            print("reportes generados (txt)")

        elif opc == "0":
            break

        else:
            print("opcion incorrecta")

conectar_base()
menu()

if cnx and cnx.is_connected():
    cnx.close()
    print("conexion cerrada")