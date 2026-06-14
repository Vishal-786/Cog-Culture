import pandas as pd
import streamlit as st

from dotenv import load_dotenv

from pdf import extract_text
from claim import extract_claims
from web import search_claim
from verify import verify_claim

load_dotenv()

st.set_page_config(
    page_title="Fact Check Agent",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Fact Check Agent")

st.markdown(
    """
Upload a PDF document.

The system will:

1. Extract text
2. Detect factual claims
3. Search the web
4. Verify claims
5. Generate a fact-check report
"""
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF Uploaded Successfully")

    with st.spinner("Extracting PDF text..."):

        text = extract_text(uploaded_file)

    with st.expander("View Extracted Text"):
        st.write(text)

    if st.button("Run Fact Check"):

        with st.spinner("Extracting Claims..."):

            claims = extract_claims(text)

        st.subheader("Detected Claims")

        for claim in claims:
            st.write("•", claim)

        results = []

        progress = st.progress(0)

        total = len(claims)

        for idx, claim in enumerate(claims):

            with st.spinner(f"Checking: {claim}"):

                evidence = search_claim(claim)

                verification = verify_claim(
                    claim,
                    evidence
                )

                results.append({
                    "Claim": claim,
                    "Status": verification.get("status"),
                    "Explanation": verification.get("explanation"),
                    "Correct Fact": verification.get("correct_fact")
                })

            progress.progress(
                (idx + 1) / total
            )

        st.success("Fact Checking Complete")

        st.subheader("Fact Check Report")

        df = pd.DataFrame(results)

        st.dataframe(
            df,
            use_container_width=True
        )

        st.download_button(
            label="Download CSV Report",
            data=df.to_csv(index=False),
            file_name="fact_check_report.csv",
            mime="text/csv"
        )