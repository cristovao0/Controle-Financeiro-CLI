import funcoes
import formatacao


formatacao.cabeçalho('Menu')

while True:
    formatacao.menu(['Adicionar movimento', 'Lstar movimentos', 'Total de entradas', 'Total de saídas', 'Saldo atual', 'Resumo financeiro', 'Sair'])
    try:
        opcao = int(input('Digite uma opção '))
    except ValueError:
        print('Digite um número inteiro')
        continue
    except KeyboardInterrupt:
        print('Programa encerrado pelo usuário')
        print('Volte sempre')
        break
    else:
        if opcao == 1:
            data_operacao = str(input('Data da operação: ')).strip().lower()

            descricao = str(input('Descrição da operação: ')).strip().lower()

            try:
                valor = float(input('Digite o valor: '))
            except ValueError:
                print('Digite um valor válido')
            else:
                while valor < 0:
                    print('Digite um valor igual ou maior que zero')
                    valor = float(input('Digite o valor: '))

            tipo_operacao = str(input('Digite o tipo de operação: [entrada/saída]')).strip().lower()
                       
            while tipo_operacao not in ('entrada', 'saida', 'saída'):
                print('Digite uma opção válida.')
                tipo_operacao = str(input('Digite o tipo de operação: [entrada/saída]')).strip().lower()
                if tipo_operacao == 'saída':
                    tipo_operacao = 'saida'
            
            funcoes.adicionar_movimento(data_operacao, descricao, valor, tipo_operacao)

        elif opcao == 2:
            formatacao.cabeçalho('LISTAR MOVIMENTOS')
            funcoes.listar_movimento()

        elif opcao == 3:
            formatacao.cabeçalho('TOTAL DE ENTRADAS')
            funcoes.total_entradas()

        elif opcao == 4:
            formatacao.cabeçalho('TOTAL DE SAÍDAS')
            funcoes.total_saidas()

        elif opcao == 5:
            formatacao.cabeçalho('SEU SALDO')
            funcoes.calcular_saldo()
        
        elif opcao == 6:
            funcoes.resumo_financeiro()

        elif opcao == 7:
            print('Volte sempre!!!')
            break
        else:
            print('Escolha uma opção válida')
            continue
            
            
