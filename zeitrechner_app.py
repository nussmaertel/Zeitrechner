import streamlit as st

st.set_page_config(page_title="Zeitrechner", layout="centered")

st.title("⏱ Zeitrechner")

if "gesamt_minuten" not in st.session_state:
    st.session_state.gesamt_minuten = 0
    st.session_state.zeiten_liste = []

col1, col2, col3 = st.columns([1, 1, 2])
stunden = col1.number_input("Stunden", min_value=0, max_value=1000, step=1, value=0, key="stunden_input")
minuten = col2.number_input("Minuten", min_value=0, max_value=59, step=1, value=0, key="minuten_input")
operation = col3.radio("Operation", ["+", "-"], index=0, horizontal=True)

zeit_hinzufuegen = st.button("➕ Zeit übernehmen")

if zeit_hinzufuegen:
    ges_min = stunden * 60 + minuten
    if operation == "+":
        st.session_state.gesamt_minuten += ges_min
        op_str = "+ "
    else:
        st.session_state.gesamt_minuten -= ges_min
        op_str = "- "

    st.session_state.zeiten_liste.append(f"{op_str}{stunden}h {minuten}min")
    st.experimental_rerun()

st.subheader("📋 Bisherige Eingaben:")
if st.session_state.zeiten_liste:
    for i, eintrag in enumerate(st.session_state.zeiten_liste, start=1):
        st.write(f"{i}. {eintrag}")
else:
    st.info("Noch keine Zeiten hinzugefügt.")

gesamt = st.session_state.gesamt_minuten
vorz = "-" if gesamt < 0 else ""
std = abs(gesamt) // 60
min_ = abs(gesamt) % 60
dezimal = gesamt / 60

st.subheader("🧮 Ergebnis:")
st.success(f"{vorz}{std} Stunden, {min_} Minuten")
st.code(f"{dezimal:.2f} Stunden (Dezimal)", language="text")

reset = st.button("🔄 Alles zurücksetzen")
if reset:
    st.session_state.gesamt_minuten = 0
    st.session_state.zeiten_liste = []
    st.experimental_rerun()
