from database import create_database, insert_transaction
from fraud_rules import detect_fraud
from datetime import datetime

def main():

    create_database()

    print("Credit Card Fraud Detection Simulator\n")

    while True:

        card = input("Enter card number: ")
        amount = float(input("Enter transaction amount: "))
        location = input("Enter location: ")

        time = datetime.now()

        insert_transaction(card, amount, location, str(time))

        score, alerts = detect_fraud(card, amount, location)

        print("\nFraud Risk Score:", score)

        if score >= 50:
            print("⚠ Suspicious Transaction Detected")

        if alerts:
            print("Reasons:")
            for reason in alerts:
                print("-", reason)
        else:
            print("Transaction appears normal")

        cont = input("\nDo another transaction? (y/n): ")
        if cont.lower() != "y":
            break


main()