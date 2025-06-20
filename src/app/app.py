import os

import streamlit as st
from databricks.sdk import WorkspaceClient

# Set page title
st.set_page_config(page_title="Hello World App", page_icon="🚀")

st.title("Hello World App")
st.write("This is a Streamlit app that lets you trigger a Databricks job.")

JOB_ID = os.getenv("JOB_ID")

# Only create WorkspaceClient if we're not in a test environment
if not os.getenv("TESTING"):
    try:
        w = WorkspaceClient()
        st.success("Connected to Databricks workspace!")
    except Exception as e:
        st.error(f"Failed to connect to Databricks: {e}")
        st.stop()

if JOB_ID:
    if st.button(f"Trigger job with ID {JOB_ID}"):
        try:
            response = w.jobs.run_now(job_id=JOB_ID)
            st.success("Job started successfully!")
        except Exception as e:
            st.error(f"Error starting job: {e}")
else:
    st.warning("No JOB_ID environment variable found.") 