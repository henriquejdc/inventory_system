from inventory_system.models import Product
from inventory_system.inventory import Inventory
from inventory_system.exceptions import ProductAlreadyExistsError, ProductNotFoundError


def separator():
    print("-" * 30)


def main():
    inventory = Inventory()
    id_counter = 1

    print("Sistema de Gerenciamento de Inventário")
    separator()

    while True:
        print("MENU - Escolha uma opção:")
        separator()
        print("1 - Adicionar Produto")
        print("2 - Consultar Produto")
        print("3 - Atualizar Quantidade")
        print("4 - Atualizar Preço")
        print("5 - Listar Produtos com Estoque Baixo")
        print("6 - Ver Valor Total do Inventário")
        print("7 - Sair")
        separator()
        option = input("Opção: ")
        separator()

        match option:
            case "1":
                name = input("Nome do produto: ")
                try:
                    price = float(input("Preço unitário: "))
                    quantity = int(input("Quantidade em estoque: "))
                    inventory.add_product(Product(id_counter, name, price, quantity))
                    id_counter += 1
                    separator()
                    print("Produto adicionado com sucesso.")
                except ValueError:
                    separator()
                    print("X - Atenção: Entrada inválida.")
                except ProductAlreadyExistsError as e:
                    separator()
                    print(f"X - {e}")

            case "2":
                product_id = input("ID do produto a consultar: ")
                try:
                    product = inventory.get_product(int(product_id))
                    separator()
                    print(f"Produto encontrado: {product.name}")
                    print(f"Preço: R$ {product.price}")
                    print(f"Quantidade: {product.quantity}")
                except ProductNotFoundError as e:
                    separator()
                    print(f"X - {e}")

            case "3":
                product_id = input("ID do produto: ")
                try:
                    quantity = int(input("Nova quantidade: "))
                    inventory.update_quantity(int(product_id), quantity)
                    separator()
                    print("Quantidade atualizada.")
                except ValueError:
                    separator()
                    print("X - Atenção: Entrada inválida.")
                except ProductNotFoundError as e:
                    separator()
                    print(f"X - {e}")

            case "4":
                product_id = input("ID do produto: ")
                try:
                    price = float(input("Novo preço: "))
                    inventory.update_price(int(product_id), price)
                    separator()
                    print("Preço atualizada.")
                except ValueError:
                    separator()
                    print("X - Atenção: Entrada inválida.")
                except ProductNotFoundError as e:
                    separator()
                    print(f"X - {e}")

            case "5":
                try:
                    minimum = int(input("Estoque mínimo: "))
                    low_stock = inventory.list_below_stock(minimum)
                    if not low_stock:
                        separator()
                        print("X - Nenhum produto com estoque abaixo do mínimo.")
                    else:
                        separator()
                        print("Produtos com estoque baixo:")
                        for p in low_stock:
                            print(f"ID: {p.id} - {p.name} - Quantidade: {p.quantity}")
                except ValueError:
                    separator()
                    print("X - Entrada inválida.")

            case "6":
                print(f"Valor total do inventário: R$ {inventory.total_value():.2f}")

            case "7":
                separator()
                print("Saindo do sistema.")
                break

            case _:
                separator()
                print("X - Opção inválida. Tente novamente.")

        print("-" * 30)


if __name__ == "__main__":
    main()
