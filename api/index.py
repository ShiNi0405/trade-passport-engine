import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MOCK_DB = {
    "chuan_luck": {
        "contractor_name": "Chuan Luck Construction",
        "promised_days": 60,
        "actual_days": 67,
        "transaction_frequency": "High",
        "frequency_rate": "3.2× / month",
        "years_cooperation": 8,
        "amount_trend": "Growing",
        "total_transacted": "RM 2.4M",
        "verified_ratio": 21 / 24, # 0.875
        "lhdn_verified": True,
        "exact_scores": {
            "timeliness": 218,
            "frequency": 176,
            "coop": 180,
            "trend": 120,
            "verification": 88
        }
    },
    "kl_premier": {
        "contractor_name": "KL Premier Builders",
        "promised_days": 60,
        "actual_days": 78,
        "transaction_frequency": "Medium",
        "frequency_rate": "1.8× / month",
        "years_cooperation": 3,
        "amount_trend": "Stable",
        "total_transacted": "RM 850k",
        "verified_ratio": 1.0,
        "lhdn_verified": True,
        "exact_scores": {
            "timeliness": 145,
            "frequency": 120,
            "coop": 130,
            "trend": 90,
            "verification": 150
        }
    },
    "sunrise": {
        "contractor_name": "Sunrise Contractors",
        "promised_days": 60,
        "actual_days": 110,
        "transaction_frequency": "Low",
        "frequency_rate": "0.8× / month",
        "years_cooperation": 2,
        "amount_trend": "Shrinking",
        "total_transacted": "RM 310k",
        "verified_ratio": 0.5,
        "lhdn_verified": False,
        "exact_scores": {
            "timeliness": 65,
            "frequency": 60,
            "coop": 110,
            "trend": 45,
            "verification": 40
        }
    }
}

@app.route('/api/evaluate', methods=['GET'])
def evaluate():
    contractor_id = request.args.get('id', 'chuan_luck')
    
    # 1. Retrieve base data or fallback
    data = MOCK_DB.get(contractor_id)
    if not data:
        # Generate default data structure for custom contractors
        data = {
            "contractor_name": request.args.get('name', 'Custom Client'),
            "promised_days": int(request.args.get('promised', 60)),
            "actual_days": int(request.args.get('actual', 75)),
            "transaction_frequency": request.args.get('frequency', 'Medium'),
            "frequency_rate": request.args.get('frequency_rate', '1.5× / month'),
            "years_cooperation": int(request.args.get('coop', 3)),
            "amount_trend": request.args.get('trend', 'Stable'),
            "total_transacted": request.args.get('total_transacted', 'RM 500k'),
            "verified_ratio": float(request.args.get('verified_ratio', 0.8)),
            "lhdn_verified": request.args.get('lhdn', 'true').lower() == 'true',
            "exact_scores": None
        }

    # 2. Extract parameters with query overrides
    promised = int(request.args.get('promised', data['promised_days']))
    actual = int(request.args.get('actual', data['actual_days']))
    frequency = request.args.get('frequency', data['transaction_frequency'])
    coop = int(request.args.get('coop', data['years_cooperation']))
    trend = request.args.get('trend', data['amount_trend'])
    verified_ratio = float(request.args.get('verified_ratio', data['verified_ratio']))
    lhdn = request.args.get('lhdn', str(data['lhdn_verified'])).lower() == 'true'

    # Check if overrides are active (if any parameter differs from base mock)
    has_overrides = (
        promised != data['promised_days'] or
        actual != data['actual_days'] or
        frequency != data['transaction_frequency'] or
        coop != data['years_cooperation'] or
        trend != data['amount_trend'] or
        verified_ratio != data['verified_ratio'] or
        lhdn != data['lhdn_verified']
    )

    # 3. Math Engine - Compute Credit Score Out of 1000
    if data['exact_scores'] and not has_overrides:
        # Use exact preset scores for mock demo consistency
        scores = data['exact_scores']
    else:
        # Calculate dynamically
        # A. Payment Timeliness (max 300)
        ratio = promised / max(actual, 1.0)
        if ratio >= 1.0:
            timeliness = 300
        elif ratio >= 0.85:
            timeliness = 180 + (ratio - 0.85) / 0.15 * 120
        elif ratio >= 0.5:
            timeliness = 60 + (ratio - 0.5) / 0.35 * 120
        else:
            timeliness = ratio / 0.5 * 60
        timeliness = round(min(300, max(0, timeliness)))

        # B. Transaction Frequency (max 200)
        if frequency == "High":
            freq_score = 176
        elif frequency == "Medium":
            freq_score = 120
        else:
            freq_score = 60

        # C. Cooperation History (max 200)
        coop_score = round(min(200, 90 + 11 * coop))

        # D. Volume Trend (max 150)
        if trend == "Growing":
            trend_score = 120
        elif trend == "Stable":
            trend_score = 90
        else:
            trend_score = 45

        # E. Verification Ratio (max 150)
        if verified_ratio >= 1.0:
            verification_score = 150
        else:
            verification_score = round(100 * verified_ratio)

        scores = {
            "timeliness": timeliness,
            "frequency": freq_score,
            "coop": coop_score,
            "trend": trend_score,
            "verification": verification_score
        }

    total_score = sum(scores.values())

    # 4. Triage Router
    # Score ranges: Prime (>= 680), Amber (>= 500), Toxic (< 500)
    if total_score >= 680:
        status, msg = "Prime", "Eligible for 1.2% CapBay Premium Financing"
    elif total_score >= 500:
        status, msg = "Amber", "Eligible for 2.5% CapBay Standard Financing"
    else:
        status, msg = "Toxic", "Rejected for Financing. Supplier holds 100% Risk"

    # 5. Simulated API Delay for visual experience
    time.sleep(0.8)

    # 6. Payload Construction
    return jsonify({
        "contractor_name": data['contractor_name'],
        "trade_passport": {
            "transaction_frequency": data['frequency_rate'] if 'frequency_rate' in data else frequency,
            "years_cooperation": coop,
            "amount_trend": trend,
            "payment_days": actual,
            "promised_days": promised,
            "total_transacted": data['total_transacted'],
            "verification_ratio_label": f"{round(verified_ratio * 24)} / 24",
            "scores": scores,
            "total_score": total_score,
            "lhdn_verified": lhdn,
            "lhdn_timestamp": "2026-06-28T08:30:00Z"
        },
        "advisory_action": {
            "status": status,
            "funder_message": msg
        }
    })


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "uptime": "100%"})
