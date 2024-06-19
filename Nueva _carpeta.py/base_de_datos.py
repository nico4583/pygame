# Importar el módulo sqlite3 para trabajar con bases de datos SQLite
import sqlite3

# Definir el nombre de la base de datos
NOMBRE_BASE_DE_DATOS = "data_ranking.db"

# Función para crear las tablas en la base de datos
def crear_tablas_db():
    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
        
        # Crear la tabla 'jugadores' si no existe
        conexion.execute('''CREATE TABLE IF NOT EXISTS jugadores (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ingreso TEXT,
                        score INTEGER
                    )''')
        
        # Cerrar la conexión
        conexion.close()
    except sqlite3.OperationalError:
        # Capturar la excepción si la tabla ya existe
        print("La tabla personajes ya existe")

# Función para insertar jugadores en la base de datos
def insertar_jugadores(ingreso, score):
    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
        print("Conexión exitosa a la base de datos")
        
        # Insertar un nuevo jugador en la tabla 'jugadores'
        conexion.execute("INSERT INTO jugadores (ingreso, score) VALUES (?,?)", (ingreso, score))
        
        # Hacer commit para guardar los cambios
        conexion.commit()
        
        # Cerrar la conexión
        conexion.close()
        
    except sqlite3.Error as e:
        # Capturar y mostrar un mensaje de error si ocurre algún problema al insertar
        print(f"Error al insertar jugadores: {e}")

# Función para obtener el ranking de jugadores ordenado por puntaje descendente
def obtener_ranking():
    try:
        # Conectar a la base de datos
        conexion = sqlite3.connect(NOMBRE_BASE_DE_DATOS)
        
        # Ejecutar una consulta para obtener el ranking de jugadores
        cursor = conexion.execute("SELECT ingreso, score FROM jugadores ORDER BY score DESC")
        
        # Obtener todas las filas del resultado de la consulta
        ranking = cursor.fetchall()
        
        # Retornar el ranking
        return ranking
    except:
        # Capturar y mostrar un mensaje de error si ocurre algún problema
        print("Error")