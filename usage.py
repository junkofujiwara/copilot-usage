#!/usr/bin/env python3
# -*- coding: utf_8 -*-
'''usage.py'''
import csv
import logging
import settings
from util import github as github_util
from util import util

def main():
    '''main function'''
    # set up logging
    logging.basicConfig(
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(message)s",
        handlers = [
            logging.FileHandler(settings.LOG_FILE),
            logging.StreamHandler()
        ])

    # initialize
    github_org, github_slug, github_token = util.init()
    github = github_util.Github(settings.API_ENDPOINT, github_slug, github_org, github_token)
    isEnteprise = github_slug is not None
    # get usage information
    summary, breakdown = github.get_usage(isEnteprise)
    if summary is None or len(summary) == 0:
        logging.error("No usage information found")
        return
    if isEnteprise:
        summary_file = settings.ENTERPRISE_USAGE_FILE_SUMMERY.format(slug=github_slug)
        breakdown_file = settings.ENTERPRISE_USAGE_FILE_BREAKDOWN.format(slug=github_slug)
    else:
        summary_file = settings.ORGANIZATION_USAGE_FILE_SUMMERY.format(org=github_org)
        breakdown_file = settings.ORGANIZATION_USAGE_FILE_BREAKDOWN.format(org=github_org)
    util.write_to_csv(summary, summary_file, isSummary=True)
    util.write_to_csv(breakdown, breakdown_file, isSummary=False)

if __name__ == "__main__":
    main()
