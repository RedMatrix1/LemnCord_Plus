import requests
from toke import token

auth = {
    'authorization': token
}


def send_message(channel_id, msg_content):
    """Sends a message to the specified channel.

    Args:
        channel_id: The ID of the channel to send the message to.
        msg_content: The content of the message.

    Returns:
        `True` if the message was sent successfully, or `False` otherwise.
    """

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    msg = {
        "content": msg_content
    }

    try:
        response = requests.post(url, headers=auth, json=msg)
        if response.status_code == 200:
            return True
        else:
            print(f"Failed to send message. Response: {response.text}")
            return False
    except Exception as e:
        print(f"Error sending message: {e}")
        return False


# Get the channel ID from the user
channel_id = input("Channel ID: ")

# Get the message content from the user
msg_content = input("Your Message: ")

# Send the message
if send_message(channel_id, msg_content):
    print("Message sent successfully!")
else:
    print("Failed to send message.")
