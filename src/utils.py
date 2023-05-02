import pandas as pd
import seaborn as sns


def resumen_pd():
    df = pd.read_pickle("data/Fraud.pkl")

    # Listar columnas
    df.columns

    # Acceder a una columna
    df.step
    df["step"]

    # Info DF
    df.info()
    df.step = df.step.astype(int)
    df.describe()
    df.type.value_counts()
    df.type.unique()
    df.type.nunique()
    df.type.isna().sum()
    df.isFraud.value_counts()

    # Operacion sobre nombre origen
    df["letraNameOrig"] = df.nameOrig.map(lambda x: x[0])
    # Igual que el anterior
    # df['letraNameOrig'] = df.nameOrig.str[0]

    df["letraNameOrig"].value_counts()

    # Librerias para ver los datos
    # matplotlib, seaborn, plotly

    sns.pairplot(df)
