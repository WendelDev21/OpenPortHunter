# OpenPortHunter - Scanner de Portas Abertas

**OpenPortHunter** é uma ferramenta de código aberto para escanear portas abertas em um endereço IP ou domínio, identificando serviços disponíveis e suas respectivas portas. Desenvolvido com Python, o OpenPortHunter oferece uma interface de linha de comando simples e eficiente, além de opções para salvar os resultados em diversos formatos, como TXT, PDF e CSV.

## Funcionalidades

- Escaneia portas abertas em um endereço IP ou domínio.
- Identifica serviços correspondentes às portas abertas.
- Exibe uma barra de progresso durante a execução do scan.
- Permite salvar os resultados do escaneamento nos seguintes formatos:
  - TXT
  - PDF
  - CSV
- Multithreading para escaneamento rápido de múltiplas portas.

## Como Usar

1. Clone o repositório ou faça o download do código fonte.
   ```bash
   git clone https://github.com/WendelDev21/OpenPortHunter.git
   ```
2. Execute o script:
   ```bash
   python OpenPortHunter.py
   ```
3. Escolha entre iniciar o scanner ou sair.
4. Caso deseje, salve os resultados em um dos formatos suportados.

### Exemplo de Execução

```bash
$ python OpenPortHunter.py

OpenPortHunter - Scanner de Portas Abertas

[1] - Iniciar OpenPortHunter
[2] - Sair

Escolha uma opção: 1

Digite o endereço IP ou domínio para escanear: example.com
Digite o número da porta inicial: 80
Digite o número da porta final: 90
Iniciando o scanner em example.com
Escaneando portas de 80 a 90...

Resultados do scanner para example.com:
Porta 80: Aberta (Serviço: http)
Porta 443: Aberta (Serviço: https)

Deseja salvar o relatório? (S/N): S
Escolha o formato para salvar:
1 - TXT
2 - PDF
3 - CSV
Digite o número correspondente: 1

Relatório salvo como TXT em: /caminho/para/o/arquivo/scan_example_com.txt
```

## Contribuindo

Contribuições são sempre bem-vindas! Se você deseja contribuir para o projeto, por favor, siga as etapas abaixo:

1. Fork o repositório.
2. Crie uma nova branch (`git checkout -b feature/novafuncionalidade`).
3. Faça suas alterações.
4. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
5. Push para o branch (`git push origin feature/novafuncionalidade`).
6. Abra um Pull Request.

## Doações

Se você gostou do projeto e gostaria de apoiar seu desenvolvimento, considere fazer uma doação em Bitcoin:

**Endereço Bitcoin para doações:**

```
bc1q0aadkkgmveayaysxk8zvr9wazlahjnn34nuds9
```

A sua contribuição é muito apreciada e ajudará a manter o projeto ativo e em constante evolução!

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**OpenPortHunter** - Desenvolvido com amor pela comunidade de código aberto.
```