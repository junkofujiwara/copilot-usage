#!/usr/bin/env python3
# -*- coding: utf_8 -*-
'''github.py'''
import logging
import requests

class Github:
    '''Github class'''
    def __init__(self, endpoint, slug, org, token):
        self.endpoint = endpoint
        self.slug = slug
        self.org = org
        self.token = token

    def get_usage(self, isEnteprise):
        """get usage"""
        usage_summary = []
        usage_brakdown = []
        if isEnteprise is True:
            endpoint_url = f'{self.endpoint}/enterprises/{self.slug}/copilot/usage?per_page=28'
        else:
            endpoint_url = f'{self.endpoint}/orgs/{self.org}/copilot/usage?per_page=28'
        logging.log(logging.INFO, "Getting usage information from %s", endpoint_url)
        while endpoint_url:
            response = requests.get(endpoint_url, headers={'Authorization': f'bearer {self.token}'})
            if response.status_code == 200:
                response_json = response.json()
                for data in response_json:
                    usage_summary.append({'day': data['day'],
                                          'total_suggestions_count': data['total_suggestions_count'],
                                            'total_acceptances_count': data['total_acceptances_count'],
                                            'total_lines_suggested': data['total_lines_suggested'],
                                            'total_lines_accepted': data['total_lines_accepted'],
                                            'total_active_users': data['total_active_users'],
                                            'total_chat_acceptances': data['total_chat_acceptances'],
                                            'total_chat_turns': data['total_chat_turns'],
                                            'total_active_chat_users': data['total_active_chat_users']})
                    for breakdown in data['breakdown']:
                        usage_brakdown.append({'day': data['day'],
                                            'language': breakdown['language'],
                                            'editor': breakdown['editor'],
                                            'suggestions_count': breakdown['suggestions_count'],
                                            'acceptances_count': breakdown['acceptances_count'],
                                            'lines_suggested': breakdown['lines_suggested'],
                                            'lines_accepted': breakdown['lines_accepted'],
                                            'active_users': breakdown['active_users']})
                                          
                if 'next' in response.links:
                    endpoint_url = response.links['next']['url']
                else:
                    endpoint_url = None
            else:
                logging.error("Error: %s", response.status_code)
                logging.error("Message: %s", response.text)
                endpoint_url = None
        return usage_summary, usage_brakdown

    