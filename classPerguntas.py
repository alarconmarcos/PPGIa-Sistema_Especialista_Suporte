from classDiagnostico import *

dados = Diagnostico()

class Pergunta:
	# busca a pergunta na lista de perguntas e respostas
	def texto(self, pergunta):
		for i in range(len(dados.db)): 
			if dados.db[i][2] == pergunta:
				return dados.db[i]
