import requests
from toke import token

headers = {
    "Authorization": token
}


def get_channels(guild_id):
    """Gets a list of channels for the specified Discord server.

    Args:
        guild_id: The ID of the Discord server to get channels for.

    Returns:
        A list of dictionaries containing information about the channels, or `None` if an error occurred.
    """

    try:
        response = requests.get(f"https://discord.com/api/v6/guilds/{guild_id}/channels", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error getting list of channels: {e}")
        return None


# Get the guild ID from the user
guild_id = input("Enter the ID of the server you want to get channels for: ")

# Get the list of channels for the specified server
channels = get_channels(guild_id)

# Check if the list of channels was retrieved successfully
if channels:
    print(f"Channels for server with ID {guild_id}:")
    for channel in channels:
        print(f"Name: {channel['name']}, ID: {channel['id']}")
else:
    print("Could not retrieve list of channels. Check your token and try again.")
