import twitter_api
import telegram_api
from discord_api import fetchDiscordMembers
import coingecko_api
import coinmarketcap_api as cmc
from dotenv import load_dotenv


def configure():
    load_dotenv()


def main():
    configure()

    data = cmc.GetLatestCoins()
    print(cmc.GetCoinID(data, 'merit circle'))



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

