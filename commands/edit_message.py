import requests
from toke import token

headers = {
    "Authorization": token
}

# Get the channel ID and message ID from the user
channel_id, message_id = input("Input channel ID and message ID: ").split()

# Get the new content of the message from the user
new_content = input("Edited text: ")

# Send a PATCH request to the Discord API to edit the message
try:
    response = requests.patch(
        f"https://discord.com/api/v6/channels/{channel_id}/messages/{message_id}",
        headers=headers,
        json={"content": new_content},
    )

    # Check if the request was successful
    if response.status_code == 200:
        print("Message successfully edited")
    else:
        print("Failed to edit message")
except Exception as e:
    print(f"Error editing message: {e}")
