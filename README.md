🛡️ Quality Gatekeeper -- A Full-Stack QA Automation Framework
-------------------------------------------------------------

A robust and modular testing framework designed to ensure software quality across **UI, API, performance, and security layers**. This project highlights my capabilities as a QA Engineer in building scalable test systems, integrating automation into CI/CD pipelines, and leveraging Docker-based infrastructure.

* * * * *

🎯 Key Features
---------------

-   **Functional UI Testing**: Selenium-based browser automation covering real-world use cases like alerts, frames, user interactions, form inputs, shadow DOM, etc.

-   **API Testing**: Validating REST API endpoints using Pytest and Requests.

-   **Performance Testing**: Leveraging [k6](https://k6.io/) for load testing and stress simulations.

-   **Security Scanning**: Automated vulnerability scans using [OWASP ZAP](https://www.zaproxy.org/).

-   **CI/CD Integration**: Fully integrated with GitHub Actions to enable automated test pipelines.

-   **Dockerized Infrastructure**: Uses Docker Compose and Selenium Grid to run distributed browser tests locally and in CI.

* * * * *

🧪 Functional Testing (Selenium)
--------------------------------

-   Designed using **Pytest** for test structuring and parallel execution.

-   Cross-browser execution via **Selenium Grid**.

-   Includes advanced scenarios like geolocation mocking, iframe handling, shadow DOM interaction, and infinite scroll.

-   Modular configuration and logging to simplify test execution and debugging.

* * * * *

⚙️ Test Architecture Highlights
-------------------------------

-   **Project Structure** promotes separation of concerns (e.g., config, drivers, utilities, test layers).

-   **Logging & Reporting** integrated with **Allure** for visual test insights.

-   **Environment flexibility** with a toggle for local or remote (Grid) execution via environment variables.

* * * * *

🚀 DevOps & CI/CD
-----------------

-   CI pipeline runs on **GitHub Actions**, executing:

    -   Functional tests via Selenium Grid

    -   API tests with coverage reporting

    -   Performance tests with k6

    -   Security scans via ZAP

-   All test results are archived as artifacts for visibility and traceability.

* * * * *

🐳 Dockerized Test Stack
------------------------

-   All test infrastructure is containerized:

    -   Selenium Grid (Hub + Chrome/Firefox nodes)

    -   OWASP ZAP

-   Managed via a **single `docker-compose.yml`**, allowing consistent local/CI environments.

* * * * *

📈 Reports & Artifacts (GitHub Actions)
---------------------------------------

| Report Type | Artifact Name |
| --- | --- |
| Coverage Report | `coverage-report` |
| UI Test Report | `allure-report` |
| k6 Load Results | `k6-performance-report` |
| ZAP Scan Report | `zap-security-json-report` |
