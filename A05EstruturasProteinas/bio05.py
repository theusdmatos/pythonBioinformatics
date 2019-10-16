#proteinas, pensando nelas como sequencias
#vamos definir qual será a função de determinada proteina
# proteinas quando elas são formadas elas adotam uma conformação
# que define qual será a função daquela proteina, adquirando uma nova estrutura
# tridimensional que vai dizer qual sera a função daquela proteina

from Bio.PDB import * #esse modulo permite a manipulação de estruturas de proteinas 

#ele lê o arquivo.pdb de um estrutura tridmensional e converte
#em um objeto do tipo structer que vai analisar um determinada hierarquia
#que seria uma SMCRA (arquitetura), que le uma estrutura de proteina
#e converte em varias camadas permitindo navegar nessas camadas..

parser = PDBParser()
estrutura = parser.get_structure("1BGA", "/home/matos/Documentos/CursoPython_BioInformatica/A05EstruturasProteinas/1bga.pdb")

modelo = estrutura[0]#recebe a estrutura na posição 0
cadeiaA = modelo['A']#pegar o modelo na posição A
residuoCadeia100 = cadeiaA[100]#pegando residuo na cadeia na posição 100
carbonoAlfa = residuoCadeia100['CA']#pegando o atomo do residuo na posiao CA

#analisando os dados
#calcular a distancia euclidiana entre dois atomos
#calcula a distancia de dois carbono alfa

atomoPosicao101 = estrutura[0]['A'][101]['CA']#pode fazer tudo que foi feito acima em uma unica linha como essa 
atomoPosicao100 = estrutura[0]['A'][100]['CA']#igual o em cima linha 18

#distancia euclidiana
distancia = atomoPosicao101 - atomoPosicao100
print("A distancia Euclidiana é: " + str(distancia))


