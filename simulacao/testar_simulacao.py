import json
from datetime import datetime

leituras = []

with open("simulacao/entrada.jsonl", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        leitura = json.loads(linha)
        leituras.append(leitura)

        assert len(leitura) == 5

        assert isinstance(leitura["molde_id"], str)
        assert isinstance(leitura["data_hora"], str)
        assert isinstance(leitura["fluxo_agua_l_min"], (int, float))
        assert isinstance(leitura["temperatura_agua_c"], (int, float))
        assert isinstance(leitura["vazamento_oleo"], bool)

        for valor in leitura.values():
            assert valor is not None

        datetime.strptime(
            leitura["data_hora"],
            "%Y-%m-%dT%H:%M:%S"
        )

assert len(leituras) == 36

assert sum(leitura["molde_id"] == "M001" for leitura in leituras) == 12
assert sum(leitura["molde_id"] == "M002" for leitura in leituras) == 12
assert sum(leitura["molde_id"] == "M003" for leitura in leituras) == 12
print("Todos os testes passaram!")