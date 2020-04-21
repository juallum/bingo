from src.bingo import carton

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

