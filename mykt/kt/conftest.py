import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv
from jira import JIRA
from datetime import datetime

load_dotenv(override=True)

JIRA_API = os.getenv("JIRA_API")
JIRA_SERVER = os.getenv("JIRA_SERVER")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")

def pytest_addoption(parser):
    parser.addoption("--languages",action="store",default="ru",help="Выберите язык")
    parser.addoption("--jira",action="store_true",help="Включить интеграцию с jira")

@pytest.fixture(scope="session")
def jira_client(request):
    if request.config.getoption("jira"):
        jira = JIRA(
            server=JIRA_SERVER,
            basic_auth=(JIRA_USERNAME,JIRA_API))
        return jira

@pytest.fixture
def browser(request):
    language = request.config.getoption("languages")
    options =Options()
    options.add_experimental_option("prefs",{"intl.accept_languages":language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n quit browser")
    browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if (report.when == "call" and report.outcome == "failed") or (report.when == "call" and hasattr(report, "wasxfail") and report.outcome == "passed"):
        if "browser" in item.funcargs:
            browser = item.funcargs["browser"]
            browser.save_screenshot("error_meow.png")

        if "jira_client" in item.funcargs:
            jira = item.funcargs["jira_client"]
            if jira:
                issue_type = jira.issue_types()
                bug_type = issue_type[4]

                issue_dict = {
                    "project": {"key": "SEL"},
                    "summary": "арбузики попадали, разбираться надо",
                    "description": f"реальна конкретная ошибка: {report.longreprtext}\n\nДата:{datetime.now()}",
                    "issuetype": {"id": bug_type.id}
                }
                
                new_issue = jira.create_issue(fields=issue_dict)

                jira.add_attachment(new_issue.key,"error_meow.png")