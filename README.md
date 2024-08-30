Desafio Técnico

Este repositório contém a solução para o desafio técnico, dividido em cinco questões, conforme descrito abaixo.

**Estrutura do Projeto**

- `src/`: Contém os scripts Python que resolvem cada uma das questões do desafio.
- `data/`: Contém o arquivo JSON necessário para a questão 3.
- `README.md`: Este arquivo, contendo as instruções para execução dos scripts.
- `requirements.txt`: Arquivo para instalação das dependências (caso necessário).

**Questões**

1. **Cálculo da Variável SOMA**
   - **Arquivo:** `questao1.py`
   - Este script calcula e imprime o valor final da variável `SOMA` após processar o código dado.

2. **Verificação de Número na Sequência de Fibonacci**
   - **Arquivo:** `questao2.py`
   - O script calcula a sequência de Fibonacci até o número informado e verifica se ele pertence à sequência.
   - **Execução:** `python src/questao2.py <numero>`

3. **Análise de Faturamento Diário**
   - **Arquivo:** `questao3.py`
   - Lê os dados de faturamento diário a partir de um arquivo JSON, identificando o menor e maior valor de faturamento, e conta quantos dias tiveram faturamento acima da média mensal.
   - **Execução:** `python src/questao3.py`

4. **Percentual de Faturamento por Estado**
   - **Arquivo:** `questao4.py`
   - Este script calcula o percentual de representação de cada estado no faturamento total mensal.

5. **Inversão de String**
   - **Arquivo:** `questao5.py`
   - O script inverte os caracteres de uma string sem usar funções prontas como `reverse()`.
   - **Execução:** `python src/questao5.py <string>`

**Execução**

Todos os scripts foram desenvolvidos em Python. Para executar, certifique-se de ter o Python instalado. Se houver dependências, instale-as com:

`pip install -r requirements.txt`
