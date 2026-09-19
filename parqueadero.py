print("====== PARQUEADERO UC ======")

# N se define directamente, NO mediante input()
N = 3
CAPACIDAD = 30

# Acumuladores
vehiculos_validos = 0
total_recaudado = 0.0

estudiantes = 0
docentes = 0
visitantes = 0

total_horas = 0.0

# Control del ciclo
i = 0

# Ciclo obligatorio con WHILE
while i < N and vehiculos_validos < CAPACIDAD:

    print("\n--- VEHICULO", i + 1, "---")

    # Entrada de datos
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

    # -------------------------------------------------
    # VALIDACION DE HORA
    # -------------------------------------------------
    if hora_entrada < 0 or hora_entrada > 23:
        print("ERROR: hora invalida.")
        print("El vehiculo no sera contado.")
        i = i + 1
        continue

    # -------------------------------------------------
    # VALIDACION DE HORAS
    # -------------------------------------------------
    if horas_permanencia <= 0:
        print("ERROR: las horas deben ser mayores que cero.")
        print("El registro sera rechazado.")
        i = i + 1
        continue

    # -------------------------------------------------
    # VALIDACION DEL TIPO DE USUARIO
    # -------------------------------------------------
    if tipo_usuario != "E" and tipo_usuario != "D" and tipo_usuario != "V":
        print("ADVERTENCIA: tipo de usuario invalido.")
        print("Se tratara como visitante.")
        tipo_usuario = "V"

    # -------------------------------------------------
    # CALCULO DE TARIFA
    # -------------------------------------------------

    # Estructura if-elif-else para calcular la tarifa
    if tipo_usuario == "E":

        # Estudiante:
        # primeras 2 horas gratis
        # luego $800 COP por hora adicional
        if horas_permanencia <= 2:
            tarifa = 0
        else:
            horas_adicionales = horas_permanencia - 2
            tarifa = horas_adicionales * 800

        estudiantes = estudiantes + 1

    elif tipo_usuario == "D":

        # Docente: $500 COP por hora
        tarifa = horas_permanencia * 500

        docentes = docentes + 1

    else:

        # Visitante:
        # primera hora $1500
        # cada hora adicional $1200
        if horas_permanencia <= 1:
            tarifa = 1500
        else:
            horas_adicionales = horas_permanencia - 1
            tarifa = 1500 + (horas_adicionales * 1200)

        visitantes = visitantes + 1

    # -------------------------------------------------
    # DESCUENTO NOCTURNO
    # -------------------------------------------------

    descuento = 0

    if hora_entrada > 19 or hora_entrada < 6:
        descuento = tarifa * 0.10
        tarifa = tarifa - descuento

    # Redondear a 2 decimales
    tarifa = round(tarifa, 2)

    # -------------------------------------------------
    # ACUMULADORES
    # -------------------------------------------------

    vehiculos_validos = vehiculos_validos + 1
    total_recaudado = total_recaudado + tarifa
    total_horas = total_horas + horas_permanencia

    # -------------------------------------------------
    # INFORMACION DEL VEHICULO
    # -------------------------------------------------

    print("\nDatos del vehiculo:")
    print("Placa:", placa)
    print("Tipo de usuario:", tipo_usuario)
    print("Hora de entrada:", hora_entrada)
    print("Horas de permanencia:", horas_permanencia)
    print("Tarifa a pagar: $", format(tarifa, ".2f"), "COP")

    if descuento > 0:
        print("Descuento nocturno aplicado: 10%")

    i = i + 1


# =====================================================
# ESTADISTICAS FINALES
# =====================================================

print("\n")
print("====== RESUMEN DEL DIA ======")

print(
    "Vehiculos registrados:",
    str(vehiculos_validos) + "/" + str(CAPACIDAD)
)

ocupacion = (vehiculos_validos / CAPACIDAD) * 100

print("Ocupacion:", format(ocupacion, ".2f") + "%")

print(
    "Recaudo total: $",
    format(total_recaudado, ".2f")
)

print(
    "Estudiantes:", estudiantes,
    "| Docentes:", docentes,
    "| Visitantes:", visitantes
)

if vehiculos_validos > 0:
    promedio_horas = total_horas / vehiculos_validos
else:
    promedio_horas = 0

print(
    "Promedio de permanencia:",
    format(promedio_horas, ".2f"),
    "horas"
)

print("==============================")

if vehiculos_validos >= CAPACIDAD:
    print("PARQUEADERO LLENO")
