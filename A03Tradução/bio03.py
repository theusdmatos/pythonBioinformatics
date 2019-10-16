#reproduzindo processo de tradução
from Bio.Seq import Seq
mySeq = Seq("ATG")

#traduzir uma sequencia de rna mensageiro em uma sequencia de proteinas

#transcrição
seqRNA = mySeq.transcribe()
seqDNA = mySeq.back_transcribe()

#tradução
seqProteineRNA = seqRNA.translate()
print(seqProteineRNA)

seqProteineDNA = seqDNA.translate()
print(seqProteineDNA)

