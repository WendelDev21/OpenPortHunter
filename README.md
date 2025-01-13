# OpenPortHunter

**OpenPortHunter** é uma ferramenta poderosa e simples para realizar varreduras de portas abertas em IPs ou domínios. Projetada para ajudar profissionais de segurança e administradores de redes, ela permite identificar serviços ativos em diferentes portas de um host.

## Recursos Principais

- **Scanner de Portas**: Identifica portas abertas em um intervalo especificado.
- **Barra de Progresso**: Feedback visual do andamento da varredura.
- **Exportação de Resultados**: Salve relatórios em **TXT**, **PDF** ou **CSV**.
- **Interface Simples**: Fluxo de uso amigável, com instruções claras.
- **Multi-threading**: Acelera o escaneamento utilizando várias threads simultaneamente.

## Requisitos

- Python 3.6 ou superior
- Pacotes necessários:
  - `fpdf`

Para instalar os pacotes necessários, execute o comando:

```bash
pip install fpdf
```

## Como Usar

1. Clone ou faça o download deste repositório.
2. Execute o script com o comando:

```bash
python OpenPortHunter.py
```

3. Digite o endereço IP ou domínio que deseja escanear.
4. Forneça o intervalo de portas que deseja verificar.
5. Acompanhe os resultados diretamente no terminal.
6. Escolha salvar os relatórios, se necessário:
   - **TXT**: Relatório em texto simples.
   - **PDF**: Relatório formatado.
   - **CSV**: Relatório estruturado para análise em planilhas.

## Exemplos de Uso

### Exemplo de Varredura

- **Entrada:**
  ```
  Digite o endereço IP ou domínio para escanear: 192.168.1.1
  Digite o número da porta inicial: 20
  Digite o número da porta final: 80
  ```
- **Saída:**
  ```
  Portas abertas em 192.168.1.1:
  Porta 22: Aberta (Serviço: ssh)
  Porta 80: Aberta (Serviço: http)
  ```

### Exportando Relatórios

- **TXT:**
  ```
Resultados do scanner para 192.168.1.1:
Porta 22: Aberta (Serviço: ssh)
Porta 80: Aberta (Serviço: http)
  ```

- **PDF:** Relatório formatado com título e lista das portas abertas.
- **CSV:** Arquivo com colunas para porta, status e serviço.

## Estrutura do Código

- **`print_banner`**: Exibe o banner inicial.
- **`print_progress_bar`**: Mostra o progresso da varredura.
- **`scan_port`**: Realiza a verificação de cada porta.
- **`save_results`**: Gerencia a exportação dos resultados.
- **`port_scanner`**: Fluxo principal da aplicação.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Desenvolvido com 💻 e ☕ por entusiastas de segurança da informação.**
