import os
from dotenv import load_dotenv
from jira import JIRA

load_dotenv(override=True)

JIRA_API = os.getenv("JIRA_API")
JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")

# JIRA_SERVER = os.environ.get("JIRA_SERVER") - другой вариант достать что-т из .env
# os.environ["key"] = "valeue" - Задать новое значение в envs 
jira = JIRA(
    server=JIRA_SERVER,
    basic_auth=(JIRA_USERNAME,JIRA_API))

# print(jira.myself())
# print(jira.projects())
# print(jira.issue_types())

jira_issue = jira.create_issue(
    {
    "project": {"key": "SEL"},
    "summary":"МЯУ МЯУ МЯУУ",
    "description": "очень крутая задача для очень крутых котят",
    "issuetype": {"id":"10000"}
    })

jira.add_attachment(jira_issue.key,"mars.jpg")