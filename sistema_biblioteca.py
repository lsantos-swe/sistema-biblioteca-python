import csv

#Realiza o cadastro de livros.
def cadastro_livros(livros):

    while True:
        while True:
            print(f"""{'_'*6} CADASTRAR LIVROS {'_'*6}""")
            codigo = input('Código:')

            if not codigo.isdigit():
                print('Digite apenas números.')
                continue

#Verifica se o código já foi cadastrado.
            elif codigo in livros:
                print('Código já cadastrado.\nDigite outro código.')

            else:
                break

        cad_titulo = input('Título:')
        cad_autor = input('Autor:')

        livros[codigo] = {
            'titulo': cad_titulo,
            'autor': cad_autor,
            'situacao': 'Disponível',
            'usuario': None,
            'matricula': None,
            'devolucao': None
}
        print("Livro cadastrado com sucesso!")

#Retorna ao menu de cadastrar livros ou ao menu principal.
        while True:
            novo_livro = input('Deseja cadastrar um novo livro? (S/N):').upper()

            if novo_livro == 'S':
                break

            elif novo_livro == 'N':
                print('Retornando ao menu principal...')
                return

            else:
                print('Opção inválida.\nDigite S ou N.')


#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________


#Realiza o cadastro de usuários.
def cadastro_usuarios(usuarios):

    while True:
        while True:
            print(f"""{'_'*5} CADASTRAR USUÁRIOS {'_'*5}""")
            matricula = input('Matrícula:')

            if not matricula.isdigit():
                print('Digite apenas números.')
                continue

#Verifica se o usuário já possui cadastro.
            elif matricula in usuarios:
                print('Usuário já cadastrado.\nDigite outro.')

            else:
                break

        nome_usuario = input('Nome do Usuário:')

        usuarios[matricula] = {
            'usuario': nome_usuario,
}

        print("Usuário cadastrado com sucesso!")

#Retorna ao menu de cadastrar usuários ou ao menu principal.
        while True:

            novo_usuario = input('Deseja cadastrar um novo usuário? (S/N):').upper()
            if novo_usuario == 'S':
                break

            elif novo_usuario == 'N':
                print('Retornando ao menu principal...')
                return

            else:
                print('Opção inválida.\nDigite S ou N.')


#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________


#Realizar o empréstimo dos livros disponíveis.
def emprestar_livro(livros, usuarios):

    while True:
        while True:
            print(f"""{'_'*5} REALIZAR EMPRÉSTIMO {'_'*5}""")
            pesquisar_livro = input('Digite o código do livro:')

            if not pesquisar_livro.isdigit():
                print('Digite apenas números.')
                continue

#Verifica se o livro existe na biblioteca.
            elif pesquisar_livro not in livros:
                print('Livro não encontrado. Tente novamente.')

#Verifica se o livro está disponível para empréstimo.
            elif livros[pesquisar_livro]['situacao'] == 'Emprestado':
                print(f"Livro '{livros[pesquisar_livro]['titulo']}' está emprestado.")
                while True:
                    novo_emprestimo = input('Deseja realizar um novo empréstimo? (S/N):').upper()
                    if novo_emprestimo == 'S':
                        break

                    elif novo_emprestimo == 'N':
                        print('Retornando ao menu principal...')
                        return

                    else:
                        print('Opção inválida.\nDigite S ou N.')

            else:
                print(f"Livro '{livros[pesquisar_livro]['titulo']}' está disponível para empréstimo!")
                break

        while True:
            matricula_usuario = input('Digite a matrícula:')

            if not matricula_usuario.isdigit():
                print('Digite apenas números.')
                continue

#Verifica se o aluno está cadastrado para realizar o empréstimo.
            elif matricula_usuario not in usuarios:
                print("Usuário não cadastrado.\nTente novamente ou retorne ao menu para realizar o cadastro")

            else:
                break

#Realiza a atualização do livro
        id_usuario = usuarios[matricula_usuario]['usuario']
        livros[pesquisar_livro]['situacao'] = 'Emprestado'
        livros[pesquisar_livro]['usuario'] = id_usuario
        livros[pesquisar_livro]['matricula'] = matricula_usuario
        livros[pesquisar_livro]['devolucao'] = input('Digite a data para devolução:')

        print('Empréstimo realizado com sucesso!')

#Retorna ao menu de empréstimo ou ao menu principal.
        while True:
            novo_empr = input('Deseja realizar outro empréstimo? (S/N):').upper()

            if novo_empr == 'S':
                break

            elif novo_empr == 'N':
                print('Retornando ao menu principal...')
                return

            else:
                print('Opção inválida.\nDigite S ou N.')


#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________


#Realiza a devolução dos livros emprestados.
def devolver_livro(livros):

    while True:
        print(f"""{'_'*5} REALIZAR DEVOLUÇÃO {'_'*5}""")
        devolucao_livro = input('Digite o código do livro a ser devolvido:')

        if not devolucao_livro.isdigit():
            print('Digite apenas números.')
            continue

#Verifica a existência do livro na biblioteca pelo código do livro.
        elif devolucao_livro not in livros:
            print('Livro não encontrado. Tente novamente.')
            continue

#Verifica se o livro está emprestado.
        elif livros[devolucao_livro]['situacao'] == 'Disponível':
            print(f"O livro '{livros[devolucao_livro]['titulo']}' já está disponível para empréstimo!")
            continue

        else:
            print(f"""Livro encontrado!

Título: {livros[devolucao_livro]['titulo']}
Autor: {livros[devolucao_livro]['autor']}
Usuário: {livros[devolucao_livro]['usuario']}
Matrícula: {livros[devolucao_livro]['matricula']}
Devolução: {livros[devolucao_livro]['devolucao']}
""")

#Confirma se o usuário realmente quer devolver o livro.
            while True:
                confirmar = input('Deseja confirmar a devolução? (S/N):').upper()

                if confirmar == 'S':

#Realiza a atualização do livro.
                    livros[devolucao_livro]['situacao'] = 'Disponível'
                    livros[devolucao_livro]['usuario'] = None
                    livros[devolucao_livro]['matricula'] = None
                    livros[devolucao_livro]['devolucao'] = None

                    print('Devolução realizada com sucesso!')
                    break

                elif confirmar == 'N':
                    print('Devolução cancelada!')
                    break

                else:
                    print('Opção inválida.\nDigite S ou N.')
                    continue

#Retorna ao menu de devolução ou ao menu principal.
        while True:

            nova_devolucao = input('Deseja devolver outro livro? (S/N):').upper()

            if nova_devolucao == 'S':
                break

            elif nova_devolucao == 'N':
                print('Retornando ao menu principal...')
                return

            else:
                print('Opção inválida.\nDigite S ou N.')


#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________


#Gerar relatórios
def gerar_relatorio(livros):

    while True:
        print(f"""
{'_'*6} GERAR RELATÓRIOS {'_'*6}

1. Relatório Completo
2. Relatório de Livros Emprestados
3. Relatório de Livros Disponíveis
4. Retornar ao MENU

{'_'*30}
""")

        opcao = input('Escolha uma opção:')

#Impede que o usuário digite letras.
        if not opcao.isdigit():
            print('Digite apenas números.')
            continue

#Gera o relatório completo.
        elif opcao == '1':
            print('\nRELATÓRIO COMPLETO\n')
            print(f'{'CÓDIGO':<8}{'TÍTULO':<30}{'AUTOR':<25}{'SITUAÇÃO':<13}{'USUÁRIO':<20}{'MATRÍCULA':<13}{'DEV. PREVISTA':<10}')

            for codigo in livros:

                livro_cod = livros[codigo]

                usuario = livro_cod['usuario'] or '-'
                matricula = livro_cod['matricula'] or '-'
                devolucao = livro_cod['devolucao'] or '-'

                print(f'{codigo:<8}{livro_cod['titulo']:<30}{livro_cod['autor']:<25}{livro_cod['situacao']:<13}{usuario:<20}{matricula:<13}{devolucao:<10}')

#Gera o relatório apenas de livros emprestados.
        elif opcao == '2':
            print('\nRELATÓRIO DE LIVROS EMPRESTADOS\n')
            print(f'{'CÓDIGO':<8}{'TÍTULO':<30}{'AUTOR':<25}{'SITUAÇÃO':<13}{'USUÁRIO':<20}{'MATRÍCULA':<13}{'DEV. PREVISTA':<10}')

            for codigo in livros:

                livro_cod = livros[codigo]

                if livro_cod['situacao'] == 'Emprestado':
                    print(f'{codigo:<8}{livro_cod['titulo']:<30}{livro_cod['autor']:<25}{livro_cod['situacao']:<13}{livro_cod['usuario']:<20}{livro_cod['matricula']:<13}{livro_cod['devolucao']:<10}')

#Gera o relatório apenas de livros disponíveis.
        elif opcao == '3':
            print('\nRELATÓRIO DE LIVROS DISPONÍVEIS\n')
            print(f'{'CÓDIGO':<8}{'TÍTULO':<30}{'AUTOR':<25}{'SITUAÇÃO':<13}{'USUÁRIO':<20}{'MATRÍCULA':<13}{'DEV. PREVISTA':<10}')

            for codigo in livros:
                livro_cod = livros[codigo]

                usuario = livro_cod['usuario'] or '-'
                matricula = livro_cod['matricula'] or '-'
                devolucao = livro_cod['devolucao'] or '-'

                if livro_cod['situacao'] == 'Disponível':
                    print(f'{codigo:<8}{livro_cod['titulo']:<30}{livro_cod['autor']:<25}{livro_cod['situacao']:<13}{usuario:<20}{matricula:<13}{devolucao:<10}')

#Retorna ao menu principal.
        elif opcao == '4':
            print('Retornando ao menu principal...')
            return

        else:
            print('Opção inválida')
            continue

#Retorna ao menu relatório ou ao menu principal.
        while True:
            novo_relatorio = input('Deseja gerar outro relatório? (S/N):').upper()

            if novo_relatorio == 'S':
                break

            elif novo_relatorio == 'N':
                print('Retornando ao menu principal...')
                return

            else:
                print('Opção inválida.\nDigite S ou N.')


#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________


#Salva os relatórios em csv.
def salvar_csv(livros):

    while True:
        print(f"""
{'_'*9} RELATÓRIOS {'_'*9}

1. Salvar - Relatório Completo
2. Salvar - Relatório de Livros Emprestados
3. Salvar - Relatório de Livros Disponíveis
4. Retornar ao MENU

{'_'*30}
""")
        opcao = input('Escolha uma opção:')

#Impede que o usuário utilize letras e outros caracteres.
        if not opcao.isdigit():
            print('Digite apenas números.')
            continue

#Retorna ao menu principal.
        elif opcao == '4':
            print('Retornando ao MENU...')
            return

#Impede que o usuário utilize outras opções além das incluídas no menu.
        elif opcao not in ['1', '2', '3', '4']:
            print('Opção inválida. Digite uma das opções: 1, 2, 3, ou 4:')
            continue

        else:
            arq_nome = input('Digite o nome do arquivo: ')
            with open(f'{arq_nome}.csv',  'w', newline = '', encoding = 'utf-8') as arquivo:

                arq_relatorio = csv.writer(arquivo, delimiter = ';')

                arq_relatorio.writerow([
                    'codigo',
                    'titulo',
                    'autor',
                    'situacao',
                    'usuario',
                    'matricula',
                    'devolucao'
                ])

                for codigo in livros:
                    livro = livros[codigo]

                    if opcao == '2' and livro['situacao'] != 'Emprestado':
                        continue

                    elif opcao == '3' and livro['situacao'] != 'Disponível':
                        continue

                    usuario = livro['usuario'] or '-'
                    matricula = livro['matricula'] or '-'
                    devolucao = livro['devolucao'] or '-'

                    arq_relatorio.writerow([
                        codigo,
                        livro['titulo'],
                        livro['autor'],
                        livro['situacao'],
                        usuario,
                        matricula,
                        devolucao
                    ])
        print('Arquivo salvo com sucesso!')

#Retorna ao menu salvar_csv ou ao menu principal.
        while True:
            novo_arq = input('Deseja salvar outro relatório? (S/N):').upper()

            if novo_arq == 'S':
                break

            elif novo_arq == 'N':
                print('Retornando ao menu principal...')
                return
            else:
                print('Opção inválida.\nDigite S ou N.')


#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________


#Menu principal da biblioteca
def menu():
    livros = {}
    usuarios = {}


    while True:

        print(f"""
{'_'*9} BIBLIOTECA {'_'*9}

1. Cadastrar Livro
2. Cadastrar Usuário
3. Realizar Empréstimo
4. Realizar Devolução
5. Gerar Relatórios
6. Salvar Relatórios CSV
7. Sair

{'_'*30}
""")

        opcao = input('Escolha uma opção: ')

#Impede que o usuário utilize letras e outros caracteres.
        if not opcao.isdigit():
            print('Digite apenas números.')
            continue

        elif opcao == '1':
            cadastro_livros(livros)

        elif opcao == '2':
            cadastro_usuarios(usuarios)

        elif opcao == '3':
            emprestar_livro(livros, usuarios)

        elif opcao == '4':
            devolver_livro(livros)

        elif opcao == '5':
            gerar_relatorio(livros)

        elif opcao == '6':
            salvar_csv(livros)

        elif opcao == '7':
            print('Encerrando...')
            break
#Caso o usuário digite outra opção além das incluídas no menu.
        else:
            print('Opção inválida. Digite uma das opções: 1, 2, 3, 4, 5, 6 ou 7.')


#_______________________________________________________________________________________________________
#_______________________________________________________________________________________________________


if __name__ == "__main__":
    menu()