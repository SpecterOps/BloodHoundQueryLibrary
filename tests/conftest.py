from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import pytest


class GithubReporter:
    def __init__(self):
        self.results = {
            "summary": {"passed": 0, "failed": 0, "skipped": 0, "total": 0},
            "tests": {
                "failed": [],
                "passed": [],
                "skipped": [],
            },
            "timestamp": datetime.now().isoformat(),
        }

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item: pytest.Item, call: pytest.CallInfo) -> None:
        outcome = yield
        report = outcome.get_result()
        if report.when == "call":
            test_info = {
                "name": item.name,
                "path": item.nodeid,
                "outcome": report.outcome,
                "duration": report.duration,
            }

            if report.outcome == "failed":
                extra_data = getattr(item, "user_data", {})
                test_info['query'] = extra_data.get("query", "Query not found")
                if hasattr(report.longrepr, "reprcrash"):     
                    error_text = report.longrepr.reprcrash.message
                    message = error_text.strip().split("\n")[0]
                    test_info["message"] = message

            self.results["summary"][report.outcome] += 1
            self.results["summary"]["total"] += 1
            self.results["tests"][report.outcome].append(test_info)

    def pytest_sessionfinish(self, session: pytest.Session) -> None:
        env = Environment(
            loader=FileSystemLoader("tests/templates"),
        )
        template = env.get_template("githubsummary.md.j2")
        rendered = template.render(data=self.results)
        with open("test-report.md", "w") as f:
            f.write(rendered)


def pytest_configure(config: pytest.Config) -> None:
    reporter = GithubReporter()
    config.pluginmanager.register(reporter, "github_reporter")
