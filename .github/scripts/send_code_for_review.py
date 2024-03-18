import os
import requests

def send_code_for_review(file_path):
    # Load the code from the file
    with open(file_path, 'r') as file:
        code_content = file.read()

    # Send the code to the ChatGPT API
    # You'll need to replace 'your_chatgpt_endpoint' with the actual endpoint of your model
    chatgpt_response = requests.post(
        'your_chatgpt_endpoint',
        headers={'Authorization': f'Bearer {os.getenv("CHATGPT_API_KEY")}'},
        json={'prompt': code_content}
    )
    feedback = chatgpt_response.json()['choices'][0]['text'].strip()

    return feedback

def post_feedback_to_github(feedback, pull_request_id):
    # Use the GitHub API to post the feedback to the pull request
    # Replace 'your_repo' with your actual repository details
    github_response = requests.post(
        f'https://api.github.com/repos/your_repo/pulls/{pull_request_id}/comments',
        headers={'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'},
        json={'body': feedback}
    )
    print(github_response.json())

# Example file path and pull request ID
file_path = 'path/to/your/code.py'
pull_request_id = 1  # Replace with the actual ID

feedback = send_code_for_review(file_path)
post_feedback_to_github(feedback, pull_request_id)
