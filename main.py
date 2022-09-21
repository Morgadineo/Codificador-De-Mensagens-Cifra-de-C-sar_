from string import 	ascii_lowercase

mensagem = str(input(''))

def codificar(mensagem: str, n=1):
	"""Codifica a mensagem enviada.
 
	param:
 	mensagem = string a ser modificada
  	n = numero que somado ira substituir o caracter atual"""
	
	codigo = ''
	for char in mensagem:
		if char == ' ':
			codigo += char
		elif char not in ascii_lowercase:
			char = '-'
			
		else:
			posicao = ascii_lowercase.find(char) + n
			char = ascii_lowercase[posicao % 26]
			codigo += char
	return codigo

def decodificar(mensagem: str, n=1):
	"""Decodifica a mensagem enviada.

  	param:
   	mensagem = string a ser decodificada
   	n = numero que somado ira substituir o caracter atual
	"""
	codigo = ''
	
	for char in mensagem:
		if char == ' ':
			codigo += char
		elif char not in ascii_lowercase:
			char = 'n'
		else:
			posicao = ascii_lowercase.find(char) - n
			char = ascii_lowercase[posicao % 26]
			codigo += char
			
	return codigo
		


print(codificar(mensagem))
print(decodificar(codificar(mensagem)))
