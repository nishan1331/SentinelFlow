import streamlit as st
import pandas as pd
from scapy.all import sniff, IP, TCP, UDP
import time
import plotly.express as px

# Setup page
st.set_page_config(page_title="SentinelFlow", layout="wide")
st.title("🛡️ SentinelFlow: Network Data Pipeline")

# Initialize data log if it doesn't exist
if 'data_log' not in st.session_state:
    st.session_state['data_log'] = pd.DataFrame(columns=["Time", "Source", "Destination", "Protocol", "Length"])

# THE DIRECT FIX: Sniff a few packets every refresh
# This bypasses the thread blocking issues in Kali
def capture_now():
    # Sniff 5 packets quickly on eth0
    packets = sniff(iface="eth0", count=5, timeout=1)
    new_entries = []
    for pkt in packets:
        if pkt.haslayer(IP):
            new_entries.append({
                "Time": time.strftime("%H:%M:%S"),
                "Source": pkt[IP].src,
                "Destination": pkt[IP].dst,
                "Protocol": "TCP" if pkt.haslayer(TCP) else "UDP" if pkt.haslayer(UDP) else "Other",
                "Length": len(pkt)
            })
    if new_entries:
        new_df = pd.DataFrame(new_entries)
        st.session_state['data_log'] = pd.concat([st.session_state['data_log'], new_df], ignore_index=True)

# Run the capture
capture_now()

# UI Display
col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("Live Traffic Stream")
    st.dataframe(st.session_state['data_log'].tail(15), width=1000)

with col2:
    st.subheader("Security Insights")
    if not st.session_state['data_log'].empty:
        # Pie Chart
        proto_counts = st.session_state['data_log']['Protocol'].value_counts()
        fig = px.pie(values=proto_counts.values, names=proto_counts.index, title="Protocol Split")
        st.plotly_chart(fig)
        
        # Metrics
        st.metric("Total Packets", len(st.session_state['data_log']))
        
        # --- SECURITY ALERT LOGIC ---
        heavy_hitters = st.session_state['data_log']['Source'].value_counts()
        # Changed to 10 so you can see it trigger with just a few pings!
        if heavy_hitters.max() > 10: 
            st.error(f"⚠️ FLOOD DETECTED: {heavy_hitters.idxmax()}")
# Auto-refresh
time.sleep(1)
st.rerun()


