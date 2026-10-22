
# SIMULACION DE MONTE CARLO PARA EL RETIRO

# Permite generar valores aleatorios, para simular los rendimientos de inversion para cada mes.
import random


capital_inicial = 50000
aportacion_mensual = 2000
years = 30
rendimiento_anual = 0.07

# Variacion anual de los rendimientos, establecida en 15%.
variacion_anual = 0.15

# Cantidad de escenarios diferentes que queremos simular.
numero_simulaciones = 1000

# Lista vacia para guardar el saldo final
resultados = []


# INICIAMOS LAS SIMULACIONES

for simulacion in range(numero_simulaciones):

    # Cada simulacion comienza con el mismo capital inicial.
    saldo = capital_inicial

    # Multiplicamos los años por 12 porque cada año tiene 12 meses.
    for mes in range(years * 12):

        # Random.gauss(promedio, desviacion) genera un numero aleatorio siguiendo una distribucion normal.
        rendimiento = random.gauss(
            rendimiento_anual / 12,
            variacion_anual / (12 ** 0.5)
        )

        # Aplicamos el rendimiento al saldo acumulado.
        # Si el rendimiento es positivo, el saldo aumenta.
        # Si es negativo, el saldo disminuye.
        saldo = saldo * (1 + rendimiento)

        # Agregamos la aportacion mensual despues de aplicar el rendimiento
        saldo = saldo + aportacion_mensual

    # Guardamos el saldo final
    resultados.append(saldo)


# ANALIZAMOS LOS RESULTADOS

# Ordenamos los saldos de menor a mayor.
resultados.sort()

# Obtenemos la mediana
mediana = resultados[len(resultados) // 2]

# Obtenemos un resultado cercano al percentil 5.
percentil_5 = resultados[int(numero_simulaciones * 0.05)]

# Obtenemos un resultado cercano al percentil 95.
percentil_95 = resultados[int(numero_simulaciones * 0.95)]


# MOSTRAMOS LOS RESULTADOS EN LA CONSOLA

print("SIMULACION DE MONTE CARLO PARA EL RETIRO")

print("Capital inicial: $", format(capital_inicial, ",.2f"))
print("Aportacion mensual: $", format(aportacion_mensual, ",.2f"))
print("Años de inversion:", years)
print("Simulaciones realizadas:", numero_simulaciones)

print()

# Calculamos el total aportado durante toda la inversion.
# Sumamos el capital inicial y todas las aportaciones mensuales.
print("Aportaciones totales: $", format(
    capital_inicial + aportacion_mensual * years * 12, ",.2f"
))

print("Escenario bajo: $", format(percentil_5, ",.2f"))
print("Resultado mediano: $", format(mediana, ",.2f"))
print("Escenario alto: $", format(percentil_95, ",.2f"))
