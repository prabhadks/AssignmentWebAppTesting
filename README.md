# Web Application Testing Assignment

---

## 🚀 Overview
This framework automates the process of searching for content and playing a streamer’s video within a web application. It emphasizes scalability and maintainability, delivering a robust and comprehensive testing solution that ensures consistent performance across diverse use cases.

---

**Test Run Locally:
![Demonstration of the search and play streamer flow](https://github.com/prabhadks/AssignmentWebAppTesting/blob/master/testresults/WebAppTestingAssignment.gif)

**Project Structure:

The Project is organized as follows:

```
AssignmentWebAppTesting
    application_config.env
    requirements.txt
    components\
        footer_component.py
    pages\
        base_page.py
        directory_page.py
        home_page.py
        video_play_page.py
        __init__.py
    screenshots\
        video_play_screenshot.png
    testresults\
        WebAppTestingAssignment.gif
    tests\
        conftest.py
        __init__.py
        features\
            play.feature
        step_definitions\
            test_search_play_streamer.py
    utils\
        common_element_actions.py
        logger.py
```

## 🏗️ Project Architecture & Design Principles
This framework adheres to robust design patterns to ensure its modularity, readability, and ease of maintenance as the application under test evolves.

### **Modular and Scalable Design**
The core design prioritizes breaking down the testing surface into manageable, reusable components.

### **Page Object Model (POM) & Component-Based Design**
* **Dedicated Page Classes:** For every distinct page in the web application, a separate class file is created. This encapsulates locators and interactions specific to that page.
* **Base Page Class:** All individual page classes inherit from a `BasePage` class. This base class houses common functionalities (e.g., `isPageReady` to verify page loading state) and foundational elements.
* **Common Components:** UI elements that appear across multiple pages (footer) are modeled as separate "component" classes. This allows page classes to use **composition** to include these common elements, promoting reusability and reducing code duplication.

### **Common Actions Wrapper**
A `CommonActions` class acts as a wrapper around basic Selenium interactions with web elements (locators). This abstraction ensures consistency in how actions are performed and provides a single point for enhancements or debugging common interactions.

### **Robust Error Handling & Assertions**
The framework is designed to fail fast and explicitly.

* **No Silent Failures, Assertion-Driven:** Intentionally avoided using `try-catch` blocks around element interactions. If an element can't be found or an action doesn't succeed, an assertion will immediately fail, stopping the test step and ensuring no issues are silently masked.

### **Pytest Fixture Management (`conftest.py`)**
The `conftest.py` file centralizes Pytest fixtures for managing the test environment:
* **Driver Setup & Teardown:** Fixtures handle the instantiation and graceful shutdown of the Selenium WebDriver.
* **Page Object Instantiation:** Fixtures are used to create instances of page classes, making them readily available to tests.
* **Default Scope:** All fixtures are implicitly scoped to `function` (test) by default, ensuring a clean state for each individual test case.

### **Centralized Configuration**
A dedicated configuration file manages key test parameters, including:
* Device settings for mobile emulation.
* The base URL of the application under test.
* Conventions for saving screenshots (e.g., file naming).

### **Comprehensive Logging**
A separate logger module is integrated throughout the framework. This allows for detailed logging of test execution, especially for capturing errors and debugging purposes. Each module imports and utilizes this logger to ensure consistent output.

### **Step Definition Strategy**
Currently, all Gherkin step implementations are consolidated within a single step definition file. While this approach served development expediency, the framework is built with the understanding that these steps can be easily split across multiple files in the future. This is entirely doable using `pytest-bdd`'s tag-based approach, which allows for a highly modular organization of steps per page or feature. Due to time constraints, this advanced splitting wasn't implemented, but it remains a clear path for significantly enhancing maintainability as the application grows.

---

## 🚀 Getting Started
To set up and run this test automation framework on your local machine, follow these steps:

### **Prerequisites**
* **Python:** Ensure Python is installed on your system.
* **Git:** For cloning the repository.
* **Chrome Browser:** The framework is configured for Chrome. No manual WebDriver installation is needed as `webdriver_manager` handles it.

### **Installation**
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/prabhadks/AssignmentWebAppTesting.git]
    cd AssignmentWebAppTesting
    ```
2.  **Create and activate a Python virtual environment:**
    ```bash
    python -m venv .venv
    # On Windows:
    .\.venv\Scripts\activate
    # On macOS/Linux:
    source ./.venv/bin/activate
    ```
3.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run Tests
Ensure your virtual environment is active and you are in the project root directory (`AssignmentWebAppTesting/`).

To execute the full test suite:

```bash
pytest
```

For more verbose output during test execution (including print statements and detailed test names):

```bash
pytest -s -v
```
