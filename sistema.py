from modulos import arquivo, interface

arq= 'pessoas.txt'
if not arquivo.arquivoEXISTE(arq):
    arquivo.criarARQUIVO(arq)

while True:
    resposta= interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova  pessoa', 'Sair do programa'])
    if (resposta==1):
        arquivo.lerARQUIVO(arq)
    elif (resposta==2):
        nome= str(input('==> INFORME O NOME QUE DESEJA CADASTRARA: '))
        idade= interface.leiaINT('==> INFORME A IDADE QUE DESEJA CADASTRAR: ')
        arquivo.cadastrar(arq, nome, idade)
    elif (resposta==3):
        interface.cabeçalho('Saindo do sistema...')
        break
    else:
        print('INFORME UMA OPÇÃO VÁLIDA!')
        continue 
    print()