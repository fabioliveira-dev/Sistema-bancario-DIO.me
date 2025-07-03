from time import sleep

# Sistema bancario v1.0

saldo = saque = deposito = 0.0

print('Bem vindo ao seu banco')
sleep(1)
while True:
    print('Escolha qual operação deseja realizar:')
    print('-' * 40)
    print('''\t[1] Saque:
    [2] Deposito:
    [3] Extrato:
    [4] SAIR:''')
    print('-' * 40)
    try:
        opcao = int(input('Opção: '))
        sleep(1)
        if opcao <=0 or opcao > 4:
            print(f'Opção {opcao} invalida!')
        elif opcao == 1:
            print('SAQUE:')
            saque = float(input('Qual valor deseja sacar R$: '))
            while True:
                try:
                    if saldo == 0:
                        print('Sua conta esta sem fundos! Faça um deposito.')
                        sleep(1)
                        break
                    elif saldo < saque:
                        print('O valor de saque é maior que o saldo disponivel!')
                        saque = float(input('Qual valor deseja sacar R$: '))
                        sleep(1)
                    else:
                        saldo = saldo - saque
                        print('Contando cédulas.')
                        sleep(1)
                        print('Finalizando...')
                        sleep(1)
                        print(f'Saque efetuado com sucesso no valor de R${saque:.2f} reais.')
                        sleep(1)
                        break
                except:
                    print('ERRO! valor incorreto.')

        elif opcao == 2:
            print('DEPOSITO:')
            try:
                deposito = float(input('Digite o valor de deposito R$: '))
                sleep(1)
                if deposito > 0:
                    saldo = deposito + saldo
                    print('Finalizando...')
                    sleep(1)
                    print('Deposito efetuado com sucesso!')
                    sleep(1)
                    print(f'Seu novo saldo é R$: {saldo:.2f}')
                    sleep(1)
                else:
                    print('Operação falhou! O valor do depósito deve ser positivo.')
                    sleep(1)
            except ValueError:
                print('ERRO! Digite um valor numérico válido para o depósito (ex: 100 ou 50.50).')
                sleep(1)
            except Exception as e:
                print(f'Ocorreu um erro inesperado: {e}')
                sleep(1)

        elif opcao == 3:
            print('EXTRATO:')
            sleep(1)
            print('Gerando Extrato...')
            sleep(1)
            print('Finalizando...')
            sleep(1)
            print(f'EXTRATO: R${saldo:.2f}')
            sleep(1)

        elif opcao == 4:
            break

    except:
        print('Digite uma opção valida!')


print('Obrigado por usar nosso banco!')
sleep(1)