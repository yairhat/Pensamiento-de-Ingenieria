import networkx as nx
import matplotlib.pyplot as plt

metro = nx.Graph()

# LINEA 1 - ROSA
metro.add_edge("Observatorio", "Tacubaya")
metro.add_edge("Tacubaya", "Juanacatlán")
metro.add_edge("Juanacatlán", "Chapultepec")
metro.add_edge("Chapultepec", "Sevilla")
metro.add_edge("Sevilla", "Insurgentes")
metro.add_edge("Insurgentes", "Cuauhtémoc")
metro.add_edge("Cuauhtémoc", "Balderas")
metro.add_edge("Balderas", "Salto del Agua")
metro.add_edge("Salto del Agua", "Isabel la Católica")
metro.add_edge("Isabel la Católica", "Pino Suárez")
metro.add_edge("Pino Suárez", "Merced")
metro.add_edge("Merced", "Candelaria")
metro.add_edge("Candelaria", "San Lázaro")
metro.add_edge("San Lázaro", "Moctezuma")
metro.add_edge("Moctezuma", "Balbuena")
metro.add_edge("Balbuena", "Boulevard Puerto Aéreo")
metro.add_edge("Boulevard Puerto Aéreo", "Gómez Farías")
metro.add_edge("Gómez Farías", "Zaragoza")
metro.add_edge("Zaragoza", "Pantitlán")

# LINEA 2 - AZUL
metro.add_edge("Cuatro Caminos", "Panteones")
metro.add_edge("Panteones", "Tacuba")
metro.add_edge("Tacuba", "Cuitláhuac")
metro.add_edge("Cuitláhuac", "Popotla")
metro.add_edge("Popotla", "Colegio Militar")
metro.add_edge("Colegio Militar", "Normal")
metro.add_edge("Normal", "San Cosme")
metro.add_edge("San Cosme", "Revolución")
metro.add_edge("Revolución", "Hidalgo")
metro.add_edge("Hidalgo", "Bellas Artes")
metro.add_edge("Bellas Artes", "Allende")
metro.add_edge("Allende", "Zócalo/Tenochtitlan")
metro.add_edge("Zócalo/Tenochtitlan", "Pino Suárez")
metro.add_edge("Pino Suárez", "San Antonio Abad")
metro.add_edge("San Antonio Abad", "Chabacano")
metro.add_edge("Chabacano", "Viaducto")
metro.add_edge("Viaducto", "Xola")
metro.add_edge("Xola", "Villa de Cortés")
metro.add_edge("Villa de Cortés", "Nativitas")
metro.add_edge("Nativitas", "Portales")
metro.add_edge("Portales", "Ermita")
metro.add_edge("Ermita", "General Anaya")
metro.add_edge("General Anaya", "Tasqueña")

# LINEA 3 - VERDE OLIVO
metro.add_edge("Indios Verdes", "Deportivo 18 de Marzo")
metro.add_edge("Deportivo 18 de Marzo", "Potrero")
metro.add_edge("Potrero", "La Raza")
metro.add_edge("La Raza", "Tlatelolco")
metro.add_edge("Tlatelolco", "Guerrero")
metro.add_edge("Guerrero", "Hidalgo")
metro.add_edge("Hidalgo", "Juárez")
metro.add_edge("Juárez", "Balderas")
metro.add_edge("Balderas", "Niños Héroes")
metro.add_edge("Niños Héroes", "Hospital General")
metro.add_edge("Hospital General", "Centro Médico")
metro.add_edge("Centro Médico", "Etiopía")
metro.add_edge("Etiopía", "Eugenia")
metro.add_edge("Eugenia", "División del Norte")
metro.add_edge("División del Norte", "Zapata")
metro.add_edge("Zapata", "Coyoacán")
metro.add_edge("Coyoacán", "Viveros")
metro.add_edge("Viveros", "Miguel Ángel de Quevedo")
metro.add_edge("Miguel Ángel de Quevedo", "Copilco")
metro.add_edge("Copilco", "Universidad")

# LINEA 4 - AZUL CLARO
metro.add_edge("Martín Carrera", "Talismán")
metro.add_edge("Talismán", "Bondojito")
metro.add_edge("Bondojito", "Consulado")
metro.add_edge("Consulado", "Canal del Norte")
metro.add_edge("Canal del Norte", "Morelos")
metro.add_edge("Morelos", "Candelaria")
metro.add_edge("Candelaria", "Fray Servando")
metro.add_edge("Fray Servando", "Jamaica")
metro.add_edge("Jamaica", "Santa Anita")


# LINEA 5 - AMARILLA
metro.add_edge("Pantitlán", "Hangares")
metro.add_edge("Hangares", "Terminal Aérea")
metro.add_edge("Terminal Aérea", "Oceanía")
metro.add_edge("Oceanía", "Aragón")
metro.add_edge("Aragón", "Eduardo Molina")
metro.add_edge("Eduardo Molina", "Consulado")
metro.add_edge("Consulado", "Valle Gómez")
metro.add_edge("Valle Gómez", "Misterios")
metro.add_edge("Misterios", "La Raza")
metro.add_edge("La Raza", "Autobuses del Norte")
metro.add_edge("Autobuses del Norte", "Instituto del Petróleo")
metro.add_edge("Instituto del Petróleo", "Politécnico")


# LINEA 6 - ROJA
metro.add_edge("El Rosario", "Tezozómoc")
metro.add_edge("Tezozómoc", "Azcapotzalco")
metro.add_edge("Azcapotzalco", "Ferrería/Arena Ciudad de México")
metro.add_edge("Ferrería/Arena Ciudad de México", "Norte 45")
metro.add_edge("Norte 45", "Vallejo")
metro.add_edge("Vallejo", "Instituto del Petróleo")
metro.add_edge("Instituto del Petróleo", "Lindavista")
metro.add_edge("Lindavista", "Deportivo 18 de Marzo")
metro.add_edge("Deportivo 18 de Marzo", "La Villa-Basílica")
metro.add_edge("La Villa-Basílica", "Martín Carrera")

# LINEA 7 - NARANJA 
metro.add_edge("El Rosario", "Aquiles Serdán")
metro.add_edge("Aquiles Serdán", "Camarones")
metro.add_edge("Camarones", "Refinería")
metro.add_edge("Refinería", "Tacuba")
metro.add_edge("Tacuba", "San Joaquín")
metro.add_edge("San Joaquín", "Polanco")
metro.add_edge("Polanco", "Auditorio")
metro.add_edge("Auditorio", "Constituyentes")
metro.add_edge("Constituyentes", "Tacubaya")
metro.add_edge("Tacubaya", "San Pedro de los Pinos")
metro.add_edge("San Pedro de los Pinos", "San Antonio")
metro.add_edge("San Antonio", "Mixcoac")
metro.add_edge("Mixcoac", "Barranca del Muerto")


# LINEA 8 - VERDE
metro.add_edge("Garibaldi/Lagunilla", "Bellas Artes")
metro.add_edge("Bellas Artes", "San Juan de Letrán")
metro.add_edge("San Juan de Letrán", "Salto del Agua")
metro.add_edge("Salto del Agua", "Doctores")
metro.add_edge("Doctores", "Obrera")
metro.add_edge("Obrera", "Chabacano")
metro.add_edge("Chabacano", "La Viga")
metro.add_edge("La Viga", "Santa Anita")
metro.add_edge("Santa Anita", "Coyuya")
metro.add_edge("Coyuya", "Iztacalco")
metro.add_edge("Iztacalco", "Apatlaco")
metro.add_edge("Apatlaco", "Aculco")
metro.add_edge("Aculco", "Escuadrón 201")
metro.add_edge("Escuadrón 201", "Atlalilco")
metro.add_edge("Atlalilco", "Iztapalapa")
metro.add_edge("Iztapalapa", "Cerro de la Estrella")
metro.add_edge("Cerro de la Estrella", "UAM-I")
metro.add_edge("UAM-I", "Constitución de 1917")


# LINEA 8 - MARRON
metro.add_edge("Tacubaya", "Patriotismo")
metro.add_edge("Patriotismo", "Chilpancingo")
metro.add_edge("Chilpancingo", "Centro Médico")
metro.add_edge("Centro Médico", "Lázaro Cárdenas")
metro.add_edge("Lázaro Cárdenas", "Chabacano")
metro.add_edge("Chabacano", "Jamaica")
metro.add_edge("Jamaica", "Mixiuhca")
metro.add_edge("Mixiuhca", "Velódromo")
metro.add_edge("Velódromo", "Ciudad Deportiva")
metro.add_edge("Ciudad Deportiva", "Puebla")
metro.add_edge("Puebla", "Pantitlán")

# LINEA A - MORADO
metro.add_edge("Pantitlán", "Agrícola Oriental")
metro.add_edge("Agrícola Oriental", "Canal de San Juan")
metro.add_edge("Canal de San Juan", "Tepalcates")
metro.add_edge("Tepalcates", "Guelatao")
metro.add_edge("Guelatao", "Peñón Viejo")
metro.add_edge("Peñón Viejo", "Acatitla")
metro.add_edge("Acatitla", "Santa Marta")
metro.add_edge("Santa Marta", "Los Reyes")
metro.add_edge("Los Reyes", "La Paz")


# LINEA B - VERDE Y GRIS
metro.add_edge("Buenavista", "Guerrero")
metro.add_edge("Guerrero", "Garibaldi/Lagunilla")
metro.add_edge("Garibaldi/Lagunilla", "Lagunilla")
metro.add_edge("Lagunilla", "Tepito")
metro.add_edge("Tepito", "Morelos")
metro.add_edge("Morelos", "San Lázaro")
metro.add_edge("San Lázaro", "Ricardo Flores Magón")
metro.add_edge("Ricardo Flores Magón", "Romero Rubio")
metro.add_edge("Romero Rubio", "Oceanía")
metro.add_edge("Oceanía", "Deportivo Oceanía")
metro.add_edge("Deportivo Oceanía", "Bosque de Aragón")
metro.add_edge("Bosque de Aragón", "Villa de Aragón")
metro.add_edge("Villa de Aragón", "Nezahualcóyotl")
metro.add_edge("Nezahualcóyotl", "Impulsora")
metro.add_edge("Impulsora", "Río de los Remedios")
metro.add_edge("Río de los Remedios", "Múzquiz")
metro.add_edge("Múzquiz", "Ecatepec")
metro.add_edge("Ecatepec", "Olímpica")
metro.add_edge("Olímpica", "Plaza Aragón")
metro.add_edge("Plaza Aragón", "Ciudad Azteca")


# LINEA 12 - ORO
metro.add_edge("Mixcoac", "Insurgentes Sur")
metro.add_edge("Insurgentes Sur", "Hospital 20 de Noviembre")
metro.add_edge("Hospital 20 de Noviembre", "Zapata")
metro.add_edge("Zapata", "Parque de los Venados")
metro.add_edge("Parque de los Venados", "Eje Central")
metro.add_edge("Eje Central", "Ermita")
metro.add_edge("Ermita", "Mexicaltzingo")
metro.add_edge("Mexicaltzingo", "Atlalilco")
metro.add_edge("Atlalilco", "Culhuacán")
metro.add_edge("Culhuacán", "San Andrés Tomatlán")
metro.add_edge("San Andrés Tomatlán", "Lomas Estrella")
metro.add_edge("Lomas Estrella", "Calle 11")
metro.add_edge("Calle 11", "Periférico Oriente")
metro.add_edge("Periférico Oriente", "Tezonco")
metro.add_edge("Tezonco", "Olivos")
metro.add_edge("Olivos", "Nopalera")
metro.add_edge("Nopalera", "Zapotitlán")
metro.add_edge("Zapotitlán", "Tlaltenco")
metro.add_edge("Tlaltenco", "Tláhuac")

# Información del grafo
print("Total de estaciones:", metro.number_of_nodes())
print("Total de conexiones:", metro.number_of_edges())

# Crear la figura
plt.figure(figsize=(28, 22))

# Organizar las estaciones
posiciones = nx.spring_layout(
    metro,
    k=0.8,
    iterations=300,
    seed=42
)

# Dibujar el grafo
nx.draw(
    metro,
    posiciones,
    with_labels=True,
    node_size=110,
    node_color="skyblue",
    edge_color="gray",
    font_size=6,
    font_weight="normal",
    width=1.2
)

# Título del grafo
plt.title(
    "Red del Metro de la Ciudad de México",
    fontsize=24,
    fontweight="bold",
    pad=25
)

# Guardar la imagen
plt.savefig(
    "metro.png",
    dpi=300,
    bbox_inches="tight"
)

# Mostrar el grafo
plt.show()