""""Código em Python (70 pts):

Menu com opções como:

Tirar dúvidas via Chatbot (simulado),

Realizar agendamento,

Simular reconhecimento facial,


Visualizar histórico,

Sair"""
import os

consultas = []
def finalizar_app():
    os.system("cls")
    print("finalizando app\n")

def exibir_nome_do_programa():
    print("bem vindo a o menu do app de queda de absenteismo")


def opcao_invalida():
    print("opção invalida\n")
    input("digite uma tecla para voltar a o menu")
    main()

def marcar_consultas():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== Marcar Consulta ===")
    
    nome = input("Digite seu nome completo: ")
    dia = input("Digite o dia que deseja marcar a consulta: ")

    for consulta in consultas:
        if consulta["dia"] == dia:
            print("Essa data já está ocupada. Tente outro horário.")
            input("Pressione Enter para voltar ao menu...")
            return

    consultas.append({"nome": nome, "dia": dia})
    print("Consulta marcada com sucesso!")
    input("Pressione Enter para voltar ao menu...")


def exibir_opcoes():
    print("1 tirar duvidas via chatbot(no futuro vai ficar o link do nosso chatbot)")
    print("2 realizar agendamento")
    print("3 simular reconhecimento facial(vai levar pro nosso reconhecimento facial)")
    print("4 mostrar consultas marcadas")
    print("5 sair")


def escolher_opcoes():
        try:
            opção_escolhida = int(input("escolha uma opção: "))
            if opção_escolhida == 1: print("link do nosso chatbot")
            elif opção_escolhida == 2:marcar_consultas()
            elif opção_escolhida == 3:  print("link do reconhecimento facial")
            elif opção_escolhida == 4: print("mostrar as consultas marcadas")
            elif opção_escolhida == 5: finalizar_app()
            else: opcao_invalida()
        except: opcao_invalida()
    


def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
   

if __name__ == "__main__":
    main()




    