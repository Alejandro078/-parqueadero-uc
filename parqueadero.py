print("=== PARQUEADERO UC ===")


placa = input("Ingrese la placa del vehículo: ")
tipo_usuario = input(
    "Ingrese el tipo de usuario (estudiante/docente/visitante): "
).lower()

hora_entrada = int(input("Ingrese la hora de entrada (0-23): "))
minutos_permanencia = int(input("Ingrese los minutos de permanencia: "))



if tipo_usuario == "estudiante":
    tarifa_hora = 1000
elif tipo_usuario == "docente":
    tarifa_hora = 1500
elif tipo_usuario == "visitante":
    tarifa_hora = 2000
else:
    print("Tipo de usuario no válido.")
    exit()



horas_cobrables = minutos_permanencia // 60

if minutos_permanencia % 60 != 0:
    horas_cobrables += 1

if horas_cobrables == 0:
    horas_cobrables = 1



tarifa = horas_cobrables * tarifa_hora




if hora_entrada >= 20 or hora_entrada < 6:
    tarifa_final = tarifa 
else:
    tarifa_final = tarifa


print("\n=== DATOS DEL VEHÍCULO ===")
print(f"Placa: {placa}")
print(f"Tipo de usuario: {tipo_usuario}")
print(f"Hora de entrada: {hora_entrada}")
print(f"Minutos de permanencia: {minutos_permanencia}")
print(f"Horas cobrables: {horas_cobrables}")
print(f"Tarifa por hora: ${tarifa_hora}")
print(f"TOTAL A PAGAR: ${tarifa_final:.0f}")
