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

def marcar_consultas():
    os.system("cls")
    print("=== Marcar Consulta ===")
    
    nome = input("Digite seu nome completo: ")
    dia = input("Digite o dia que deseja marcar a consulta (formato DD/MM): ")

    try:
        partes = dia.split("/")
        dia_num = int(partes[0])
        mes_num = int(partes[1])
        if dia_num < 1 or dia_num > 31 or mes_num < 1 or mes_num > 12:
            print("Data inválida! Dia ou mês fora do intervalo permitido.")
            input("Pressione Enter para voltar ao menu...")
            main()
            return
    except:
        print("Formato de data inválido. Use o formato DD/MM.")
        input("Pressione Enter para voltar ao menu...")
        return

    for consulta in consultas:
        if consulta["dia"] == dia:
            print("Essa data já está ocupada. Tente outro horário.")
            input("Pressione Enter para voltar ao menu...")
            main()
            return

    consultas.append({"nome": nome, "dia": dia})
    print("Consulta marcada com sucesso!")
    input("Pressione Enter para voltar ao menu...")
    





def mostrar_consultas():
    os.system("cls")
    print("=== Consultas Marcadas ===")
    if not consultas:
        print("Nenhuma consulta marcada.")
    else:
        for i, consulta in enumerate(consultas, start=1):
            print(f"{i}. Nome: {consulta['nome']} | Dia: {consulta['dia']}")
    input("\nPressione Enter para voltar ao menu...")
    

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
            elif opção_escolhida == 4: mostrar_consultas()
            elif opção_escolhida == 5: finalizar_app()
            else: opcao_invalida()
        except: opcao_invalida()
    


def main():
    while True:
        os.system("cls")
        exibir_nome_do_programa()
        exibir_opcoes()
        escolher_opcoes()
   

if __name__ == "__main__":
    main()




    