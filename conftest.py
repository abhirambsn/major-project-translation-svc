import pytest
import os, signal

@pytest.hookimpl()
def pytest_html_report_title(report):
    print("Setting report title.")
    report.title = "Translation Service API Tests"