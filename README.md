<div align="center">
  
# 🚀 Trade Passport Engine
**Next-Generation Contractor Risk Assessment & Frictionless Financing**

[![Python](https://img.shields.io/badge/Python-Flask-blue?logo=python&logoColor=white)](#)
[![PHP](https://img.shields.io/badge/PHP-Frontend-777BB4?logo=php&logoColor=white)](#)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Styling-38B2AC?logo=tailwind-css&logoColor=white)](#)
[![Vercel](https://img.shields.io/badge/Vercel-Deployed-000000?logo=vercel&logoColor=white)](#)

</div>

<br/>

## 💡 The Problem
In the construction and B2B supply chain industry, late payments and defaults are a massive problem. Suppliers take on 100% of the risk when delivering materials, often waiting 90+ days for payment, crippling their cash flow and stalling business growth.

## 🎯 Our Solution
**Trade Passport Engine** is an intelligent risk-assessment and financial routing platform. It aggregates payment behaviors, historical data, and real-time **LHDN (Lembaga Hasil Dalam Negeri) e-Invoice** verification to generate a dynamic **"Trade Passport Health"** score for contractors.

By scoring contractors as **Prime, Amber, or Toxic**, our engine allows businesses to make data-driven decisions on whether to extend credit, demand cash upfront, or instantly route invoices to institutional financing partners.

---

## ✨ Key Features

- **📊 Dynamic Trade Passport Metrics**: Analyzes Transaction Frequency, Payment Habits (promised vs. actual payment days), Years of Cooperation, and Invoice Amount Trends.
- **🏛️ Real-time LHDN e-Invoice Sync (Simulated)**: Leverages official tax data to verify transaction legitimacy and ensure compliance.
- **🚦 Smart Triage Router**: 
  - 🟢 **Prime**: Frictionless processing for highly reliable payers.
  - 🟡 **Amber**: Cautionary processing highlighting a history of late payments.
  - 🔴 **Toxic**: High-default risk alerts requiring explicit manual override to proceed with delivery.
- **💸 Seamless Institutional Financing**: One-click integration to instantly route eligible Accounts Receivable (AR) to financing partners (like CapBay) for immediate cash flow.

---

## 🛠️ Tech Stack

- **Frontend**: PHP, HTML5, TailwindCSS (for a sleek, modern, and responsive UI)
- **Backend**: Python (Flask API, handling the logic and algorithmic scoring)
- **Deployment**: Vercel (`vercel.json` configured for seamless serverless deployment)

---

## 🚀 How It Works

1. **Dashboard View**: View all active contractors and their outstanding Accounts Receivable.
2. **Passport Evaluation**: Select a contractor to generate their Trade Passport. The engine simulates a sync with LHDN e-Invoice APIs and calculates a payment velocity score.
3. **Actionable Insights**: The dashboard presents the contractor's health status. 
4. **The CapBay Bridge**: If an invoice needs immediate liquidity, users can click **"Submit AR to CapBay"** to instantly request institutional financing based on the generated Trade Passport score.

---

## 🏆 Why It Wins
**Trade Passport Engine** doesn't just assess risk—it actively bridges the gap between B2B suppliers and institutional financing. By integrating credit scoring directly into the delivery and invoicing workflow, we solve the cash flow bottleneck that has plagued the supply chain industry for decades.

<br/>

<div align="center">
  <i>Built with ❤️ for NexHack</i>
</div>
