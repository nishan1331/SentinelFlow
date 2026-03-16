# SentinelFlow
A real-time Network Data Pipeline built on Kali Linux. Integrates Scapy for packet ingestion, Pandas for ETL processing, and Streamlit for security visualization and flood detection.


# SentinelFlow: Integrated Network Data Pipeline

SentinelFlow is a standalone security monitoring tool designed for Kali Linux. It treats raw network traffic as a streaming data source, applying Data Engineering principles to provide real-time Security Insights.

# Technical Architecture
- **Networking:** Real-time packet ingestion from `eth0` using Scapy.
- **Data Engineering:** Developed a synchronous polling pipeline to transform raw packet headers into structured Pandas DataFrames.
- **Security:** Real-time visualization of protocol distribution and automated Flood (DoS) detection logic.

# Installation & Usage
1. Clone: `git clone https://github.com/nishan1331/SentinelFlow.git`
2. Install: `pip install -r requirements.txt`
3. Run (Requires Root): `sudo streamlit run sentinel.py`

# Dashboard Features
- **Live Traffic Stream:** Real-time monitoring of Source/Destination IPs and protocols.
- **Protocol Analysis:** Interactive Plotly charts showing TCP/UDP/ICMP distribution.
- **Anomalous Traffic Detection:** Automated red-alert triggers for high-velocity IP traffic.
<img width="1715" height="779" alt="dashboard_demo" src="https://github.com/user-attachments/assets/3cf9935c-fd76-487b-9dc5-cbc034b6c91e" />
