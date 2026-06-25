import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MOCK_DB = {
    "ah_meng": {
        "contractor_name": "Ah Meng Construction",
        "promised_days": 30,
        "actual_days": 32,
        "transaction_frequency": "14/month",
        "years_cooperation": 8,
        "amount_trend": "+12% (Growing)",
        "lhdn_verified": True
    },
    "maju_jaya": {
        "contractor_name": "Maju Jaya Builders",
        "promised_days": 60,
        "actual_days": 85,
        "transaction_frequency": "Medium frequency",
        "years_cooperation": 4,
        "amount_trend": "+2% (Stable)",
        "lhdn_verified": True
    },
    "skudai_steel": {
        "contractor_name": "Skudai Steelworks",
        "promised_days": 30,
        "actual_days": 110,
        "transaction_frequency": "Low frequency",
        "years_cooperation": 1,
        "amount_trend": "-15% (Shrinking)",
        "lhdn_verified": False
    }
}

@app.route('/api/evaluate', methods=['GET'])
def evaluate():
    contractor_id = request.args.get('id', 'maju_jaya') # default to average if nothing specified
    
    # DEMO SAFETY: Fallback to average profile if not found
    data = MOCK_DB.get(contractor_id, MOCK_DB['maju_jaya'])
    
    # 1. Math Engine (Safe from Div-by-Zero)
    safe_actual = max(data['actual_days'], 1)
    velocity = data['promised_days'] / safe_actual
    
    # 2. Triage Router
    if velocity >= 0.85:
        status, msg = "PRIME", "Eligible for 3% CapBay Premium Financing"
    elif velocity >= 0.50:
        status, msg = "AMBER", "Eligible for 8% CapBay Standard Financing"
    else:
        status, msg = "TOXIC", "Rejected for Financing. Defong holds 100% Risk"
        
    # 3. Simulated API Delay (The "Wow" factor)
    time.sleep(0.8)

    # 4. Payload Construction
    return jsonify({
        "contractor_name": data['contractor_name'],
        "trade_passport": {
            "transaction_frequency": data['transaction_frequency'],
            "years_cooperation": data['years_cooperation'],
            "amount_trend": data['amount_trend'],
            "payment_velocity_score": round(velocity, 2),
            "algorithm_confidence": "96.4%",
            "lhdn_verified": data['lhdn_verified'],
            "lhdn_timestamp": "2024-03-15T08:30:00Z"
        },
        "advisory_action": {
            "status": status,
            "funder_message": msg
        }
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "uptime": "100%"})
