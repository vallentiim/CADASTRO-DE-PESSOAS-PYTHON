from modulos import interface

def arquivoEXISTE(nome):
    try:
        arq= open(nome, 'rt')
        arq.close()
    except (FileNotFoundError):
        return False
    else:
        return True
def criarARQUIVO(nome):
    try:
        arq= open(nome, 'wt+')
        arq.close()
    except:
        print('HOUVE UM ERRO AO CRIAR O ARQUIVO')
    else:
        print(f'ARQUIVO {nome} CRIADO COM SUCESSO!')
def lerARQUIVO(nome):
    try:
        arq= open(nome, 'rt')
    except:
        print(f'ERRO AO LER ARQUIVO {nome}')
    else:
        interface.cabeçalho('PESSOAS CADASTRADAS')
        for linha in arq:
            dados= linha.split(';')
            dados[1]= dados[1].replace('\n', '')
            print(f'{dados[0]:<30} {dados[1]:>3} anos')
    finally:
        arq.close()
def cadastrar(arq, nome= 'DESCONHECIDO', idade= 0):
    try:
        a= open(arq, 'at+')
    except:
        print('HOUVE UM ERRO NA ABERTURA DO ARQUIVO!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('HOUVE UM ERRO AO ADICIONAR AS INFORMAÇÕES!')
        else:
            print('INFORMAÇÕES ADICIONADAS')