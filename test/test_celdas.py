from src.bingo import carton
from src.bingo import columna

def test_menos_de_quince():
	menos_carton = carton()
	contador = 0
	for fila in menos_carton:
		for celda in fila:
			contador = contador + celda
			
	assert contador >= 15
	
def test_mas_de_quince():
	mas_carton = carton()
	contador = 0
	for fila in mas_carton:
		for celda in fila:
			contador = contador + celda
			
	assert contador <= 15

def test_columnas():
	carton_columnas = carton()
	contador = 0
	bandera_columnas = 0
	while contador < 9:
		if ((columna(carton_columnas, contador)) == (0, 0, 0)):
			bandera_columnas = 1
			break
		
		contador += 1
	
	assert bandera_columnas == 0

	