import getpass
class Cliente:
    def __init__(self, conta):
        self.conta = conta

    def menu_conta(self):
        if not self.autenticar_cliente():
            print("\nAcesso negado. Certifique-se de fornecer as informações corretas.")
            return

        while True:
            print("="*30)
            print(f"Bem-vindo, {self.conta.nome}!")
            print("Número da conta:", self.conta.numero_conta)
            print("="*30)
            print("1. Verificar Saldo")
            print("2. Sacar")
            print("3. Sair")
            print("="*30)

            escolha = input("Escolha uma opção (1-3): ")

            if escolha == '1':
                self.verificar_saldo()
            elif escolha == '2':
                self.sacar()
            elif escolha == '3':
                print("\nObrigado por usar nosso ATM. Até logo!")
                break
            else:
                print("\nOpção inválida. Tente novamente.")

    def autenticar_cliente(self):
        senha = getpass.getpass("Digite sua senha: ").strip()
        return senha == self.conta.senha

    def verificar_saldo(self):
        print("="*30)
        print("Verificar Saldo")
        print("="*30)
        print(f"Seu saldo atual é: R${self.conta.saldo:.2f}")

    def sacar(self):
        valor_str = input("\nDigite o valor a sacar : R$").strip()

        try:
            valor = float(valor_str)
        except ValueError:
            print("\nPor favor, insira um valor válido.")
            return

        if 0 < valor <= self.conta.saldo:
            self.conta.saldo -= valor
            print(f"\nSaque de R${valor:.2f} realizado com sucesso.")
        else:
            print("\nSaldo insuficiente ou valor inválido.")