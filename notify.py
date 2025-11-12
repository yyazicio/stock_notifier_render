
import requests

def send_slack_message(webhook_url, text):
    payload = {"text": text}
    requests.post(webhook_url, json=payload)

def format_message(title, df):
    msg = f"*{title}*\n"
    for _, row in df.iterrows():
        msg += f"{row['Name']} ({row['Ticker']}) — P/E: {row['P/E']:.2f}, P/B: {row['P/B']:.2f}, PEG: {row['PEG']:.2f}\n"
    return msg
