import csv
import random
from datetime import datetime, timedelta

FAIXAS_PLAUSIVEIS = {
    'bpm': (60, 130),
    'spo2': (90, 100),
    'temp_celsius': (35.5, 39.5),
    'pressao_sis': (90, 150),
    'pressao_dia': (60, 95)
}

def gerar_leituras_csv(num_linhas, num_estacoes, num_sensores, intervalo_segundos, nome_arquivo):
    estacoes = [f"Leito_{i:02d}" for i in range(1, num_estacoes + 1)]
    sensores = [f"Monitor_{i:03d}" for i in range(1, num_sensores + 1)]

    mapa_sensor_estacao = {sensor: random.choice(estacoes) for sensor in sensores}

    tempo_atual = datetime.now()

    colunas = [
        'timestamp',
        'estacao_id',
        'sensor_id',
        'bpm',
        'spo2_pct',
        'temperatura_c',
        'pressao_sistolica',
        'pressao_diastolica'
    ]

    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.DictWriter(arquivo_csv, fieldnames=colunas)
        escritor.writeheader()

        for _ in range(num_linhas):
            sensor_id = random.choice(sensores)
            estacao_id = mapa_sensor_estacao[sensor_id]

            bpm = random.randint(*FAIXAS_PLAUSIVEIS['bpm'])
            spo2 = random.randint(*FAIXAS_PLAUSIVEIS['spo2'])
            temp = round(random.uniform(*FAIXAS_PLAUSIVEIS['temp_celsius']), 1)
            p_sis = random.randint(*FAIXAS_PLAUSIVEIS['pressao_sis'])
            p_dia = random.randint(*FAIXAS_PLAUSIVEIS['pressao_dia'])

            escritor.writerow({
                'timestamp': tempo_atual.strftime('%Y-%m-%d %H:%M:%S'),
                'estacao_id': estacao_id,
                'sensor_id': sensor_id,
                'bpm': bpm,
                'spo2_pct': spo2,
                'temperatura_c': temp,
                'pressao_sistolica': p_sis,
                'pressao_diastolica': p_dia
            })

            tempo_atual += timedelta(seconds=intervalo_segundos)

    print(f"Gerado: {nome_arquivo} ({num_linhas} linhas)")

if __name__ == '__main__':
    gerar_leituras_csv(100_000, 20, 20, 5, 'leituras_sensores_100k.csv')
    gerar_leituras_csv(1_000_000, 20, 20, 5, 'leituras_sensores_1m.csv')
    gerar_leituras_csv(5_000_000, 20, 20, 5, 'leituras_sensores_5m.csv')
