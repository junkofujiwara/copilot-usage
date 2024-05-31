#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""common.py"""
import csv
import getopt
import logging
import sys

def init():
    """init"""
    try:
        github_org = None
        github_token = None
        github_slug = None
        script = sys.argv[0]
        usage_text = (f"Usage: {script} "
                "-s <enterprise_slug> -o <organization_name> -t <github_personal_token>")
        opts, _args = getopt.getopt(
            sys.argv[1:], "o:s:t:h", ["org=", "slug=", "token=", "help"]
        )
        for opt, arg in opts:
            if opt in ("-o", "--org"):
                github_org = arg
            if opt in ("-s", "--slug"):
                github_slug = arg
            if opt in ("-t", "--token"):
                github_token = arg
            elif opt in ("-h", "--help"):
                logging.info(usage_text)
                sys.exit()
        if github_token is None:
            logging.info(usage_text)
            sys.exit()
        return github_org, github_slug, github_token
    except (getopt.GetoptError, IndexError) as exception:
        logging.error(exception)
        logging.info(usage_text)
        sys.exit(1)

def write_to_csv(pullrequests, filename, isSummary=False):
    """write information to csv"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        if isSummary:
            fieldnames = ['day',
                          'total_suggestions_count',
                          'total_acceptances_count',
                          'total_lines_suggested',
                          'total_lines_accepted',
                          'total_active_users',
                          'total_chat_acceptances',
                          'total_chat_turns',
                          'total_active_chat_users']
        else:
            fieldnames = ['day',
                          'language',
                          'editor',
                          'suggestions_count',
                          'acceptances_count',
                          'lines_suggested',
                          'lines_accepted',
                          'active_users']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for pullrequest in pullrequests:
            writer.writerow(pullrequest)