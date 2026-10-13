# SISP — Sistema Inteligente de Sensores Preditivos

**Projeto acadêmico de Análise e Desenvolvimento de Sistemas — ETEP**

## Sobre o projeto

O **SISP (Sistema Inteligente de Sensores Preditivos)** é um protótipo acadêmico que busca demonstrar como o monitoramento de variáveis de um processo industrial pode auxiliar na identificação de condições anormais e apoiar a tomada de decisões relacionadas à manutenção.

O projeto utiliza como referência hipotética um ambiente de injeção de plástico, considerando situações como a redução do fluxo de água no sistema de refrigeração, o aumento da temperatura da água e a ocorrência de vazamentos de óleo.

A solução será desenvolvida por meio de simulação de sensores, processamento de dados em Python, armazenamento em banco de dados SQLite e visualização dos resultados em um dashboard no Power BI Desktop.

> **Aviso:** este projeto utiliza dados simulados e moldes hipotéticos. Não representa um sistema industrial em operação, não utiliza dados reais de nenhuma empresa e não substitui a avaliação de profissionais técnicos.

## Objetivos

- Simular a coleta de variáveis relacionadas a um processo industrial.
- Gerar cenários de operação nominal e de condições anormais.
- Processar as medições para identificar possíveis anomalias.
- Classificar as condições identificadas conforme regras e limites hipotéticos definidos no projeto.
- Armazenar os resultados para consulta e análise.
- Desenvolver um dashboard para facilitar a visualização das medições, ocorrências e classificações.

## Relação com os Objetivos de Desenvolvimento Sustentável

- **ODS 9 — Indústria, Inovação e Infraestrutura:** objetivo principal, relacionado à demonstração de soluções tecnológicas para o monitoramento e a melhoria de processos industriais.
- **ODS 12 — Consumo e Produção Responsáveis:** objetivo complementar, relacionado ao potencial de identificação de condições que possam contribuir para desperdícios ou impactos ambientais.

A contribuição para esses objetivos é exploratória e conceitual. O protótipo não comprova redução de emissões, consumo de recursos ou custos operacionais.

## Arquitetura da solução

O fluxo previsto para o projeto é:

1. **Simulação:** geração de medições fictícias que representam os sensores e o dispositivo IoT.
2. **Processamento:** leitura dos dados simulados, aplicação das regras de classificação e identificação de possíveis anomalias.
3. **Banco de dados:** armazenamento das medições processadas e dos resultados conforme o esquema definido pelo projeto.
4. **Visualização:** apresentação dos dados e resultados em um dashboard no Power BI Desktop.

### Tecnologias previstas

| Tecnologia | Finalidade |
|---|---|
| Python | Simulação e processamento de dados |
| JSONL | Intercâmbio de medições simuladas |
| SQLite | Armazenamento dos dados |
| SQL | Definição e consulta dos dados |
| Power BI Desktop | Visualização e análise dos resultados |
| Git e GitHub | Versionamento e colaboração |

A comunicação via API REST ou MQTT poderá ser avaliada, caso seja necessária para a integração. O uso de hardware físico, como ESP32 e sensores reais, não faz parte do escopo obrigatório do protótipo.

## Variáveis monitoradas

O contrato de entrada da simulação contempla cinco campos:

| Campo | Tipo | Descrição |
|---|---|---|
| `molde_id` | String | Identificador do molde hipotético |
| `data_hora` | String | Data e hora da medição |
| `fluxo_agua_l_min` | Número decimal | Fluxo de água em litros por minuto |
| `temperatura_agua_c` | Número decimal | Temperatura da água em graus Celsius |
| `vazamento_oleo` | Booleano | Indica se o cenário simulado apresenta vazamento |

Os identificadores `M001`, `M002` e `M003` representam moldes fictícios utilizados na simulação.

O arquivo `entrada.jsonl` utiliza o formato JSON Lines, no qual cada linha contém um objeto JSON independente.

Exemplo de uma leitura:

```json
{
  "molde_id": "M001",
  "data_hora": "2026-10-14T08:00:00",
  "fluxo_agua_l_min": 18.5,
  "temperatura_agua_c": 32.4,
  "vazamento_oleo": false
}
```

Os valores apresentados são ilustrativos e não devem ser interpretados como parâmetros reais de operação industrial.

## Cenários simulados

A simulação contempla os seguintes cenários:

- **Operação nominal:** valores próximos às condições de referência hipotéticas.
- **Queda progressiva de fluxo:** redução gradual do fluxo de água.
- **Aquecimento:** aumento progressivo da temperatura da água.
- **Vazamento de óleo:** alteração do indicador booleano para representar a ocorrência simulada.

O processamento posterior será responsável por interpretar as medições e determinar os respectivos eventos, status e níveis de severidade, conforme as regras aprovadas pelo grupo.

As classificações do protótipo não constituem diagnóstico industrial nem previsão comprovada de falhas.

## Organização do repositório

A estrutura planejada para o projeto é:

```text
SISP/
├── simulacao/
│   ├── cenarios.py
│   ├── gerar_dados.py
│   └── testar_simulacao.py
├── processamento/
│   ├── processar_dados.py
│   ├── config.json
│   └── testar_processamento.py
├── banco/
│   ├── schema.sql
│   └── consultas.sql
├── powerbi/
│   └── README.md
├── documentacao/
│   ├── arquitetura.md
│   ├── contrato_dados.md
│   └── atas/
├── .gitignore
└── README.md
```

A estrutura poderá ser ajustada conforme a integração dos módulos e a evolução do projeto.

## Execução do projeto

O projeto será executado por etapas, respeitando as dependências entre os módulos:

1. Gerar o arquivo de medições simuladas.
2. Executar o processamento dos dados.
3. Persistir e consultar os resultados no SQLite.
4. Conectar o Power BI Desktop à fonte de dados configurada.
5. Visualizar os resultados no dashboard.

As instruções específicas de instalação e execução de cada módulo serão documentadas nas respectivas pastas à medida que a implementação for consolidada.

## Escopo e limitações

- Os sensores e o dispositivo IoT são simulados.
- Os moldes e os dados utilizados são fictícios.
- Os limites de classificação são hipotéticos e definidos exclusivamente para a demonstração acadêmica.
- O sistema não substitui inspeções, manutenção ou decisões de profissionais especializados.
- Não há garantia de detecção antecipada de falhas reais.
- Os resultados obtidos demonstram o funcionamento do protótipo, não sua eficácia em ambiente industrial real.

## Equipe

Projeto desenvolvido por uma equipe de seis estudantes do curso de Análise e Desenvolvimento de Sistemas da ETEP, em São José dos Campos — SP.

**Finalidade:** acadêmica e demonstrativa.

