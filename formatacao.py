def linhas():
    print('-=' * 30)


def cabeçalho(texto):
    linhas()
    print(f'{texto:^50}')
    linhas()


def menu(opcoes):
    for indice, conteudo in enumerate(opcoes):
        print(f'\033[33m{indice + 1}\033[m - \033[34m{conteudo}\033[m')