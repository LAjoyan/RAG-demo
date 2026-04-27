import streamlit as st
import httpx

API_URL = "http://localhost:8000"


def layout():
    st.markdown("# RAGnimals")
    st.markdown("Ask me about tigers, fishes, rabbits, crabs ans pandas")


if __name__ == "__main__":
    layout()
