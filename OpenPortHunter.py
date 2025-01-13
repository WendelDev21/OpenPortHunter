import socket
from datetime import datetime
import threading
import csv
import os
import sys
from fpdf import FPDF  # Certifique-se de instalar essa biblioteca com `pip install fpdf`

# --- Funções utilitárias ---
def print_banner():
    """Exibe o banner da ferramenta apenas uma vez."""
    print("""
    
    
 _______  _______  _______  __    _  _______  _______  ______    _______  __   __  __   __  __    _  _______  _______  ______     
|       ||       ||       ||  |  | ||       ||       ||    _ |  |       ||  | |  ||  | |  ||  |  | ||       ||       ||    _ |    
|   _   ||    _  ||    ___||   |_| ||    _  ||   _   ||   | ||  |_     _||  |_|  ||  | |  ||   |_| ||_     _||    ___||   | ||    
|  | |  ||   |_| ||   |___ |       ||   |_| ||  | |  ||   |_||_   |   |  |       ||  |_|  ||       |  |   |  |   |___ |   |_||_   
|  |_|  ||    ___||    ___||  _    ||    ___||  |_|  ||    __  |  |   |  |       ||       ||  _    |  |   |  |    ___||    __  |  
|       ||   |    |   |___ | | |   ||   |    |       ||   |  | |  |   |  |   _   ||       || | |   |  |   |  |   |___ |   |  | |  
|_______||___|    |_______||_|  |__||___|    |_______||___|  |_|  |___|  |__| |__||_______||_|  |__|  |___|  |_______||___|  |_|  

    
OpenPortHunter - Scanner de portas abertas
    """)

def print_progress_bar(iteration, total, length=50):
    """Exibe uma barra de progresso."""
    percent = (iteration / total) * 100
    filled_length = int(length * iteration // total)
    bar = '=' * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r[{bar}] {percent:.1f}%')
    sys.stdout.flush()

def scan_port(target, port, results):
    """Tenta conectar a uma porta e registra o status."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Desconhecido"
            results.append((port, "Aberta", service))
        sock.close()
    except Exception:
        pass

def save_results(results, target):
    """Oferece opções de salvar os resultados em TXT, PDF ou CSV."""
    choice = input("\nDeseja salvar o relatório? (S/N): ").strip().lower()
    if choice != 's':
        return

    print("\nEscolha o formato para salvar:")
    print("1 - TXT")
    print("2 - PDF")
    print("3 - CSV")
    format_choice = input("Digite o número correspondente: ").strip()

    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    os.makedirs(downloads_dir, exist_ok=True)
    
    if format_choice == "1":
        output_file = os.path.join(downloads_dir, f"scan_{target.replace('.', '_')}.txt")
        with open(output_file, "w") as txtfile:
            txtfile.write(f"Resultados do scanner para {target}:\n")
            for port, status, service in results:
                txtfile.write(f"Porta {port}: {status} (Serviço: {service})\n")
        print(f"Relatório salvo como TXT em: {output_file}")
    elif format_choice == "2":
        output_file = os.path.join(downloads_dir, f"scan_{target.replace('.', '_')}.pdf")
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Resultados do scanner para {target}", ln=True, align='C')
        pdf.ln(10)
        for port, status, service in results:
            pdf.cell(0, 10, txt=f"Porta {port}: {status} (Serviço: {service})", ln=True)
        pdf.output(output_file)
        print(f"Relatório salvo como PDF em: {output_file}")
    elif format_choice == "3":
        output_file = os.path.join(downloads_dir, f"scan_{target.replace('.', '_')}.csv")
        with open(output_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Porta", "Status", "Serviço"])
            writer.writerows(results)
        print(f"Relatório salvo como CSV em: {output_file}")
    else:
        print("Opção inválida. O relatório não foi salvo.")

# --- Função principal ---
def port_scanner():
    """Executa o scanner de portas abertas."""
    print_banner()  # Exibe o banner uma vez
    while True:
        # Solicita as informações do usuário
        target = input("\nDigite o endereço IP ou domínio para escanear: ").strip()
        start_port = int(input("Digite o número da porta inicial: "))
        end_port = int(input("Digite o número da porta final: "))

        print(f"\nIniciando o scanner em {target}")
        print(f"Escaneando portas de {start_port} a {end_port}...\n")

        start_time = datetime.now()
        threads = []
        results = []
        total_ports = end_port - start_port + 1

        # Cria threads para escanear as portas
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(target, port, results))
            threads.append(t)
            t.start()
            print_progress_bar(port - start_port + 1, total_ports)

        # Aguarda todas as threads terminarem
        for t in threads:
            t.join()
        print_progress_bar(total_ports, total_ports)  # Exibe progresso final

        # Exibe os resultados
        results.sort(key=lambda x: x[0])
        if results:
            print(f"\nPortas abertas em {target}:")
            for port, status, service in results:
                print(f"Porta {port}: {status} (Serviço: {service})")
        else:
            print(f"Nenhuma porta aberta encontrada em {target}.")

        # Salva os resultados
        save_results(results, target)

        # Pergunta se o usuário quer continuar
        cont = input("\nDeseja continuar escaneando? (S/N): ").strip().lower()
        if cont == 'n':
            print("\nEncerrando o programa. Obrigado por usar o OpenPortHunter!")
            break

# --- Ponto de entrada ---
if __name__ == "__main__":
    port_scanner()
