class Pergunta:
	# metodo construtor
	# carrega a lista de perguntas e respostas
	def __init__(self):
		self.lista = []

		arquivo = open('db.txt','r', encoding='utf-8')
		for linha in arquivo:
			linha = linha.strip()  # Remove espaços e quebras de linha
			if linha:
				# Divide a linha em 4 partes, considerando as 3 vírgulas e carrega somente os dois últimos
				dados = linha.split(',', 3)[-2:]
				self.lista.append(dados)
		arquivo.close()
  
	# busca a pergunta na lista de perguntas e respostas
	def texto(self, pergunta):
		for i in range(len(self.lista)): 
			if self.lista[i][0] == pergunta:
				return self.lista[i]
