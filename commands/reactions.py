import requests
import json
from toke import token


headers = {
    "Authorization": token,
}


def add_reaction(message_id, channel_id, emoji_name):
    """Adds a reaction to the specified message.

    Args:
        message_id: The ID of the message to add the reaction to.
        channel_id: The ID of the channel where the message is located.
        emoji_name: The name of the emoji to add.

    Returns:
        `True` if the reaction was added successfully, or `False` otherwise.
    """

    url = f"https://discordapp.com/api/v6/channels/{channel_id}/messages/{message_id}/reactions/{emoji_name}/@me"

    try:
        response = requests.put(url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to add reaction. Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error adding reaction: {e}")
        return False


# Get the message ID and channel ID from the user
message_id = input("Message ID: ")
channel_id = input("Channel ID: ")

# Get the emoji name from the user
emoji_name = input("Emoji Name: ")

# Add the reaction to the message
if add_reaction(message_id, channel_id, emoji_name):
    print("Reaction added successfully")
else:
    print("Failed to add reaction.")
