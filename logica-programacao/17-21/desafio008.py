tamanho_arquivo = float(input("Informe o tamanho do arquivo(MB): "))
velocidade_internet = float(input("Informe a velocidade da internet(Mbps): "))

tempo_download_segundos = tamanho_arquivo * 8 / velocidade_internet

tempo_download_minutos = tempo_download_segundos // 60
tempo_download_segundos = tempo_download_segundos % 60

print(f"Tempo de download {tempo_download_minutos:.0f}:{tempo_download_segundos:.0f} min")