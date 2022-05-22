import twitter_api
import telegram_api
from discord_api import fetchDiscordMembers
import coingecko_api
import notion_api
import coinmarketcap_api as cmc
from dotenv import load_dotenv
import json


def configure():
    load_dotenv()


def main():
    configure()

    new_records = notion_api.FetchNewEntries()

    for record in new_records:
        coin_name = record['properties']['Coin']['title'][0]['text']['content']
        page_id = record['id']
        coin_info = coingecko_api.GetCoinData(coingecko_api.GetCoinId(coin_name))
        print(f'{coin_name}. ID: {[page_id]}. INFO: {coin_info}')


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

