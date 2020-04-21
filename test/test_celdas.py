from src.bingo import carton
from src.bingo import columna

def test_menos_de_quince():#verifica que no haya menos de 15 lugares ocupados
	menos_carton = carton()
	contador = 0
	for fila in menos_carton:
		for celda in fila:
			contador = contador + celda
			
	assert contador >= 15
	
def test_mas_de_quince():#verifica que no haya mas de 15 lugares ocupados
	mas_carton = carton()
	contador = 0
	for fila in mas_carton:
		for celda in fila:
			contador = contador + celda
			
	assert contador <= 15

def test_columnas():#verifica que no haya columnas vacias
	carton_columnas = carton()
	contador = 0
	bandera_columnas = 0
	while contador < 9:#mira todas las 9 columnas
		if ((columna(carton_columnas, contador)) == (0, 0, 0)):#si encuentra una columna vacia
			bandera_columnas = 1#pone una bandera
			break
		
		contador += 1
	
	assert bandera_columnas == 0


def test_filas():#verifica que no haya filas vacias
	carton_filas= carton()
	contador = 0
	bandera_filas = 0
	while contador < 3:#revisa las tres filas
		if ((carton_filas[contador]) == (0,0,0,0,0,0,0,0,0)):#si hay una fila vacia
			bandera_filas = 1#pone una bandera
			break

		contador += 1

	assert bandera_filas == 0

