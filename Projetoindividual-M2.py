def buscar_candidatos(notamin_e=5, notamin_t=5, notamin_p=5, notamin_s=5):
    candidatos_selecionados = []
    
    for candidato in candidatos:
        nome = candidato["nome"]
        notas = candidato["notas"].split("_")[1:]
        notas_int = [int(nota[1:]) for nota in notas]
        
        if all(nota >= notamin for nota, notamin in zip(notas_int, [notamin_e, notamin_t, notamin_p, notamin_s])):
            candidatos_selecionados.append(nome)
            return candidatos_selecionados