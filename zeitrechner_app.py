import streamlit as st

st.set_page_config(page_title="Zeitrechner", layout="centered")

st.title("⏱ Zeitrechner")

# Session-Status initialisieren
if "gesamt_minuten" not in st.session_state:
    st.session_state.gesamt_minuten = 0
    st.session_state.zeiten_liste = []

# Eingabe
col1, col2, col3 = st.columns(3)
stunden = col1.number_input("Stunden", min_value=0, max_value=1000, step=1, value=0)
minuten = col2.number_input("Minuten", min_value=0, max_value=59, step=1, value=0)
operation = col3.radio("Operation", ["+", "-"], horizontal=True)

# Zeit hinzufügen
if st.button("➕ Zeit hinzufügen"):
    ges_min = stunden * 60 + minuten
    if operation == "+":
        st.session_state.gesamt_minuten += ges_min
    else:
        st.session_state.gesamt_minuten -= ges_min
    st.session_state.zeiten_liste.append((operation, stunden, minuten))

# Liste anzeigen
st.subheader("📋 Hinzugefügte Zeiten:")
if st.session_state.zeiten_liste:
    for i, (op, h, m) in enumerate(st.session_state.zeiten_liste, start=1):
        st.write(f"{i}. {op} {h}h {m}m")  # hier + oder - sichtbar
else:
    st.info("Noch keine Zeiten hinzugefügt.")

# Ergebnis anzeigen
st.subheader("🧮 Ergebnis:")

gesamt = st.session_state.gesamt_minuten
vorz = "-" if gesamt < 0 else ""
std = abs(gesamt) // 60
min_ = abs(gesamt) % 60
dezimal = gesamt / 60

st.success(f"{vorz}{std} Stunden, {min_} Minuten")
st.code(f"{dezimal:.2f} Stunden (Dezimal)", language="text")

# Reset-Button
if st.button("🔄 Zurücksetzen"):
    st.session_state.gesamt_minuten = 0
    st.session_state.zeiten_liste = []
