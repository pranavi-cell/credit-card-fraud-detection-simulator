from datetime import datetime, timedelta

# store transaction history for each card
card_data = {}

def detect_fraud(card_number, amount, location):

    global card_data

    fraud_score = 0
    alerts = []

    location = location.lower().strip()

    current_time = datetime.now()

    # create record for new card
    if card_number not in card_data:
        card_data[card_number] = {
            "transaction_times": []
        }

    card = card_data[card_number]

    # store transaction time
    card["transaction_times"].append(current_time)

    # keep only transactions within last 60 seconds
    card["transaction_times"] = [
        t for t in card["transaction_times"]
        if current_time - t < timedelta(seconds=60)
    ]

    # Amount risk levels
    if amount > 50000:
        fraud_score += 35
        alerts.append("Very high transaction amount")

    elif amount > 25000:
        fraud_score += 20
        alerts.append("High transaction amount")

    elif amount > 10000:
        fraud_score += 10
        alerts.append("Moderately high transaction amount")

    # Rapid transaction detection
    if len(card["transaction_times"]) > 3:
        fraud_score += 30
        alerts.append("Too many transactions in short time")

    return fraud_score, alerts