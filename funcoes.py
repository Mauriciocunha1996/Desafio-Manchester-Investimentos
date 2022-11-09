import pandas as pd
import time
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')




class BancoDeDados:
    def __init__(self, arquivo):
        """Função chamada toda vez que um objeto é criado a partir de uma classe.

        Args:
            arquivo: recebe o arquivo que irei usar como base de dados para o código
            self.df_sem_duplicatas: variável que remove as duplicatas da tabela e mostrar a tabela sem essas duplicatas
        """
        self.dataFrame = pd.read_excel(arquivo) #lendo o arquivo excel Base_de_dados
        self.df_sem_duplicatas = self.dataFrame.drop_duplicates(subset=['codigo_cliente', 'nome_cliente', 'idade', 'filial', 'custodia'])
        self.linha()
        print(self.df_sem_duplicatas)
        self.linha()   
        
        
    def linha(self):
        """Função apenas para traçar uma linha para separar as respostas
        """
        print("="*80)
          
          
          
          
          
    def listar_quantidade_de_clientes(self, coluna):
        """Função para listar a quantidade de clientes na minha base de dados
        
        Args:
            coluna (int): este parâmetro recebe a coluna que desejo analisar

        Returns:
            (int): retorna a variável quantidade_de_clientes que armazena o valor exato da quantidade de clientes da minha base de dados
        """
        quantidade_de_clientes = self.df_sem_duplicatas [coluna].count()
        return quantidade_de_clientes

    
    
    
    def custodia_total(self, coluna):
        """Função para calcular o valor total da minha coluna

        Args:
            coluna (int): este parâmetro recebe a coluna que desejo analisar

        Returns:
            sum(): função adiciona os itens de um iterável e retorna a soma.
            (int): retorna a variável self.custototal que armazena a soma de todos os valores do paramêtro coluna
        """
        self.custototal = self.df_sem_duplicatas[coluna].sum()
        return self.custototal
    
    
    
    def custodia_media(self, coluna):
        """Função para calcular o valor da média da coluna custodia

        Args:
            coluna (int): este parâmetro recebe a coluna que desejo analisar

        Returns:
            median() usada para calcular o valor mediano de uma lista de dados não classificada
            (float): retorna a variável self.custo_medio que armazena a média dos valores da coluna que analisei.
        """
        self.custo_medio = self.df_sem_duplicatas[coluna].median()
        return self.custo_medio
    
    
    
    
    def media_de_idade(self, coluna):
        """Função para analisar a média das idades da minha base de dados que estou trabalhando

        Args:
            coluna (int): este parâmetro recebe a coluna que desejo analisar

        Returns:
            (float): retorna a variável self.media_de_idade que armazena a media das idades da coluna que recebi atraves do parametro coluna
        """
        self.media_idade = self.df_sem_duplicatas[coluna].median()
        return self.media_de_idade
    
    
    
    
    def quantidade_de_assessores(self, coluna):
        """Função para analisar a quantidade de assessores da minha base de dados

        Args:
            coluna (str): este parâmetro recebe a coluna que desejo analisar

        Returns:
            int : retorna a variável qtd_de_acessores que armazena a quantidade exata de acessores que tenho na minha base de dados
        """
        self.sem_duplicatas1 = self.dataFrame.drop_duplicates(subset=[coluna])
        qtd_de_acessores = self.sem_duplicatas1[coluna].count()
        return qtd_de_acessores
    
    
    
    
    def custodia_total_por_assessor(self, col1, col2):
        """Função para retornar a tabela com os acessores e custódia total de cada um deles

        Args:
            col1 (str): este parâmetro recebe a coluna que desejo analisar
            col2 (int): este parâmetro recebe a coluna que desejo analisar
            nova_df: variável é meu data frame sem duplicatas dos acessores
            tabela_custodia: variável armazena o data frame dos valores de cada acessor passando para moeda local
        Returns:
            juncao: variável a concatenação das minhas tabelas novo_df e tabela_custodia. Onde essa data freme mostar o valor da custodia total de cada acessor
        """
        df = self.dataFrame
        novo_df = df.groupby([col1])[col2].sum().reset_index()
        tabela_custodia = novo_df['custodia'].apply(lambda x: f"{locale.currency(x, grouping=True)}")
        juncao = pd.concat([novo_df[col1], tabela_custodia], axis=1)
        return juncao
        
    
    
    def menu(self):
        """Função que escreve na tela um menu para o usuário da informações que meu código oferece
        """
        print('Escolha a opção desejada: ')
        print('[1] Quantidade de clientes diferentes na base de dados?')
        print('[2] Qual é custodia total?')
        print('[3] Qual a custodia media?')
        print('[4] Qual a media de idade de todos os clientes?')
        print('[5] Qual é a quantidade de assessores?')
        print('[6] Qual a custódia total por assessor?')
        print('[0] Desejo sair ')

    
    
    
    
    def opcoes(self):
        """Função que armazena as opções escolhidas atráves do menu

        Raises:
            ValueError: caso o valor digitado pelo usuário seja diferente das opções dadas retorna
            erro e a dá a opção de escolher novamente.
        """
        while True:
            self.menu()
            try:
                opcao = int(input('Opção Desejada: '))
                if not 0 <= opcao <= 6:
                    self.linha()
                    raise ValueError("Escolha a opção correta")
            except ValueError as e:
                
                print("Valor inválido:", e)
                self.linha()
                continue
            
            while opcao != 0:
                if opcao == 1:
                    resposta1 = self.listar_quantidade_de_clientes("codigo_cliente")
                    self.linha()
                    print(f'Quantidade de clientes diferentes na base de dados: {resposta1}\n')
                    self.linha()
                    break
                
                elif opcao == 2:
                     resposta2 = self.custodia_total('custodia')
                     self.linha()
                     print(f'Custodia total: {locale.currency(resposta2, grouping=True)}')
                     self.linha()
                     break
                 
                elif opcao == 3:
                    resposta3 = self.custodia_media('custodia')
                    self.linha()
                    print(f'Custodia média: {locale.currency(resposta3, grouping=True)}')
                    self.linha()
                    break
                
                elif opcao == 4:
                    resposta4 = self.custodia_media('idade')
                    self.linha()
                    print(f'Media de idade de todos os clientes: {resposta4} anos')
                    self.linha()
                    break
                
                elif opcao == 5:
                    resposta5 = self.quantidade_de_assessores('codigo_assessor')
                    self.linha()
                    print(f'Quantidade de assessores: {resposta5}')
                    self.linha()
                    break
                
                elif opcao == 6:
                    resposta6 = self.custodia_total_por_assessor("codigo_assessor", 'custodia')
                    self.linha()
                    print(resposta6)
                    self.linha()
                    break
                
            if opcao == 0:
                time.sleep(0.5)
                self.linha()
                print("Promaga Encerrado!!!")
                self.linha()
                break

    
    