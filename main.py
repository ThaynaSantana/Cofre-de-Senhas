import random
from account import Account
from database.cofre import LOGINS
import re

# cadeia de caracteres para randomicamente gerar uma senha(segura)
chars = "qwertyuiopasdfghjklçzxcvbnm1234567890-=[~],.;!@#$%¨&*()_+^?:><"

# função para gerar senha(segura)
def generate_password(size):
    password=''
    # loop para criar uma senha do tamanho informado.
    for c in range(size):
        # acrescenta-se cada caracter da string chars para gerar uma senha(segura)
        password += random.choice(chars)
    return password

# função para registrar uma conta nova ao cofre
def register():
    print("############# Cadastro de um novo login ###############")
    name = str(input("Qual nome do site/aplicativo> "))
    email = str(input("E-mail> "))
    # se a validacao de email passar
    if validate_email(email):
        # solicita o tamanho da senha
        size = int(input("Qual a quantidade de caracteres voce deseja a sua senha> "))
        # gera a senha
        password = generate_password(size)
        # cria um objeto da classe Account de account.py
        one_account = Account(email,password)
        # cria um dicionario com as informações da conta
        new_account = {
            "nome": one_account.nome,
            "email": one_account.email,
            "senha": one_account.senha,
        }
        # adiciona no "database" de LOGINS que é um dicionario tambem
        LOGINS.append(new_account)
        print("Conta criada com sucesso.")
    else:
        print("email inválido.")
    
# função de login (testes)
def login(email):
    # pecorre todo o dicionario LOGINS
    for acc in LOGINS:
        # se email da conta for igual ao email informado
        if acc["email"] == email:
            # mostre na tela as informações :)
            print(f"Email: {acc['email']}")
            print(f"Passowrd: {acc['password']}")
        
# função para validação de um email
def validate_email(email):
    # padrão expressão regular de um email "nome@dm.com"
    default = r'^\S+@\S+\.\S+$'
    # com a lib "re" ele verifica se bate o padrão informado com o email digitado
    if re.match(default, email):
        return True
    else:
        return False
    
# função cria um cofre de senhas
def create_chest():
    # nome padronizado por mim
    name="cofre"
    password=str(input("Digite a password master do cofre: "))
    # cria um dicionario para inserir no "db" LOGINS
    master= {
        "name": name,
        "password": password,
    }
    LOGINS.append(master)
    print("Cofre criado com sucesso.")

# função fazendo login no cofre
def login_chest():
    password=str(input("Senha Master: "))
    # loooop em LOGINS
    for acc in LOGINS:
        # se o nome for igual a cofre
        if acc['name'] == "cofre":
            # se a senha digitada for igual a senha master
            if password == acc['password']:
                return True
            else:
                return False
            