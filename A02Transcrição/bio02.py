#efetuar o processo de transcrição
#onde esse processo é o processo de conversão de uma sequencia
#de dna em uma região codificante em uma sequencia de rna mensageiro

from Bio.Seq import Seq 

mySeq = Seq("ATG")

seqRNA = mySeq.transcribe()
print(seqRNA)

#retorna a sequencia para DNA (transcrição reversa)

setDNA = seqRNA.back_transcribe()
print(setDNA)