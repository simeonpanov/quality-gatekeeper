🛡️ Quality Gatekeeper --- A Full-Stack QA Automation Framework
=============================================================

This project began as my personal toolkit to tackle complex testing challenges across UI, API, performance, and security layers. Over time, it evolved into a modular, scalable automation framework designed to fit into modern CI/CD pipelines and leverage containerized infrastructure for consistency.

* * * * *

What It Does
------------

Quality Gatekeeper helps you cover all your bases:

-   **Functional UI Testing:** Browser automation with Selenium, handling tricky real-world stuff like alerts, frames, shadow DOM, infinite scroll, and more.

-   **API Testing:** Validates REST endpoints using Pytest and Requests.

-   **Performance Testing:** Uses k6 for load and stress testing.

-   **Security Scanning:** Automated vulnerability checks via OWASP ZAP.

-   **CI/CD Integration:** Seamlessly plugs into GitHub Actions for automated pipelines.

-   **Dockerized Setup:** Runs everything through Docker Compose and Selenium Grid so you get the same environment locally and in CI.

* * * * *

Quick Start / Setup Notes
-------------------------

Before diving in, here's what you'll need:

-   Docker and Docker Compose installed locally

-   Chrome and Firefox browsers available for Selenium Grid nodes

-   A GitHub repository configured to run GitHub Actions (if you want CI)

-   Basic Python environment with Pytest and dependencies installed (`requirements.txt` included)

**TODO:** Add a setup script or Makefile to simplify installation.

* * * * *

Key Features & Highlights
-------------------------

### Functional Testing (Selenium)

-   Built with Pytest for clean test structure and parallel runs.

-   Runs cross-browser tests on Selenium Grid (Chrome & Firefox).

-   Handles advanced scenarios like geolocation mocking, iframe interactions, shadow DOM, alerts, and infinite scroll.

-   Modular configs and detailed logging help troubleshoot flaky tests quickly.

### API Testing

-   Validates REST APIs using Requests and Pytest.

-   Easy to extend with new endpoints or test cases.

### Performance Testing

-   Load testing with k6, designed to simulate realistic traffic and stress scenarios.

### Security Scanning

-   OWASP ZAP runs automated vulnerability scans during your test pipeline.

-   Reports help catch security issues early.

### CI/CD Integration

-   GitHub Actions workflows run your UI, API, performance, and security tests automatically.

-   Test results are saved as artifacts for later review.

### Dockerized Test Stack

-   All services run inside Docker containers:

    -   Selenium Grid Hub + browser nodes

    -   OWASP ZAP scanner

-   Managed by a single `docker-compose.yml` file, so setup is consistent everywhere.

* * * * *

Architecture Notes
------------------

-   Clean separation of concerns (config, drivers, utilities, tests).

-   Allure reporting for rich visual test reports.

-   Flexible environment setup --- switch between local and remote Grid easily via environment variables.

* * * * *
