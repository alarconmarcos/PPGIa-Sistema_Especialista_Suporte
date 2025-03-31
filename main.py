# Pequeno sistema especialista em python para diagnosticar problemas no computador

# PUCPR
# Disciplina: Inteligência Artificial
# Professor: Edson Emilio Scalabrin
# Alunos: Marcos Alarcon, Daniel Volanick e Camila Gonçalves Marques


from classDiagnostico import *
from classPerguntas import *

#Inferência
se = Diagnostico()
pergunta = Pergunta()

#A primeira pergunta é a primeira linha do arquivo
proxPergunta = pergunta.lista[0][0]

while proxPergunta != 'Fim':
	string = pergunta.texto(proxPergunta)
	proxPergunta = se.pergunta(string[0],string[1])


print(string[1])


# DICAS DE TESTE:

# Não não não 			  = (Ligue na tomada)
# não não sim  			  = (A fonte está queimada)
# não sim não  			  = (A fonte está com problema)
# não sim sim 			  = (Placa mãe queimada)
# sim sim sim não 		  =	(Sistema Operacional corrompido)
# sim sim sim sim         =	(Sem problemas, tudo normal)
# sim sim não sim sim sim = (Sistema Operacional corrompido)
# sim sim não sim sim não = (Troar o HD)
# sim sim não sim não 	  =	(boot)
# sim sim não não 		  =	(HD está desconectado)
# sim não sim 			  =	(Problema na memória ram e processador)
# sim não não 			  =	(Problema na placa mãe)


