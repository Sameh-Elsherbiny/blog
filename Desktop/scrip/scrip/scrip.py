from twitter_scraper_selenium import scrape_profile
import json
from datetime import datetime, timedelta
import pytz

accounts = ['Mr_Derivatives','warrior_0719','ChartingProdigy','allstarcharts','yuriymatso','TriggerTrades','AdamMancini4','CordovaTrades','Barchart','RoyLMattox']

def get_stock_symbol():
    """Get the stock symbol from the user."""
    stock_symbol = input("Please enter the stock symbol (e.g., $TSLA): ").capitalize()
    return stock_symbol

def get_duration():
    """Get the duration in minutes from the user."""
    duration = int(input("Please enter the duration in minutes: "))
    return duration

def scrape_tweets(accounts, stock_symbol, duration):
    """Scrape tweets for each account."""
    timezone = pytz.timezone('UTC')
    mention_count = 0

    for account in accounts:
        tweets_body = scrape_profile(twitter_username=account, output_format="json", browser="firefox")
        data_dict = json.loads(tweets_body)

        for tweet_id, tweet_details in data_dict.items():
            datetime_obj = datetime.fromisoformat(tweet_details['posted_time']).replace(tzinfo=timezone)
            time_interval = datetime.now(timezone) - timedelta(minutes=duration)

            if stock_symbol in tweet_details['content'] and datetime_obj >= time_interval:
                mention_count += 1

    return mention_count

if __name__ == "__main__":
    stock_symbol = get_stock_symbol()
    duration = get_duration()
    mention_count = scrape_tweets(accounts, stock_symbol, duration)
    print(f"The stock symbol {stock_symbol} was mentioned {mention_count} times within the last {duration} minutes.") 
