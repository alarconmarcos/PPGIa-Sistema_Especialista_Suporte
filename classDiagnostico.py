class Diagnostico():
	# metodo construtor
	def __init__(self):
		self.db = []

		# abre o arquivo db.txt e lê as linhas
		# armazena as linhas em uma lista, separando os dados por ponto e vírgula
		# cada linha do arquivo representa uma pergunta, resposta, diagnóstico ou próxima pergunta
		
		arquivo = open('db.txt','r', encoding='utf-8')
		for linha in arquivo:
			linha = linha.strip()  # Remove espaços e quebras de linha
			if linha:
				# Separa os dados por ponto e vírgula
				dados = linha.split(';')
				self.db.append(dados)

		arquivo.close()



	# faz a busca no banco de dados, com base na pergunta e resposta
	# retorna a próxima pergunta ou 'Fim' se não houver mais perguntas
	def buscaDb(self, resposta, caract):	
		for i in range(len(self.db)):
			if caract == self.db[i][0]:
				if self.db[i][1].upper() == resposta:
					return self.db[i][2]
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
