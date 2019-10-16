#SEQUENCIA COMPLEMENTAR
from Bio.Seq import Seq #chamando a classe que permite analises código do BioPython

# não se pode declara como String, mas sim como objeto
minhaPrimeiraSequencia = Seq("ATG")

print(minhaPrimeiraSequencia)

# obtendo a sequencia complementar
seqComplementar = minhaPrimeiraSequencia.complement()
print(seqComplementar)

# obter tamebm a sequencia reversa complementar

seqComplementarReversa = minhaPrimeiraSequencia.reverse_complement
print(seqComplementarReversa)