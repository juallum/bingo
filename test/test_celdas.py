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
	test_carton = carton()
	contador = 0
	bandera_test = 0
	while contador < 9:
		if ((columna(test_carton, contador)) == (0, 0, 0)):
			bandera_test = 1
			break
		
		contador += 1
	
	assert bandera_test == 0;