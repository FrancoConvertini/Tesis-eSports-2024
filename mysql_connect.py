import mysql.connector

# Establish a connection to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="tesis2024",
    auth_plugin='mysql_native_password'
)


# Check if the connection is successful
if cnx.is_connected():
    print("Connected to MySQL database")
   # Crear un cursor
    cursor = cnx.cursor()

    # Ejecutar una consulta SQL para seleccionar los datos de la tabla
    cursor.execute("SELECT * FROM users")

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Imprimir los resultados
    for fila in resultados:
        print(fila)

    # Cerrar el cursor
    cursor.close()

# Close the connection
cnx.close()