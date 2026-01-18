def linhas():
    print('-=' * 30)


def cabeçalho(texto):
    linhas()
    print(f'{texto:^50}')
    linhas()


def menu(opcoes):
    for indice, conteudo in enumerate(opcoes):
        print(f'{indice + 1} - {conteudo}')