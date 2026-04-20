saldo = 0
transacoes = []

while True:
    print("\n--- CoinTrack ---")
    print("1 - Adicionar Receita")
    print("2 - Adicionar Despesa")
    print("3 - Ver Saldo")
    print("4 - Ver Histórico")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        descricao = input("Descrição da receita: ")
        valor = float(input("Valor: "))

        saldo += valor
        transacoes.append(f"Receita: {descricao} | +R$ {valor:.2f} | Saldo: R$ {saldo:.2f}")

        print("Receita adicionada!")

    elif opcao == "2":
        descricao = input("O que você gastou? ")

        print("Categoria:")
        print("1 - Alimentação")
        print("2 - Transporte")
        print("3 - Contas")
        print("4 - Lazer")

        cat = input("Escolha: ")

        if cat == "1":
            categoria = "Alimentação"
        elif cat == "2":
            categoria = "Transporte"
        elif cat == "3":
            categoria = "Contas"
        elif cat == "4":
            categoria = "Lazer"
        else:
            categoria = "Outros"

        valor = float(input("Valor: "))

        saldo -= valor
        transacoes.append(f"Despesa: {descricao} | {categoria} | -R$ {valor:.2f} | Saldo: R$ {saldo:.2f}")

        print("Despesa registrada!")

    elif opcao == "3":
        print(f"\nSaldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        print("\n--- Histórico ---")
        if len(transacoes) == 0:
            print("Nenhuma transação.")
        else:
            for t in transacoes:
                print(t)

    elif opcao == "5":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
