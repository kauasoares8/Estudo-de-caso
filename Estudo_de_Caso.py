# a logica por tras do codigo e simples, tinha que definir se os servidores eram elegiveis pra se aposentar ou nao entao eu resolvi usar uma função 
# pra me dizer isso com o if elif e else,e depois foi so impor as condiçoes passadas no escopo e definir o retorno de acordo com o caso, o resto era so referenciar 
# com os dados ja existentes sendo eles o nome, sexo e idade.


#importando a biblioteca pandas e usando um alias "pd" pra mudar o nome da referencia das funções
import pandas as pd 

#criação da variavel "dataframe" que vai receber a planilha "Estudo de caso" como valor, que no caso e a planilha que me foi enviada
dataframe = pd.read_excel('./Estudo_De_Caso.xlsx', sheet_name='Servidores')#Estudo_De_Caso.xlsx e o nome do meu arquivo do excel

#definindo a função pra validar se o servidor em questao esta elegivel para ser aposentado ou nao, a condição para ser elegivel e +60 anos para as pessoas do genero feminino e +65 para as do genero
#masculino
def is_aposentavel(i):
    if i['codsexo'] == 'F' and i['datanascimento'] <= pd.to_datetime('today') - pd.DateOffset(years=60):
        return ('Aposentavel')
    #aqui ele analisa qual e o codsexo, se for 'F' e a tiver mais de 60 anos vai retornar ('aposentavel')
    elif i['codsexo'] == 'M' and i['datanascimento'] <= pd.to_datetime('today') - pd.DateOffset(years=65):
        return('Aposentavel')
    # e se o codsex for 'M' e tiver mais de 65 anos ele tambem ira retornar ('aposentavel')
    else:
        return('Nao aposentavel')
    #caso uma ou nenhuma das condiçoes nao seja atendida vai ser retornado ('Nao aposentavel')
    
#a linha 21 cria uma nova coluna que e anexada a planilha "Estudo de caso" pra ser adcionada no novo dataframe
dataframe['Aposentável'] = dataframe.apply(is_aposentavel, axis=1)
#a linha23 cria um novo dataframe com o nome dataframe_aposentavel com base no Estudo_De_Caso usando as colunas nome, codsexo etc
dataframe_aposentavel = dataframe[['nome', 'codsexo', 'datanascimento', 'Aposentável']]
#a linha 25 converte o novo dataframe criado em um arquivo xlsx
dataframe_aposentavel.to_excel('./Dataframe_Aposentavel.xlsx', index =False)#Dataframe_Aposentavel o nome do arquivo excel criado