# Douglas, Renato
# 17/09/2016
# Desenv. de Sist. Aplicados a dados


import json

def validar_qualidade_dados(caminho_arquivo):
    try:
        # 1. Abertura e leitura do arquivo JSON
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        print("✅ Arquivo JSON carregado com sucesso!\n")

        # 2. Validação de chaves estruturais obrigatórias
        chaves_obrigatorias = ["nome_squad", "registros_vendas"]
        for chave in chaves_obrigatorias:
            if chave not in dados:
                print(f"❌ ERRO DE SCHEMA: A chave obrigatória '{chave}' não foi encontrada!")
                return

        print(f"📊 Squad Responsável: {dados.get('nome_squad')}")
        print(f"📅 Data da Coleta: {dados.get('data_coleta', 'Não informada')}")
        print("-" * 40)

        # 3. Processamento e contagem de qualidade dos registros
        registros = dados["registros_vendas"]
        total_registros = len(registros)
        validos = 0
        invalidos = 0

        for reg in registros:
            status = reg.get("status_qualidade", "DESCONHECIDO")
            if status == "VALIDO":
                validos += 1
            else:
                invalidos += 1

        # 4. Exibição do relatório final no terminal
        print(f"📊 Total de registros analisados: {total_registros}")
        print(f"🟢 Registros VÁLIDOS: {validos}")
        print(f"🔴 Registros INVÁLIDOS: {invalidos}")

    except FileNotFoundError:
        print(f"❌ ERRO: O arquivo '{caminho_arquivo}' não foi encontrado na pasta.")

    except json.JSONDecodeError:
        print("❌ ERRO SINTÁTICO: O arquivo contém erros de formatação JSON.")

# Execução do validador
if __name__ == "__main__":
    validar_qualidade_dados("schema_dados.json")
