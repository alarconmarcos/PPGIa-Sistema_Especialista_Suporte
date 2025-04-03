from classDiagnostico import *

# classe que representa as perguntas e respostas do sistema especialista
class Pergunta:
	
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



	# busca a pergunta na lista de perguntas e respostas
	def texto(self, pergunta):
		for i in range(len(self.db)): 
			if self.db[i][2] == pergunta:
				return self.db[i]
