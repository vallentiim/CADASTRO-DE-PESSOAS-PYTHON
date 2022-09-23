def leiaINT(num):
    while True:
        try:
            n= int(input(num))
        except (ValueError, TypeError):
            print('TIVEMOS PROBELMAS COM OS VALORES DIGITADOS! TENTE NOVAMENTE')
            continue
        except (KeyboardInterrupt):
            print('O USUÁRIO PREFERIU NÃO INFORMAR O NÚMERO!')
            continue
        else:
            return n
def linha(tam=42):
    return '~'*tam
def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
def menu(lista):
    cabeçalho('\033[1;32mMENU PRINCIPAL\033[m')
    c=1
    for item in lista:
        print(f'\033[1;33m{c}\033[m ===> \033[1;34m{item}\033[m')
        c= (c+1)
    opc= leiaINT('==> SUA OPÇÃO: ')
    return opc