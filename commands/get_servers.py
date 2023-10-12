import requests
from toke import token

headers = {
    "Authorization": token
}

def get_guilds():
    """Gets a list of guilds that the current user is a member of.

    Returns:
        A list of dictionaries containing information about the guilds, or `None` if an error occurred.
    """

    try:
        response = requests.get("https://discord.com/api/v6/users/@me/guilds", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error getting list of guilds: {e}")
        return None

guilds = get_guilds()
if guilds:
    print("You are a member of the following servers:")
    for guild in guilds:
        print(f"Name: {guild['name']}, ID: {guild['id']}")
else:
    print("Could not retrieve list of servers. Check your token and try again.")
