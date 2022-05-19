import json
import requests
import os


def createPage(databaseId, response):
    createUrl = 'https://api.notion.com/v1/pages'
    token = os.getenv('NOTION_SECRET')

    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
        'Notion-Version': '2022-02-22'
    }

    newPageData = {
        "parent": {"database_id": databaseId},
        "icon": {
            'type': 'external',
            'external': {
                'url': response['profile_image_url']
            }
        },
        "properties": {
            "Coin": {
                "title": [
                    {
                        "text": {
                            "content": response['name']
                        }
                    }
                ]
            },
            "Market": {
                "select": {
                    "name": "market_name"
                }
            },
            "Network": {
                "select": {
                    "name": "network_name"
                }
            },
            "Market Cap": {
                "number": response['market_cap']
            },
            "Ticker": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": response['ticker']
                        }
                    }
                ]
            },
            "Website": {
                "url": response['website']
            },
            "Twitter": {
                "url": response['twitter']
            },
            "Discord": {
                "url": response['discord']
            },
            "Telegram": {
                "url": response['telegram']
            },
            "Discord members": {
                'number': response['discord_members']
            },
            "Twitter followers": {
                'number': response['twitter_followers']
            },
            "Telegram members": {
                'number': response['telegram_members']
            }
        }
    }

    data = json.dumps(newPageData)
    res = requests.request("POST", createUrl, headers=headers, data=data)
    return res.status_code
