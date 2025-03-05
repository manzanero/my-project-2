import json

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

sky = Sky()

def crear_cubo(posicion, _color=None, es_una_llave=False, es_una_puerta=True):
    if _color == None:
        _color = color.green

    entity = Entity(
        position=posicion,
        model='cube',
        scale=[1, 1, 1],
        color=_color,
        collider='box'
    )

    entity.es_llave = es_una_llave
    entity.es_puerta = es_una_puerta

    return entity

cubo_inicial = Entity(
        position=[0, 0, 0],
        model='cube',
        scale=[1, 1, 1],
        color=color.red,
        collider='box'
    )

cubo_final = Entity(
        position=[10, 0, 0],
        model='cube',
        scale=[1, 1, 1],
        color=color.red,
        collider='box'
    )


with open('mapas/mapa1.txt', 'r') as f:
    mapa = f.read()

lineas = mapa.splitlines()
for i in range(len(lineas)):
    columnas = lineas[i].split(' ')
    for j in range(len(columnas)):
        if columnas[j] == '0':
            crear_cubo([i, 0, j])
        if columnas[j] == '1':
            crear_cubo([i, 1, j], color.blue)
            crear_cubo([i, 2, j], color.blue)
        if columnas[j] == '2':
            crear_cubo([i, 0, j])
            llave = crear_cubo([i, 2, j], color.yellow, es_una_llave=True)
        if columnas[j] == '3':
            crear_cubo([i, 0, j])
            puerta1 = crear_cubo([i, 1, j], color.brown, es_una_puerta=True)
            puerta2 = crear_cubo([i, 2, j], color.brown, es_una_puerta=True)
            puerta2.esta_abierta = False

# for i in range(10):
#     j = random.randint(0, 4)
#     crear_cubo([i, 0, j])


player = FirstPersonController()
player.tiene_la_llave = False


def update():
    if player.position.y < -10:
        player.position = [0, 10, 0]

    rayo = raycast(player.position, player.down, distance=2, ignore=[player])
    if rayo.entity == cubo_final:
        Text(text="FIN", color=color.black, scale=(5, 5), origin=(0, -2))


def input(key):  # noqa
    if key == 'escape':
        exit()
    if key == 'h':
        Text(text="HOLA", color=color.black, scale=(5, 5), origin=(-3, 0))

    if key == 'left mouse down':
        rayo_interactuar = raycast(player.position + [0, 2, 0], player.forward, distance=1, ignore=[player])
        if rayo_interactuar.hit and rayo_interactuar.entity:
            if rayo_interactuar.entity == llave:
                Text(text="TIENES LA LLAVE", color=color.black, scale=(1, 1), origin=(0, 0))
                destroy(llave)
                player.tiene_la_llave = True

            if rayo_interactuar.entity == puerta2 and player.tiene_la_llave:
                destroy(puerta1)
                destroy(puerta2)
                puerta2.esta_abierta = True

    if key == 's':
        data = {
            "posicion": list(player.position),
            "tiene la llave": player.tiene_la_llave,
            "puerta abierta": puerta2.esta_abierta
        }

        with open('partida_guardada.txt', 'w') as f:
            f.write(json.dumps(data))

    if key == 'l':
        with open('partida_guardada.txt', 'r') as f:
            data = json.loads(f.read())

        player.position = data["posicion"]
        if data["tiene la llave"]:
            destroy(llave)
            player.tiene_la_llave = True
        if data["puerta abierta"]:
            destroy(puerta1)
            destroy(puerta2)

app.run()