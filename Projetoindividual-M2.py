def buscar_candidatos(notamin_e=5, notamin_t=5, notamin_p=5, notamin_s=5):
    candidatos_selecionados = []
    
    for candidato in candidatos:
        nome = candidato["nome"]
        notas = candidato["notas"].split("_")[1:]
        notas_int = [int(nota[1:]) for nota in notas]
        
        if all(nota >= notamin for nota, notamin in zip(notas_int, [notamin_e, notamin_t, notamin_p, notamin_s])):
            candidatos_selecionados.append(nome)
            return candidatos_selecionados
        
candidatos = [{"nome": "João", "notas": "e4_t5_p7_s6"},
             {"nome": "Maria", "notas": "e5_t6_p8_s9"},
             {"nome": "Pedro", "notas": "e3_t4_p6_s7"},
             {"nome": "Ana", "notas": "e6_t7_p9_s8"},
             {"nome": "Carlos", "notas": "e4_t4_p8_s8"},
             {"nome": "Mariana", "notas": "e7_t8_p9_s9"},]

notamin_e = int(input("Digite a nota mínima para entrevista: "))
notamin_t = int(input("Digite a nota mínima para teste teórico: "))
notamin_p = int(input("Digite a nota mínima para teste prático: "))
notamin_s = int(input("Digite a nota mínima para avaliação de soft skills: "))

resultados = buscar_candidatos(notamin_e, notamin_t, notamin_p, notamin_s)
print("Candidatos selecionados:")
if resultados:
    for candidato in resultados:
        print(candidato)
else:
    print("Nenhum candidato atende aos critérios.")
    
    
    

            
        
        