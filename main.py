import funcoes
import formatacao
import ControleFinanceiro


formatacao.cabeçalho('Menu')
ct = ControleFinanceiro.ControleFinanceiro(r'Controle Financeiro\Controle-Financeiro-CLI\movimentos.json')
while True:
    
    formatacao.menu(['Adicionar movimento', 'Listar movimentos', 'Total de entradas', 'Total de saídas', 'Saldo atual', 'Resumo financeiro', 'Sair'])
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
            
            ct.adicionar_movimento(data_operacao, descricao, valor, tipo_operacao)

        elif opcao == 2:
            formatacao.cabeçalho('LISTAR MOVIMENTOS')
            ct.listar_movimentos()

        elif opcao == 3:
            formatacao.cabeçalho('TOTAL DE ENTRADAS')
            total = ct.total_entradas()
            print(f"Total de entradas: R$ {total:.2f}")

        elif opcao == 4:
            formatacao.cabeçalho('TOTAL DE SAÍDAS')
            total = ct.total_saidas()
            print(f"Total de saidas: R$ {total:.2f}")

        elif opcao == 5:
            formatacao.cabeçalho('SEU SALDO')
            saldo = ct.calcular_saldo()
            print(f"Saldo: R$ {saldo:.2f}")
        
        elif opcao == 6:
            resumo = ct.resumo_financeiro()
            print('\033[7mRESUMO FINANCEIRO\033[m')
            print(f"Total de entradas: \033[34m{resumo['entradas']:>15.2f}\033[m")
            print(f"Total de saídas: \033[34m{resumo['saidas']:>17.2f}\033[m")

            if resumo['saldo'] >= 0:
                print(f"Saldo: \033[32m{resumo['saldo']:>27.2f}\033[m")
            else:
                print(f"Saldo: \033[31m{resumo['saldo']:>27.2f}\033[m")

        elif opcao == 7:
            print('Volte sempre!!!')
            break
        else:
            print('Escolha uma opção válida')
            continue
            
            
