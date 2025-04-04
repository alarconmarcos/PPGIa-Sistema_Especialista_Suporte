from classPerguntas import *

dados = Pergunta()

class Diagnostico():

	# faz a busca no banco de dados, com base na pergunta e resposta
	# retorna a próxima pergunta ou 'Fim' se não houver mais perguntas
	def buscaDb(self, resposta, caract):	
		for i in range(len(dados.db)):
			if caract == dados.db[i][0]:
				if dados.db[i][1].upper() == resposta:
					return dados.db[i][2]
		return 'FIM'

	# dependendo a resposta já busca a próxima pergunta
	# essa função é chamada quando o usuário responde a pergunta
	def proxPergunta(self, resposta, caract):
		pergunta = self.buscaDb(resposta, caract)	
		return pergunta

	# Obtem a resposta do usuário e busca a próxima pergunta
	def pergunta(self,caract, pergunta):
		if self.proxPergunta('SIM', caract) == 'FIM':
			return 'FIM'	
		resp = input(pergunta).upper()
		if resp == 'SIM':
			return self.proxPergunta('SIM', caract)
		elif resp == 'NAO' or resp == 'NÃO':
			return self.proxPergunta('NÃO', caract)
