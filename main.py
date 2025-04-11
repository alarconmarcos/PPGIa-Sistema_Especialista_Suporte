# Pequeno sistema especialista em python para diagnosticar problemas no computador

# PUCPR
# Disciplina: Inteligência Artificial
# Professor: Edson Emilio Scalabrin
# Alunos: Marcos Alarcon, Daniel Volanick e Camila Gonçalves Marques

from classDiagnostico import *
from classPerguntas import *

#Inferência
se = Diagnostico()
busca = Pergunta()

#A primeira pergunta é a primeira linha do arquivo
proxPergunta = busca.db[0][2]

print("=" * 100)
print("\nSistema especialista de diagnóstico de computadores\n")
print("=" * 100)
print("\nResponda as perguntas com Sim ou Não\n")


while proxPergunta != 'FIM':
	string = busca.texto(proxPergunta)
	proxPergunta = se.pergunta(string[2],string[3])

print("\n" + "=" * 100 + "\n")
print("Diagnóstico: " + string[3])
print("\n" + "=" * 100 + "\n")











# LISTA DE REGRAS

# 1. SE (o computador liga 							= Sim) 
#    E (A BIOS está iniciando 						= Sim) 
#    E (O Sistema Operacional inicia 				= Sim) 
#    E (O sistema operacional inicia completamente 	= Sim) 
#	 ENTÃO (Sem problemas, tudo normal)


# 2. SE (o computador liga 							= Sim)
#    E (A BIOS está iniciando 						= Sim)
#    E (O Sistema Operacional inicia 				= Sim)
#    E (O sistema operacional inicia completamente 	= Não)
#	 ENTÃO (O Sistema Operacional está corrompido)

# 3. SE (o computador liga 							= Sim)
#    E (A BIOS está iniciando 						= Sim)	
#    E (O Sistema Operacional inicia 				= Não)
#    E (A unidade de armazenamento é detectada 		= Sim)
#	 E (A ordem de boot está correta 				= Sim)
#	 E (A unidade de armazenamento está íntegra 	= Sim)
#	 ENTÃO (O Sistema Operacional está corrompido)

# 4. SE (o computador liga 							= Sim)
#    E (A BIOS está iniciando 						= Sim)	
#    E (O Sistema Operacional inicia 				= Não)
#    E (A unidade de armazenamento é detectada 		= Sim)
#	 E (A ordem de boot está correta 				= Sim)
#	 E (A unidade de armazenamento está íntegra 	= Não)
#	 ENTÃO (Troque o HD/SDD)

# 5. SE (o computador liga 							= Sim)
#    E (A BIOS está iniciando 						= Sim)	
#    E (O Sistema Operacional inicia 				= Não)
#    E (A unidade de armazenamento é detectada 		= Sim)
#	 E (A ordem de boot está correta 				= Não)
#	 ENTÃO (Ajustar Boot)

# 6. SE (o computador liga 							= Sim)
#    E (A BIOS está iniciando 						= Sim)	
#    E (O Sistema Operacional inicia 				= Não)
#    E (A unidade de armazenamento é detectada 		= Não)
#	 ENTÃO (HD está desconectado ou com problema)

# 7. SE (o computador liga 							= Sim)
#    E (A BIOS está iniciando	 					= Não)
#	 E (O speaker emite alertas 					= Sim)
#	 ENTÃO (Problema na memória ou processador)

# 8. SE (o computador liga 							= Sim)
#    E (A BIOS está iniciando 						= Não)
#	 E (O speaker emite alertas 					= Não)
#	 ENTÃO (Problema na placa mãe)

# 9. SE (o computador não liga						= Não)
#	 E (A fonte inicia 								= Sim)
#	 E (A voltagem está correta 					= Sim)
#	 ENTÃO (Problema no circuito da Placa Mãe)

# 10. SE (o computador não liga 					= Não)
#	  E (A fonte inicia 							= Sim)
#	  E (A voltagem está correta 					= Não)
#	  ENTÃO (A fonte está com problema)

# 11. SE (o computador não liga 					= Não)
#	  E (A fonte inicia 							= Não)
#	  E (A alimentacao está conectada 				= Sim)
#	  ENTÃO (A fonte está queimada)

# 12. SE (o computador não liga 					= Não)
#	  E (A fonte inicia 							= Não)
#	  E (A alimentacao está conectada 				= Não)
#	  ENTÃO (Ligar na tomada)
