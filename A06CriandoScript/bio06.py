
inputBio = open("/home/matos/Documentos/CursoPython_BioInformatica/A06CriandoScript/16s_bacteria.fasta").read()
outputBio = open("bacterium.html", "w") #salvar como html

count = {} #criar um dicionario
# cada par de nucleotido vale 0 
# quatro nucleotidos possivies

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        count[i+j] = 0
#cria um dicionario de 16 possições
#print(count) 

inputBio = inputBio.replace("\n", "") #pra tirar o erro de barra N
#fazendo a contagem
for k in range(len(inputBio)):
    count[inputBio[k]+inputBio[k+1]] += 1

print(count)