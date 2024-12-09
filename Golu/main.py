import cloudscraper
import requests

# Step 1: Set up Cloudscraper with headers to mimic a browser
scraper = cloudscraper.create_scraper()

# Custom headers to mimic browser behavior from cURL
headers = {
    "authority": "www.fakepersongenerator.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "__gads=ID=19afe8654c49ab24:T=1733710805:RT=1733710805:S=ALNI_Ma29FOkyR_Kwbhhyx0UX8BZUUUWig; __gpi=UID=00000f87da838ea1:T=1733710805:RT=1733710805:S=ALNI_Ma2GmfmnthmF-wJs4RUzR9BPRIupA; __eoi=ID=0a098a4461a5d25e:T=1733710805:RT=1733710805:S=AA-AfjZE-3FrV8OgvVxX7zTmvmUC; FCNEC=%5B%5B%22AKsRol8nglgREzAuLx1TmOOqSTUpa71iCb7VDj4ZiZsGg-LItqJDhVXgY88QuZBldPxGNGAEMBfZrvLabQd_FwTDgn92Je36nCUcK2WCEfyUdvrNnjsF46EBeO1xgtcBxbjRquFbzGJeIGhRQlWpHioEiZZrhXDQWQ%3D%3D%22%5D%5D; PHPSESSID=5o683a5ll9ntvrp2qodgpoe7r7; cf_clearance=RRwqDBP_c5_jC2TpPTeGRQSEeZKyxoUNaekxBc0CyI8-1733719121-1.2.1.1-fiSaIPrLwOZC.GOcOfjKYKIKfEryUlmRngp_AYoARnHoJQPNh4VzFNEYJO5UMzJYgYoYD0rP6Z5CQEj90e52x3ET9zxv41mONmReoT_NVR2WWjO.d_M8eDT2LLXoNOZNxrkU3h4wDiGRqkwyiWm05pyj0yPbCvE1OuXy2E2_.cYWuJnhcuVhgOQ3difZsxPaUcMZFV5JsBB9LCDY4j2w28RdoeM.jwxqr4XK_PP6zQ0DknlzKOo4kC02yl426qHywH7HsSI6_r0Q5DcCUNvcuNXcJwtjiiBNUBi.aJFP.Dm8AvJppAeLo_Azov8OfTDwsORjm8PSLYbp_a_9ePv5G5APG8SuoYeXNLdx0IQCnt3KY1tXHkYVIjJCgLXLynGdCfKw_InJJwhuwYL.4gEdM6dQToM989cG2oms9qdyVGrdmQ6i3pXT0j6Lsd3MvFGG; sc_is_visitor_unique=rx11380196.1733719125.4F9181A3869C44DF98025A6ACB452519.2.2.2.1.1.1.1.1.1",
    "origin": "https://www.fakepersongenerator.com",
    "referer": "https://www.fakepersongenerator.com/Random1/credit_card_generator",
    "sec-ch-ua": '"Not-A.Brand";v="99", "Chromium";v="124"',
    "sec-ch-ua-arch": '""',
    "sec-ch-ua-bitness": '""',
    "sec-ch-ua-full-version": '"124.0.6327.4"',
    "sec-ch-ua-full-version-list": '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-model": '"V2315"',
    "sec-ch-ua-platform": '"Android"',
    "sec-ch-ua-platform-version": '"14.0.0"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
}

# Define URL for POST request
url = "https://www.fakepersongenerator.com/credit_card_generator"

# Data to send in the POST request (from cURL)
data = {
    "type": "0",
    "quantity": "20",
    "country": "0"
}

# Step 2: Fetch the webpage content with the headers and data
try:
    # Make POST request using Cloudscraper
    response = scraper.post(url, headers=headers, data=data)
    response.raise_for_status()  # Check if the request was successful

    # Step 3: If the response is successful, send the data to Telegram
    if response.status_code == 200:
        print("Request was successful!")

        # Parse the response (this is the HTML, adjust as needed)
        credit_card_data = response.text  # This will be the raw HTML or the response data

        # Telegram bot details
        telegram_bot_token = "7789129873:AAFTbKbZy8RB84RwvseTugifweyqIncOqnU"
        chat_id = "-1002002108311"  # Example: "-1002002108311" (for group chat)
        telegram_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"

        # Message to send
        message = f"Credit Card Data:\n{credit_card_data}"

        # Send the message to Telegram
        telegram_response = requests.post(telegram_url, data={"chat_id": chat_id, "text": message})

        # Check if the message was successfully sent
        if telegram_response.status_code == 200:
            print("Message sent to Telegram successfully!")
        else:
            print(f"Failed to send message to Telegram: {telegram_response.text}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
