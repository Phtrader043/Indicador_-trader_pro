import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

MODEL_PATH = "model/neural_model.pkl"

def treinar_modelo(dados):
    X = dados.drop(columns=["Sinal"])
    y = dados["Sinal"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    modelo = RandomForestClassifier(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)

    score = modelo.score(X_test, y_test)
    print(f"✔️ Modelo treinado com acurácia: {round(score * 100, 2)}%")

    os.makedirs("model", exist_ok=True)
    joblib.dump(modelo, MODEL_PATH)
    print("✔️ Modelo salvo em:", MODEL_PATH)

def carregar_modelo():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        raise FileNotFoundError("Modelo não encontrado. Execute o treino primeiro.")

def prever_sinal(entrada):
    modelo = carregar_modelo()
    resultado = modelo.predict(entrada)
    probabilidade = modelo.predict_proba(entrada)
    return resultado[0], np.max(probabilidade)
