
QA Quality Gatekeeper

This repository contains automated test suites and infrastructure for ensuring software quality through functional UI tests, API testing, performance testing with k6, and security scanning with OWASP ZAP.
Project Structure

    docker-compose.yml — Docker setup for Selenium Grid and related services.

    requirements.txt — Python dependencies.

    reports/security/ — Security scan reports (e.g., OWASP ZAP).

    tests/ — Organized test suites:

        functional/selenium_tests/ — UI tests with Selenium WebDriver.

        functional/test_api.py — API backend tests.

        performance/ — k6 scripts for load and performance testing.

        security/ — Security scanning automation scripts.

Functional Selenium Tests

Tests cover a broad range of UI scenarios, including:

    Alerts (JavaScript alerts handling)

    Authentication (Basic, Digest, Form, Forgot Password)

    Dynamic Content & Controls

    Editors (WYSIWYG)

    Elements (Checkboxes, dropdowns, inputs, add/remove elements)

    File management (downloads)

    Frames (including nested)

    Geolocation

    Interactions (drag-and-drop, context menus, sliders, multiple windows)

    Keyboard events

    Menus (jQuery UI)

    Notifications (entry/exit ads, message popups)

    Scrolling (infinite scroll)

    Shadow DOM components

    Tables (sortable data)

    Miscellaneous edge cases (broken images, status codes, slow resources)

Performance Tests

Performance and load testing is done using k6, an open-source load testing tool.

The performance/ folder contains JavaScript scripts that simulate:

    Multiple endpoints load testing

    POST request stress scenarios

    User ramping and concurrency tests

    Overall performance benchmarks

Security Scanning

Security scans leverage OWASP ZAP with:

    Python script: run_zap_scan.py

    Baseline shell script: zap_baseline_scan.sh

    Reports generated under reports/security/

Getting Started
Prerequisites

    Install Docker and Docker Compose

    Python 3.8+ and install dependencies:

    pip install -r requirements.txt

    Install k6 for performance tests.

Running Selenium Grid Locally

Start Selenium Grid and Chrome node via Docker Compose or manually:

docker-compose up -d

Or start containers individually as configured.
Running Tests

Run Selenium functional tests with:

pytest tests/functional/selenium_tests/

Run API tests similarly:

pytest tests/functional/test_api.py

Run performance tests with k6, e.g.:

k6 run performance/performance_test.js

Run security scans with:

python tests/security/run_zap_scan.py

CI/CD Integration

    GitHub Actions pipeline (.github/workflows/) automates starting Selenium Grid, waiting for readiness, and running tests.

    Logs and reports are automatically collected and saved.

Logs and Reports

    Test execution logs stored in logs/

    Security reports in reports/security/

    Performance test results can be saved under a new reports/performance/ folder
