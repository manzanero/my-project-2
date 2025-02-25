"hacer un calendario y que resalte la fecha actual"

import datetime

now = datetime.datetime.now()

print(now.day)

def print_de_numero(x, es_hoy=False):
    if len(x) == 1:
        x = f" {x}"
    if es_hoy:
        return f" *{x}* "
    else:
        return f"  {x}  "

texto_salida = "   L     M     X     J     V     S     D   \n"
dia_inicial_mes = 27

total_num = 7 * 6
contador = 0
for i in range(total_num):
    dia = dia_inicial_mes + i
    if dia > 31:
        dia = dia - 31
    if now.day == dia:
        es_hoy = True
        texto_salida =  texto_salida + print_de_numero(str(dia), es_hoy)
    else:
        texto_salida =  texto_salida + print_de_numero(str(dia))
    contador = contador + 1
    if contador == 7:
        texto_salida = texto_salida + "\n"
        contador = 0


print(texto_salida)
