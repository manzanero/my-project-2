"debe escribir por pantalla si var es primo"

var = 14

for i in range(var - 2):
    i = i + 2
    division = var / i
    if '.0' in str(division):
        es_primo = False
        break
    else:
        es_primo = True

if es_primo:
    print("SI")
else:
    print("NO")
