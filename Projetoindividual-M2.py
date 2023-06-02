def buscar_candidatos(notamin_entrevista=5, notamin_teste_teórico=5, notamin_teste_prático=5, notamin_soft_skills=5):
  # Função para buscar candidatos com notas mínimas específicas   
    
    candidatos_selecionados = [] # Lista para armazenar os candidatos selecionados
    
    
    for candidato in candidatos:
        nome = candidato["nome"]   # Obtém o nome do candidato
        notas = candidato["notas"].split("_")[1:] # Obtém as notas do candidato, excluindo o prefixo "e", "t", "p", "s"
        notas_int = [int(nota[1:]) for nota in notas]   # Converte as notas em inteiros
        
         # Verifica se todas as notas do candidato são maiores ou iguais às notas mínimas especificadas
        if all(nota >= notamin for nota, notamin in zip(notas_int, [notamin_entrevista, notamin_teste_teórico, notamin_teste_prático, notamin_soft_skills])):
            candidatos_selecionados.append(nome)   # Adiciona o nome do candidato à lista de candidatos selecionados
            
    return candidatos_selecionados # Retorna a lista de candidatos selecionados

  
#Lista de candidatos      
candidatos = [{"nome": "João", "notas": "e4_t5_p7_s6"},
             {"nome": "Maria", "notas": "e5_t6_p8_s9"},
             {"nome": "Pedro", "notas": "e3_t4_p6_s7"},
             {"nome": "Ana", "notas": "e6_t7_p9_s8"},
             {"nome": "Carlos", "notas": "e4_t4_p8_s8"},
             {"nome": "Mariana", "notas": "e7_t8_p9_s9"},]

try:  # Solicita as notas mínimas ao usuário
    notamin_entrevista = int(input("Digite a nota mínima para Entrevista: "))
    notamin_teste_teórico = int(input("Digite a nota mínima para Teste Teórico: "))
    notamin_teste_prático = int(input("Digite a nota mínima para Teste Prático: "))
    notamin_soft_skills = int(input("Digite a nota mínima para avaliação de Soft Skills: "))
     
    # Chama a função passando as notas mínimas como argumentos 
    resultados = buscar_candidatos(notamin_entrevista, notamin_teste_teórico, notamin_teste_prático, notamin_soft_skills)

    print("Os candidatos que atendem as notas mínimas exigidas são:") #Imprime os candidatos que atendem as notas mínimas exigidas.
    if resultados:  #Verifica se a lista de resultados não está vazia. Se houver candidatos que atendam aos critérios, a condição será avaliada como verdadeira e o bloco de código abaixo será executado.
        for candidato in resultados: #Itera sobre cada candidato na lista de resultados.
         print(candidato)  # Imprime o nome do candidato selecionado
            
    else:  #Este bloco é executado quando nenhum candidato atende aos critérios das notas mínimas especificadas.
         print("Nenhum candidato atende aos critérios mínimos.")
    
except ValueError: #Este bloco de código captura a exceção que pode ocorrer caso haja uma entrada inválida.
    print("Entrada inválida. Certifique-se de inserir apenas valores numéricos para as notas mínimas.")
    




            
        
        