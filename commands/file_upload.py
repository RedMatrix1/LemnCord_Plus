import requests

from toke import token

headers = {
    "Authorization": token
}


def upload_file(channel_id, file_path):
    """Uploads a file to the specified Discord channel.

    Args:
        channel_id: The ID of the Discord channel to upload the file to.
        file_path: The path of the file to upload.

    Returns:
        The JSON response from the Discord API if the file was uploaded successfully, or `None` otherwise.
    """

    try:
        files = {"file": open(file_path, "rb")}
        response = requests.post(f"https://discord.com/api/v6/channels/{channel_id}/messages", headers=headers, files=files)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None


# Get the channel ID and file path from the user
channel_id, file_path = input("Enter the ID of the channel you want to upload a file to and the path of the file you want to upload: ").split()

# Upload the file to the Discord channel
response = upload_file(channel_id, file_path)

# Check if the file was uploaded successfully
if response:
    print("File uploaded successfully!")
else:
    print("Could not upload file. Check your token and try again.")
