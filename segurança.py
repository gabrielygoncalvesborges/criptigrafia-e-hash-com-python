import hashlib
import itertools

def calcula_hash_basico(senha):
    valor = 0
    for letra in senha:
        valor = valor + ord(letra)
    return valor

def calcula_hash_avancado(senha):
    valor = 0
    for letra in senha:
        valor = valor*31 + ord(letra)
    valor %= 2**32
    return f"{valor:08X}"

def calcula_hash_sha256(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def login_simulado():
    senha_cadastrada = "marcelo123"
    hash_cadastrado = calcula_hash_sha256(senha_cadastrada)
    senha_digitada = input("Digite sua senha: ")
    hash_digitada = calcula_hash_sha256(senha_digitada)
    if hash_digitada == hash_cadastrado:
        print("Acesso liberado")
    else:
        print("Acesso negado")

def forca_bruta():
    nova_senha = "abc"
    hash_nova = calcula_hash_sha256(nova_senha)
    dic_caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for combinacao in itertools.product(dic_caracteres, repeat=len(nova_senha)):
        senha_teste = ''.join(combinacao)
        hash_teste = calcula_hash_sha256(senha_teste)
        if hash_teste == hash_nova:
            print("Senha encontrada:", senha_teste)
            break

def criptografar(texto, chave):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            posicao = ord(letra.lower()) - ord('a')
            nova_posicao = (posicao + chave) % 26
            nova_letra = chr(ord('a') + nova_posicao)
            resultado += nova_letra
        else:
            resultado += letra
    return resultado

def dicionario_ascii():
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cripto = 'qwertyuiopasdfghjklzxcvbnm'
    dicionario = {}
    for i in range(len(alfabeto)):
        dicionario[alfabeto[i]] = cripto[i]
    senha = "marcelo"
    senha_criptografada = ""
    for letra in senha:
        senha_criptografada += dicionario[letra]
    print("Senha criptografada:", senha_criptografada)

if __name__ == "__main__":
    print("Hash básico:", calcula_hash_basico("marcelo123"))
    print("Hash avançado:", calcula_hash_avancado("Marcelo123!"))
    print("Hash SHA256:", calcula_hash_sha256("marcelo123"))
    # login_simulado()
    # forca_bruta()
    print("Criptografia simples:", criptografar("marcelo", 3))
    dicionario_ascii()
