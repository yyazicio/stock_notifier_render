
import json
from analyze import fetch_and_analyze
from notify import send_slack_message, format_message

with open("config.json") as f:
    cfg = json.load(f)

tickers = cfg["INDEXES"]
undervalued, overvalued = fetch_and_analyze(tickers)

text = format_message("Top 5 Undervalued", undervalued) + "\n" + format_message("Top 5 Overvalued", overvalued)
send_slack_message(cfg["SLACK_WEBHOOK_URL"], text)
