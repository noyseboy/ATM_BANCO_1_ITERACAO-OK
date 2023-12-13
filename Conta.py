import random
import getpass

class Conta:
    def __init__(self, nome, cpf, numero_conta, saldo=100.0):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.senha = None

    def cadastrar_senha(self, senha):
        self.senha = senha
        print("\nSenha cadastrada com sucesso.")

    def digitar_senha(self):
        return getpass.getpass("Digite sua senha: ").strip()

class Administrador:
    def __init__(self):
        self.nome_usuario = ""
        self.senha = ""
        self.contas = []

    def criar_usuario_senha(self):
        print("="*30)
        print("Criar Usuário e Senha do Administrador")
        print("="*30)
        self.nome_usuario = input("Digite o nome de usuário para o administrador: ").strip()
        self.senha = getpass.getpass("Digite a senha para o administrador: ").strip()
        print("\nUsuário e senha do administrador criados com sucesso.")

    def autenticar_admin(self):
        print("="*30)
        print("Bem-vindo ao ATM Banco!")
        print("="*30)
        nome_usuario = input("Digite o nome de usuário: ").strip()
        senha = getpass.getpass("Digite a senha: ").strip()
        return nome_usuario == self.nome_usuario and senha == self.senha

    def criar_conta(self):
        print("="*30)
        print("Criar Nova Conta")
        print("="*30)
        nome = input("Digite o nome do cliente: ").strip()
        cpf = input("Digite o CPF do cliente (apenas números, 11 dígitos): ").strip()

        for conta in self.contas:
            if conta.cpf == cpf:
                print("\nJá existe uma conta registrada com este CPF.")
                return

        numero_conta = self.gerar_numero_conta()
        nova_conta = Conta(nome, cpf, numero_conta)
        senha = getpass.getpass("Digite a senha para a conta: ").strip()
        nova_conta.cadastrar_senha(senha)
        self.contas.append(nova_conta)

        print("\nConta criada com sucesso!")
        print(f"O número da conta para {nome} é: {numero_conta}")

    def gerar_numero_conta(self):
        return str(random.randint(100000, 999999))