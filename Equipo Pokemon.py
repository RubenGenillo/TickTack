import pandas as pd
from mochila import mochila

def main():
    df = pd.read_csv('Pokemon.csv')
    df_clean = df[['name', 'capture_rate', 'base_total']].copy()
    cp_max = 10

    #Borro a minior del dataFrame limpio dado que falla a la hora de cambiarlo a tipo float y que no es de los mejores pokemon
    df_clean.drop((df.loc[df_clean['capture_rate'] == '30 (Meteorite)255 (Core)']).index, inplace=True)
    df_clean['capture_rate'] = df_clean['capture_rate'].astype('float')
    df_clean['base_total'] = df_clean['base_total'].astype('float')
    df_clean['capture_rate'] = df_clean['capture_rate'].apply(lambda x: (x-2.0)/253.0)
    df_clean['beneficio/peso'] = df_clean['base_total']*df_clean['capture_rate']
    df_clean = df_clean.sort_values(by = "beneficio/peso", ascending=True)
    print(df_clean.head(10))
    listaPokemons = df_clean.values.tolist()
    Equipo_pokemon = mochila(listaPokemons, cp_max)
    print(Equipo_pokemon)

if __name__ == "__main__":
    main()