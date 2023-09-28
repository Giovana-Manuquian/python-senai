print('*******************************************************************************')
nome = input('Seja bem vindo(a)! Digite seu nome: ')

n1 = "Tite"
n2 = "Mano Menezes"
n3 = "Vitor Pereira"
n4 = "Abel"

print(f'Selecione a opção com o nome do técnico que deseja para comandar o time do Corinthians:\n'
      f'1- {n1}\n'
      f'2- {n2}\n'
      f'3- {n3}\n'
      f'4- {n4}\n'
      '5- Sair\n')

continuar = True

while continuar:
    opcao = int(input('Escolha uma opção (1-5): '))

    if opcao == 1:
        print("Unica escolha certa")
        break;
    elif opcao == 2:
        print("Tá ficando maluco(a) é?!")
        break;
    elif opcao == 3:
        print("Com certeza a melhor escolha em!")
        break;
    elif opcao == 4:
        print("Aí você sonha grande em!")
        break;
    elif opcao == 5:
        continuar = False
        break;
    else:
        print("Opção inválida!")
        break;

print("Você saiu do programa.")
print('*******************************************************************************')
