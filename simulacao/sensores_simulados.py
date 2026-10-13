import json
import random
from datetime import datetime, timedelta

random.seed(42)


def gerar_leitura(molde_id, data_hora, fluxo_agua_l_min, temperatura_agua_c, vazamento_oleo):
    leitura = {
        "molde_id": molde_id,
        "data_hora": data_hora,
        "fluxo_agua_l_min": fluxo_agua_l_min,
        "temperatura_agua_c": temperatura_agua_c,
        "vazamento_oleo": vazamento_oleo
    }

    return leitura


def cenario_nominal(molde_id, data_hora):
    fluxo = 18.0 + random.uniform(-0.5, 0.5)
    temperatura = 32.0 + random.uniform(-0.5, 0.5)

    return gerar_leitura(
        molde_id,
        data_hora,
        round(fluxo, 1),
        round(temperatura, 1),
        False
    )


def cenario_queda_fluxo(molde_id, data_hora, indice, total_leituras):
    fluxo_inicial = 18.5
    fluxo_final = 8.0

    progresso = indice / (total_leituras - 1)
    fluxo = fluxo_inicial + (fluxo_final - fluxo_inicial) * progresso

    fluxo += random.uniform(-0.3, 0.3)

    temperatura = 32.0 + random.uniform(-0.5, 0.5)

    return gerar_leitura(
        molde_id,
        data_hora,
        round(fluxo, 1),
        round(temperatura, 1),
        False
    )

def cenario_aquecimento(molde_id, data_hora, indice, total_leituras):
    temperatura_inicial = 32.0
    temperatura_final = 47.0

    progresso = indice / (total_leituras - 1)
    temperatura = temperatura_inicial + (temperatura_final - temperatura_inicial) * progresso

    temperatura += random.uniform(-0.3, 0.3)

    fluxo = 18.5 + random.uniform(-0.3, 0.3)

    return gerar_leitura(
        molde_id,
        data_hora,
        round(fluxo, 1),
        round(temperatura, 1),
        False
    )


def salvar_jsonl(leituras, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for leitura in leituras:
            arquivo.write(json.dumps(leitura, ensure_ascii=False) + "\n")


leituras = []

inicio = datetime.fromisoformat("2026-10-05T08:00:00")

for i in range(12):
    data_hora = inicio + timedelta(minutes=5 * i)
    data_hora = data_hora.strftime("%Y-%m-%dT%H:%M:%S")

    leituras.append(cenario_queda_fluxo("M001", data_hora, i, 12))

    leituras.append(cenario_aquecimento("M002", data_hora, i, 12))

    if i < 6:
        vazamento = False
    else:
        vazamento = True

    leituras.append(
        gerar_leitura(
            "M003",
            data_hora,
            round(18.5 + random.uniform(-0.3, 0.3), 1),
            round(32.0 + random.uniform(-0.5, 0.5), 1),
            vazamento
        )
    )


salvar_jsonl(leituras, "simulacao/entrada.jsonl")
