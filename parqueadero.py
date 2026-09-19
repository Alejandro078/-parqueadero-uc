print("=== PARQUEADERO UC ===")

# Cantidad de vehículos que se desean registrar
N = int(input("Ingrese la cantidad de vehículos a registrar: "))

# Capacidad máxima del parqueadero
CAPACIDAD = 30

# Estadísticas
total_validos = 0
total_recaudado = 0.0

cantidad_estudiantes = 0
cantidad_docentes = 0
cantidad_visitantes = 0

total_horas = 0.0


# Registro de vehículos
for i in range(N):

    # Control de cupos
    if total_validos >= CAPACIDAD:
        print("\nPARQUEADERO LLENO")
        break

    print(f"\n--- Vehículo {i + 1} ---")

    # 1. Entrada de datos
    placa = input("Ingrese la placa: ")

    tipo_usuario = input(
        "Ingrese el tipo de usuario (E estudiante / D docente / V visitante): "
    ).upper()

    hora_entrada = int(
        input("Ingrese la hora de entrada (0-23): ")
    )

    horas_permanencia = float(
        input("Ingrese las horas de permanencia: ")
    )

    # 2. Validación de la hora
    if hora_entrada < 0 or hora_entrada > 23:
        print("ERROR: la hora debe estar entre 0 y 23.")
        print("El vehículo no será contado en las estadísticas.")
        continue

    # 3. Validación de horas de permanencia
    if horas_permanencia <= 0:
        print("ERROR: las horas de permanencia deben ser mayores que cero.")
        print("El registro será rechazado.")
        continue

    # 4. Validación del tipo de usuario
    if tipo_usuario not in ["E", "D", "V"]:
        print("ADVERTENCIA: tipo de usuario no válido.")
        print("Se tratará como visitante.")
        tipo_usuario = "V"

    # 5. Cálculo de tarifa
    tarifa = 0.0

    if tipo_usuario == "E":
        # Estudiante: primeras 2 horas gratis
        # Luego $800 COP por hora adicional
        horas_adicionales = max(0, horas_permanencia - 2)
        tarifa = horas_adicionales * 800

        cantidad_estudiantes += 1

    elif tipo_usuario == "D":
        # Docente: $500 COP por hora
        tarifa = horas_permanencia * 500

        cantidad_docentes += 1

    else:
        # Visitante: $1500 primera hora
        # + $1200 por cada hora adicional
        if horas_permanencia <= 1:
            tarifa = 1500
        else:
            horas_adicionales = horas_permanencia - 1
            tarifa = 1500 + (horas_adicionales * 1200)

        cantidad_visitantes += 1

    # 6. Descuento nocturno
    descuento = 0.0

    if hora_entrada > 19 or hora_entrada < 6:
        descuento = tarifa * 0.10
        tarifa = tarifa - descuento

    # Redondear cobro a 2 decimales
    tarifa = round(tarifa, 2)

    # 7. Acumuladores
    total_validos += 1
    total_recaudado += tarifa
    total_horas += horas_permanencia

    # 8. Mostrar información del vehículo
    print("\nDatos del vehículo:")
    print(f"Placa: {placa}")
    print(f"Tipo de usuario: {tipo_usuario}")
    print(f"Hora de entrada: {hora_entrada}")
    print(f"Horas de permanencia: {horas_permanencia}")
    print(f"Tarifa a pagar: ${tarifa:.2f} COP")

    if descuento > 0:
        print("Se aplicó descuento nocturno del 10%.")


# =========================================================
# ESTADÍSTICAS FINALES
# =========================================================

print("\n===================================")
print("       ESTADÍSTICAS FINALES")
print("===================================")

print(f"Total de vehículos válidos: {total_validos}")
print(f"Total recaudado: ${total_recaudado:.2f} COP")
print(f"Cantidad de estudiantes: {cantidad_estudiantes}")
print(f"Cantidad de docentes: {cantidad_docentes}")
print(f"Cantidad de visitantes: {cantidad_visitantes}")

# Promedio de horas de permanencia
if total_validos > 0:
    promedio_horas = total_horas / total_validos
else:
    promedio_horas = 0

print(f"Promedio de horas de permanencia: {promedio_horas:.2f}")

# Porcentaje de ocupación
porcentaje_ocupacion = (total_validos / CAPACIDAD) * 100

print(f"Porcentaje de ocupación: {porcentaje_ocupacion:.2f}%")

# Mensaje si se llenó el parqueadero
if total_validos >= CAPACIDAD:
    print("\nPARQUEADERO LLENO")