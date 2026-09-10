# Playbot demo reports

Public GitHub Pages reports from `Test-Automation-PTS/playbot-demo-customer`.

- [Allure: all module tests, history and trends](https://test-automation-pts.github.io/playbot-demo-reports/allure/)
- [PDF dashboard: document evidence and test steps](https://test-automation-pts.github.io/playbot-demo-reports/pdf/)
- [Report files](https://github.com/Test-Automation-PTS/playbot-demo-reports/tree/gh-pages)

The customer workflow runs the approved Playbot image and publishes its completed
report bundle to the existing public `playbot-reports` handoff. This repository
imports that public bundle, stores the report files on `gh-pages`, and deploys
its own GitHub Pages site. It needs no token granting access to the private
customer source repository. Only the generated demo results are published.

The importer checks every five minutes and can also be started with **Actions →
Publish PDF dashboard and Allure → Run workflow**. GitHub scheduling may delay a
scheduled run. The landing page and dashboard identify the published test run and
commit. Identical publications are skipped.

Both latest views and up to 20 archived complete runs are retained. Allure's
`history/` is restored by the customer workflow before the next report is
created. The PDF dashboard has its own history generated from those same Robot
runs. Trend points represent real runs; no synthetic history is inserted.
