import requests
from toke import token

print("Friend! Note! If your discord account dont linked with your phone number, your account will be blocked. This is very likely to happen, and the code is not to blame for this! Thanks!")
headers = {
    "authorization": token
}


def join(server_invite):
    """Joins a Discord server using the specified invite link.

    Args:
        server_invite: The invite link to the server.
    """

    try:
        response = requests.post(f"https://discord.com/api/v8/invites/{server_invite}", headers=headers)
        if response.status_code == 200:
            print("Successfully joined server!")
        else:
            print("Failed to join server. Check your token and try again.")
    except Exception as e:
        print(f"Error joining server: {e}")


# Get the server invite from the user
server_invite = input("Your invite link: ")

# Join the server
join(server_invite)


