import random

class Account:
    def __init__(self, email, password):
        self.nome = ''
        self.icon = ''
        self.email = email
        self.password = password
        
    def setNome(self, nome):
        self.nome = nome
    
    def setIcon(self, icon):
        self.icon = icon

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password

    def codeGeneration():
        code=''
        chars = "1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pç"
        for c in range(8):
            code += random.choice(chars)
        return code