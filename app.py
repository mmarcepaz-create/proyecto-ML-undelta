import streamlit as st
import pandas as pd

# Configuración inicial de la página
st.set_page_config(page_title="Fashion-MNIST Dashboard", layout="wide")

st.title("📊 Seguimiento de Proyecto: Clasificación Fashion-MNIST")
st.markdown("---")

# Barra lateral de navegación
seccion = st.sidebar.radio("Navegación", [
                           "General", "Experimentos de Hiperparámetros", "Comparación de Modelos"])

if seccion == "General":
    st.header("📌 Resumen del Proyecto")
    st.write("Seguimiento del entrenamiento de modelos (Random Forest vs Perceptrón Multicapa / MLP) sobre Fashion-MNIST.")

elif seccion == "Experimentos de Hiperparámetros":
    st.header("📝 Registro de Pruebas")

    # Registro de pruebas realizadas en Colab
    experimentos = [
        {"Exp": "E-01", "Modelo": "MLP Base",
            "Hiperparámetros": "2 Capas (128, 64), lr=0.001", "Accuracy Test": "87.1%"},
        {"Exp": "E-02", "Modelo": "MLP + Dropout",
            "Hiperparámetros": "Dropout=0.2, Epochs=25", "Accuracy Test": "88.8%"},
        {"Exp": "E-03", "Modelo": "Random Forest",
            "Hiperparámetros": "n_estimators=25, max_depth=20", "Accuracy Test": "86.8%"},
    ]
    df_exp = pd.DataFrame(experimentos)
    st.dataframe(df_exp, use_container_width=True)

elif seccion == "Comparación de Modelos":
    st.header("⚔️ Random Forest vs MLP")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Random Forest")
        st.metric(label="Accuracy en Test",
                  value="86.8%", delta="Tiempo: 30.95s")
    with col2:
        st.subheader("Perceptrón Multicapa (MLP)")
        st.metric(label="Accuracy en Test",
                  value="88.8%", delta="+2.0% Mejora")
