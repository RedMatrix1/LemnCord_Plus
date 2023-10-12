import requests
from toke import token

headers = {
    "Authorization": token
}


def leave_server(guild_id):
    """Leaves the specified Discord server.

    Args:
        guild_id: The ID of the server to leave.

    Returns:
        `True` if the server was left successfully, or `False` otherwise.
    """

    try:
        response = requests.delete(f"https://discord.com/api/v6/users/@me/guilds/{guild_id}", headers=headers)
        if response.status_code == 204:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error leaving server: {e}")
        return False


# Get the guild ID from the user
guild_id = input("Enter the ID of the server you want to leave: ")

# Leave the server
if leave_server(guild_id):
    print("Left server successfully!")
else:
    print("Could not leave server. Check your token and try again.")
