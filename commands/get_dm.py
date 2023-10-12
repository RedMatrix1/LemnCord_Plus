import requests
from toke import token

headers = {
    "Authorization": token
}

def get_direct_messages():
    """Gets a list of direct messages for the current user.

    Returns:
        A list of dictionaries containing information about the direct messages, or `None` if an error occurred.
    """

    try:
        response = requests.get("https://discordapp.com/api/v6/users/@me/channels", headers=headers)
        if response.status_code != 200:
            print("Could not retrieve list of direct messages. Check your token and try again.")
            return None
        return response.json()
    except Exception as e:
        print(f"Error getting list of direct messages: {e}")
        return None

dms = get_direct_messages()
if dms:
    print("You have the following direct messages: ")
    dms_set = set()
    for dm in dms:
        if dm["type"] == 1: # 1 = DM channel type
            dms_set.add((dm["id"], dm["recipients"][0]["username"]))
    for dm in dms_set:
        print(f"DM ID: {dm[0]}, with user: {dm[1]}")
else:
    print("Could not retrieve list of direct messages. Check your token and try again.")
