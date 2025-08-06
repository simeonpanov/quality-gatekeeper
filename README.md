# Quality Gatekeeper

This repository contains automated test suites and infrastructure for ensuring software quality through functional UI tests, API testing, performance testing with [k6](https://k6.io/), and security scanning with [OWASP ZAP](https://www.zaproxy.org/).

---

## 🧪 Functional Selenium Tests

UI automation is powered by **Selenium WebDriver** and covers a wide range of real-world scenarios:

- **Alerts**: Handling JavaScript alerts
- **Authentication**: Basic, Digest, Form-based, Forgot Password flows
- **Dynamic Content & Controls**: AJAX, dynamic loading, etc.
- **Editors**: WYSIWYG editor interactions
- **Elements**: Checkboxes, dropdowns, inputs, add/remove elements
- **File Management**: File downloads
- **Frames**: Nested iframe handling
- **Geolocation**: Mocking geolocation data
- **Interactions**: Drag-and-drop, context menus, sliders, multiple windows
- **Keyboard Events**: Key presses and input simulation
- **Menus**: jQuery UI menu interactions
- **Notifications**: Entry/exit ads, message popups
- **Scrolling**: Infinite scroll testing
- **Shadow DOM**: Component interaction within shadow roots
- **Tables**: Sortable and dynamic tables
- **Edge Cases**: Broken images, HTTP status codes, slow-loading resources

---

## ⚡ Performance Testing (k6)

Performance and load testing is conducted using **[k6](https://k6.io/)**, an open-source tool for modern performance testing.

The \`performance/\` directory includes scripts that simulate:
- Load across multiple endpoints
- Stress testing via POST requests
- User ramp-up and concurrency patterns
- Performance benchmarking

📄 Example: `tests/performance/performance_test.js`

---

## 🔒 Security Scanning

Security testing leverages **OWASP ZAP (Zed Attack Proxy)** to identify vulnerabilities.

---

## 🚀 Getting Started

### Prerequisites

Ensure the following are installed:
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/)
- Python 3.8+
- [k6](https://k6.io/docs/getting-started/installation/)

### Install Python dependencies
```bash
pip install -r requirements.txt


---

### Running Selenium Grid Locally

Start the Selenium Grid and Chrome node using Docker Compose:
\`\`\`bash
docker-compose up -d
\`\`\`

> This sets up a Selenium Hub with a Chrome browser node ready for testing.

To stop:
\`\`\`bash
docker-compose down
\`\`\`

---

### Running Tests

#### Functional UI Tests (Selenium)
\`\`\`bash
pytest tests/functional/selenium_tests/
\`\`\`

#### API Tests
\`\`\`bash
pytest tests/functional/test_api.py
\`\`\`

#### Performance Tests (k6)
\`\`\`bash
k6 run performance/performance_test.js
\`\`\`

#### Security Scans (OWASP ZAP)
\`\`\`bash
python tests/security/run_zap_scan.py
\`\`\`

---

## 🔄 CI/CD Integration

Automated via **GitHub Actions**:
- Pipeline: \`.github/workflows/ci.yml\`
- Actions include:
  - Starting Selenium Grid
  - Waiting for service readiness
  - Running functional, performance, and security tests
  - Collecting logs and reports

All outputs are archived for analysis.

---

## 📊 Logs and Reports

Test artifacts are uploaded during the CI pipeline and can be accessed from each workflow run in GitHub Actions:

| Type                | GitHub Actions Artifact Name |
|---------------------|------------------------------|
| Test Coverage       | `coverage-report`            |
| Selenium Test       | `allure-report`              |
| Security Scan (ZAP) | `zap-security-json-report`   |
| Performance Tes(k6) | `k6-performance-report`      |

---

## 📚 Learn More

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [k6 Documentation](https://k6.io/docs/)
- [OWASP ZAP User Guide](https://www.zaproxy.org/docs/)

---
