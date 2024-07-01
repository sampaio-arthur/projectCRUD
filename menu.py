import atualizar
import deletar
import inserir
import selecionar_todos
import selecionar_um

def mostrar_menu():
    print("\nMenu de Operações:")
    print("1. Inserir usuário")
    print("2. Atualizar usuário")
    print("3. Deletar usuário")
    print("4. Selecionar todos os usuários")
    print("5. Selecionar um usuário")
    print("6. Sair")

def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            inserir.inserir_usuario()
        elif escolha == '2':
            atualizar.atualizar_usuario()
        elif escolha == '3':
            deletar.deletar_usuario()
        elif escolha == '4':
            selecionar_todos.selecionar_todos()
        elif escolha == '5':
            selecionar_um.selecionar_um()
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
