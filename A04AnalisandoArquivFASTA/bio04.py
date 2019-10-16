#analisar sequencias no formato fasta 
#criar um arquivo FASTA

from Bio import SeqIO #classe que faz analise de sequencias

#laco que vai ler todo arquivo de sequencias

for fasta in SeqIO.parse("/home/matos/Documentos/CursoPython_BioInformatica/A04AnalisandoArquivFASTA/mySEQ.fasta", "fasta"):
    print(fasta.id) #aqui pega o ID do arquivo
    print(fasta.seq)

