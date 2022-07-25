#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

import click
import yaml
import requests
import json


from app.logz import create_logger


logger = create_logger()
# Create group to handle bulk processing and data migrations
@click.group()
def migrations():
    """Performs data processing for legacy data to migrate data formats or perform bulk processing"""
    pass


# Add links in the lineage tree to issues
@migrations.command()
def issuelinker():
    """Provides linkage to the lineage of the issue (deep links to parent records in the tree)"""
    # load the config from YAML
    with open("init.yaml", "r") as stream:
        config = yaml.safe_load(stream)

    # make sure config is set before processing
    if config["domain"] == None:
        return "ERROR: No domain set in the initilization file."
    elif config["domain"] == "":
        return "ERROR: The domain is blank in the initialization file."
    elif config["token"] == None:
        return "ERROR: The token has not been set in the initialization file."
    elif config["token"] == "":
        return "ERROR: The token has not been set in the initialization file."
    else:
        # set health check URL
        url_issues = config["domain"] + "/api/issues/getAll"

        # set headers
        headersGet = {"Accept": "application/json", "Authorization": config["token"]}

        # get the full list of issues
        logger.info("Fetching full issue list from RegScale")
        try:
            issueResponse = requests.request("GET", url_issues, headers=headersGet)
            issuesData = issueResponse.json()
        except:
            logger.error("ERROR: Unable to retrieve issue list from RegScale.")
            quit()

        # write out issues data to file
        with open("artifacts/regscaleIssueList.json", "w") as outfile:
            outfile.write(json.dumps(issuesData, indent=4))
        logger.info(
            "Writing out RegScale issue list to the artifacts folder (see regscaleIssueList.json)"
        )
        logger.info(
            str(len(issuesData)) + " issues retrieved for processing from RegScale."
        )

        # loop through each issue
        for iss in issuesData:
            url_processor = (
                config["domain"] + "/api/issues/processLineage/" + str(iss["id"])
            )
            try:
                processResult = requests.request(
                    "GET", url_processor, headers=headersGet
                )
                logger.info(
                    "Processing Issue #: "
                    + str(iss["id"])
                    + ", Result: "
                    + str(processResult)
                )
            except Exception:
                logger.error("ERROR: Unable to process Issue # " + str(iss["id"]))


# Add links in the lineage tree to assessments
@migrations.command()
def assessmentlinker():
    """Provides linkage to the lineage of the assessment (deep links to parent records in the tree)"""
    # load the config from YAML
    with open("init.yaml", "r") as stream:
        config = yaml.safe_load(stream)

    # make sure config is set before processing
    if config["domain"] == None:
        return "ERROR: No domain set in the initilization file."
    elif config["domain"] == "":
        return "ERROR: The domain is blank in the initialization file."
    elif config["token"] == None:
        return "ERROR: The token has not been set in the initialization file."
    elif config["token"] == "":
        return "ERROR: The token has not been set in the initialization file."
    else:
        # set health check URL
        url_assessments = config["domain"] + "/api/assessments/getAll"

        # set headers
        headersGet = {"Accept": "application/json", "Authorization": config["token"]}

        # get the full list of assessments
        logger.info("Fetching full assessment list from RegScale")
        try:
            astResponse = requests.request("GET", url_assessments, headers=headersGet)
            astData = astResponse.json()
        except:
            logger.error("ERROR: Unable to retrieve assessment list from RegScale.")
            quit()

        # write out assessment data to file
        with open("artifacts/regscaleAssessmentList.json", "w") as outfile:
            outfile.write(json.dumps(astData, indent=4))
        logger.info(
            "Writing out RegScale assessment list to the artifacts folder (see regscaleAssessmentList.json)"
        )
        logger.info(
            str(len(astData)) + " assessments retrieved for processing from RegScale."
        )

        # loop through each assessment
        for ast in astData:
            url_processor = (
                config["domain"] + "/api/assessments/processLineage/" + str(ast["id"])
            )
            try:
                processResult = requests.request(
                    "GET", url_processor, headers=headersGet
                )
                logger.info(
                    "Processing Assessment #: "
                    + str(ast["id"])
                    + ", Result: "
                    + str(processResult)
                )
            except:
                logger.error("ERROR: Unable to process Assessment # " + str(ast["id"]))


# Add links in the lineage tree to risks
@migrations.command()
def risklinker():
    """Provides linkage to the lineage of the risk (deep links to parent records in the tree)"""
    # load the config from YAML
    with open("init.yaml", "r") as stream:
        config = yaml.safe_load(stream)

    # make sure config is set before processing
    if config["domain"] == None:
        return "ERROR: No domain set in the initilization file."
    elif config["domain"] == "":
        return "ERROR: The domain is blank in the initialization file."
    elif config["token"] == None:
        return "ERROR: The token has not been set in the initialization file."
    elif config["token"] == "":
        return "ERROR: The token has not been set in the initialization file."
    else:
        # set health check URL
        url_risks = config["domain"] + "/api/risks/getAll"

        # set headers
        headersGet = {"Accept": "application/json", "Authorization": config["token"]}

        # get the full list of risks
        logger.info("Fetching full risk list from RegScale")
        try:
            riskResponse = requests.request("GET", url_risks, headers=headersGet)
            riskData = riskResponse.json()
        except:
            logger.error("ERROR: Unable to retrieve risk list from RegScale.")
            quit()

        # write out risks data to file
        with open("artifacts/regscaleriskList.json", "w") as outfile:
            outfile.write(json.dumps(riskData, indent=4))
        logger.info(
            "Writing out RegScale risk list to the artifacts folder (see regscaleRiskList.json)"
        )
        logger.info(
            str(len(riskData)) + " risks retrieved for processing from RegScale."
        )

        # loop through each risk
        for r in riskData:
            url_processor = (
                config["domain"] + "/api/risks/processLineage/" + str(r["id"])
            )
            try:
                processResult = requests.request(
                    "GET", url_processor, headers=headersGet
                )
                logger.info(
                    "Processing Risk #: "
                    + str(r["id"])
                    + ", Result: "
                    + str(processResult)
                )
            except:
                logger.error("ERROR: Unable to process Risk # " + str(r["id"]))
