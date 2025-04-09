import streamlit as st

st.set_page_config(page_title="Calculadora Inteligente", page_icon="🧠", layout="centered")

st.title("🧮 Calculadora Inteligente de Carlos")
st.subheader("Tu asistente matemático con estilo 💡")

opciones = [
    "Suma de 2 números",
    "Suma de 3 números",
    "Resta",
    "Multiplicación",
    "División",
    "Exponenciación",
    "División Entera",
    "Resto de División",
    "Promedio de 3 Notas",
    "Promedio Ponderado (5, 12, 20, 15)",
]

opcion = st.selectbox("Selecciona la operación matemática que deseas realizar:", opciones)

if opcion == "Suma de 2 números":
    a = st.number_input("Ingresa el primer número:", key="suma2_1")
    b = st.number_input("Ingresa el segundo número:", key="suma2_2")
    st.success(f"Resultado: {a + b}")

elif opcion == "Suma de 3 números":
    a = st.number_input("Número 1", key="suma3_1")
    b = st.number_input("Número 2", key="suma3_2")
    c = st.number_input("Número 3", key="suma3_3")
    st.success(f"Resultado: {a + b + c}")

elif opcion == "Resta":
    minuendo = st.number_input("Minuendo (valor mayor)", key="resta_1")
    sustraendo = st.number_input("Sustraendo (valor a restar)", key="resta_2")
    st.success(f"Resultado: {minuendo - sustraendo}")

elif opcion == "Multiplicación":
    f1 = st.number_input("Primer factor", key="multi_1")
    f2 = st.number_input("Segundo factor", key="multi_2")
    st.success(f"Resultado: {f1 * f2}")

elif opcion == "División":
    numerador = st.number_input("Numerador", key="div_1")
    denominador = st.number_input("Denominador", key="div_2")
    if denominador != 0:
        st.success(f"Resultado: {numerador / denominador}")
    else:
        st.error("⚠️ Error: No se puede dividir entre 0")

elif opcion == "Exponenciación":
    base = st.number_input("Base", key="exp_base")
    exponente = st.number_input("Exponente", key="exp_exp")
    st.success(f"Resultado: {base ** exponente}")

elif opcion == "División Entera":
    numerador = st.number_input("Numerador", key="div_ent_1")
    denominador = st.number_input("Denominador", key="div_ent_2")
    if denominador != 0:
        st.success(f"Resultado: {numerador // denominador}")
    else:
        st.error("⚠️ No se puede dividir entre 0")

elif opcion == "Resto de División":
    numerador = st.number_input("Numerador", key="resto_1")
    denominador = st.number_input("Denominador", key="resto_2")
    if denominador != 0:
        st.success(f"Resultado: {numerador % denominador}")
    else:
        st.error("⚠️ No se puede dividir entre 0")

elif opcion == "Promedio de 3 Notas":
    n1 = st.number_input("Nota 1", key="nota1")
    n2 = st.number_input("Nota 2", key="nota2")
    n3 = st.number_input("Nota 3", key="nota3")
    promedio = (n1 + n2 + n3) / 3
    st.success(f"Promedio: {round(promedio, 2)}")

elif opcion == "Promedio Ponderado (5, 12, 20, 15)":
    valores = [5, 12, 20, 15]
    pesos = [1, 2, 3, 4]
    ponderado = sum(v * p for v, p in zip(valores, pesos)) / sum(pesos)
    st.success(f"Promedio Ponderado: {round(ponderado, 2)}")