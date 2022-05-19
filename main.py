import twitter_api
import telegram_api
import discord_api
import coingecko_api
from coinmarketcap_api import GetMarketData
from dotenv import load_dotenv


def configure():
    load_dotenv()


def main():
    configure()


main()

# response = {'name': coin_details['name'],
#             'ticker': coin_details['ticker'],
#             'market_cap': coin_details['market_cap'],
#             'profile_image_url': coin_details['profile_image_url'],
#             'website': coin_socials['website'],
#             'discord': coin_socials['discord'],
#             'twitter': coin_socials['twitter'],
#             'telegram': coin_socials['telegram'],
#             'discord_members': discord_members,
#             'twitter_followers': twitter_params['followers_count'],
#             'telegram_members': telegram_members}

