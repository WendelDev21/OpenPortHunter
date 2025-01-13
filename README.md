# OpenPortHunter - Scanner de Portas Abertas

OpenPortHunter é uma ferramenta eficiente para escaneamento de portas abertas em servidores, IPs ou domínios. Através desta ferramenta, você pode realizar uma análise rápida para verificar a segurança de sistemas, identificando quais portas estão acessíveis publicamente. A ferramenta suporta a geração de relatórios em vários formatos, como TXT, PDF e CSV, oferecendo flexibilidade na apresentação dos resultados.

## Funcionalidades

- **Escaneamento de Portas**: Permite escanear um intervalo de portas em um IP ou domínio específico.
- **Suporte a Múltiplos Formatos de Relatório**: Salve os resultados em TXT, PDF ou CSV.
- **Barra de Progresso Interativa**: Exibe o progresso do escaneamento em tempo real, oferecendo uma experiência de usuário mais amigável.
- **Instalação Automática de Pacotes**: O pacote necessário será instalado automaticamente caso não esteja presente no ambiente, garantindo que o usuário não precise se preocupar com dependências.

## Tecnologias Utilizadas

- **Python 3.x**: A linguagem de programação usada para desenvolver a ferramenta.
- **Bibliotecas**: 
  - `socket` para a comunicação de rede e escaneamento de portas.
  - `fpdf` para gerar relatórios em formato PDF.
  - `csv` para exportar resultados em formato CSV.
  - `threading` para realizar escaneamentos de portas de forma paralela e otimizada.

## Requisitos

- Python 3.x instalado.
- Conexão com a Internet para instalação automática de pacotes.

## Instalação

1. **Clone este repositório**:

   Clone o repositório para o seu diretório local:

   ```bash
   git clone https://github.com/seu_usuario/OpenPortHunter.git
   cd OpenPortHunter
   ```

2. **Executar o script**:

   O script pode ser executado diretamente. A instalação do pacote `fpdf` será feita automaticamente se não estiver instalado:

   ```bash
   python3 OpenPortHunter.py
   ```

   O programa pedirá para você inserir o endereço IP ou domínio, e o intervalo de portas a ser escaneado. Após o escaneamento, você poderá escolher em qual formato deseja salvar os resultados.

## Como Usar

1. Ao executar o script, será solicitado o **endereço IP ou domínio** que você deseja escanear.
2. Depois, você informará o **intervalo de portas** (exemplo: 80 a 443).
3. O programa começará o escaneamento e mostrará uma **barra de progresso** durante a execução.
4. Após o término do escaneamento, será perguntado se você deseja salvar os resultados:
   - **TXT**: Relatório simples em formato de texto.
   - **PDF**: Relatório formatado em PDF.
   - **CSV**: Relatório em formato CSV, adequado para análise em planilhas.
5. Se desejar continuar escaneando outras portas, o programa permitirá que você faça novos escaneamentos.

## Exemplo de Uso

```bash
$ python3 OpenPortHunter.py

Digite o endereço IP ou domínio para escanear: 192.168.1.1
Digite o número da porta inicial: 80
Digite o número da porta final: 90

Iniciando o scanner em 192.168.1.1
Escaneando portas de 80 a 90...

[====================--------------------] 60%

Portas abertas em 192.168.1.1:
Porta 80: Aberta (Serviço: http)
Porta 443: Aberta (Serviço: https)

Deseja salvar o relatório? (S/N): s
Escolha o formato para salvar:
1 - TXT
2 - PDF
3 - CSV
Digite o número correspondente: 2
Relatório salvo como PDF em: /home/user/Downloads/scan_192_168_1_1.pdf
```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE). Consulte o arquivo LICENSE para mais detalhes.