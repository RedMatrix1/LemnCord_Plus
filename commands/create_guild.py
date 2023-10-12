import requests
from toke import token


def create_server(server_name):
    """Creates a new Discord guild with the specified name.

    Args:
        server_name: The desired guild name.

    Returns:
        The JSON response from the Discord API containing information about the newly created guild.
    """

    headers = {
        "Authorization": f"{token}"
    }

    payload = {
        "name": f"{server_name}"
    }

    response = requests.post("https://discord.com/api/v9/guilds", headers=headers, json=payload)

    return response.json()



server_name = input("Name of your guild: ")
response = create_server(server_name)

print(response)
