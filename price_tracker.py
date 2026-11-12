from datetime import datetime
import requests

url = "https://api.coingecko.com/api/v3/simple/price"

targets = {
    "bitcoin": 95000,
    "chainlink": 10.50,
    "the-graph": 0.015,
    "celo": 0.07
}

params = {
    "ids": ",".join(targets.keys()),
    "vs_currencies": "usd"
}

try:
    # 1. Send the request
    response = requests.get(url, params=params, timeout=10)
    
    # 2. Immediately raise an error if the status code is bad (e.g., 404 or 429)
    response.raise_for_status()
    
    data = response.json()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alerts = []

    for coin, target_price in targets.items():
        # 3. Safely check that the coin actually exists in the returned JSON
        if coin not in data:
            print(f"Warning: '{coin}' was not found in API response. Check the CoinGecko API ID.")
            continue

        current_price = data[coin]["usd"]
        print(f"{coin.upper()}: ${current_price} (Target: <= ${target_price})")

        if current_price <= target_price:
            alerts.append(f"[{now}] ALERT: {coin.upper()} hit ${current_price} (Target: ${target_price})")

    if alerts:
        with open("market_alerts.log", "a") as log_file:
            for alert in alerts:
                log_file.write(alert + "\n")
        print(f"\nSaved {len(alerts)} alert(s) to market_alerts.log!")
    else:
        print("\nNo price targets hit.")

except requests.exceptions.Timeout:
    print("Network Error: CoinGecko took longer than 10 seconds to respond.")
except requests.exceptions.HTTPError as err:
    print(f"API Error: Server returned an error status ({err}).")
except requests.exceptions.RequestException as err:
    print(f"Connection Error: Could not reach the internet ({err}).")