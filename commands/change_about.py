import requests
import json
from toke import token


def change_about(about):
    """Changes the user's about text.

    Args:
        about: The desired about text.

    Returns:
        True if the about text was changed successfully, False otherwise.
    """

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    data = {"description": about}
    response = requests.patch("https://discord.com/api/v6/users/@me", headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return True
    else:
        return False


# Example usage:

about = input("Enter your desired about text: ")
if change_about(about):
    print("About text changed successfully!")
else:
    print("Could not change about text. Check your token and try again.")
