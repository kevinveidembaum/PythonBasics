import pandas as pd
from bcb import currency
from datetime import datetime, timedelta

def obter_taxa_cambio():
    # Define o intervalo de datas (última semana)
    hoje = datetime.today()
    data_inicio = hoje - timedelta(days=7)
    data_fim = hoje

    # Obtém a taxa de câmbio mais recente para BRL/USD
    df = currency.get(symbols=['USD'], start=data_inicio.strftime('%Y-%m-%d'), end=data_fim.strftime('%Y-%m-%d'))
    
    if df.empty:
        raise ValueError("Nenhuma taxa de câmbio foi retornada pela API.")
    
    # Seleciona a taxa de câmbio mais recente
    return df['USD'].iloc[-1]

def converter_valor(valor_brl, taxa_cambio):
    return valor_brl / taxa_cambio

def main():
    try:
        valor_brl = float(input("Digite o valor em Real (BRL) que deseja converter para Dólar (USD): "))
        taxa_cambio = obter_taxa_cambio()
        valor_usd = converter_valor(valor_brl, taxa_cambio)
        print(f"Valor em Dólar (USD): {valor_usd:.2f}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
