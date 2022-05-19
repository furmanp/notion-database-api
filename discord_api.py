import requests


def fetchDiscordMembers(invite_url):
    invite_url = invite_url.split('invite/')[-1]

    url = f'https://discord.com/api/v9/invites/{invite_url}'

    params = {'with_counts': 'True',
              'with_expiration': 'True'
              }
    try:
        response = requests.request('GET', url=url, params=params)
        response = response.json()

        return response['approximate_member_count']

    except:
        return 'N/A'
