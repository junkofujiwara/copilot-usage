# GitHub Copilot Usage

## Introduction
This script generates csv files with the following information about usage of GitHub Copilot.
- summary: day, total_suggestions_count, total_acceptances_count, total_lines_suggested, total_lines_accepted, total_active_users, total_chat_acceptances, total_chat_turns, total_active_chat_users
- breakdown: day, language, editor, suggestions_count, acceptances_count, lines_suggested, lines_accepted, active_users


## Requirements
- Python 3.6 or higher
- GitHub Owner permissions and GitHub Personal Access Token (See API reference for specific permission and token)
- `pip install -r requirements.txt`

### Usage
For Enterprise Usage<br>
`python usage.py -s <enterprise_slug> -t <github_token>`

For Organization Usage<br>
`python usage.py -o <organization> -t <github_token>`

### Reference
https://docs.github.com/en/enterprise-cloud@latest/rest/copilot/copilot-usage?apiVersion=2022-11-28