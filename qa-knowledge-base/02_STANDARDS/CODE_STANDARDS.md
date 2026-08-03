# Code Standards

## Purpose

This document defines coding standards and best practices for QA automation code.

## General Principles

1. **Readability**: Code should be easy to read and understand
2. **Maintainability**: Code should be easy to modify and extend
3. **Consistency**: Follow established patterns
4. **Testability**: Code should be testable
5. **Documentation**: Code should be well-documented

## Java Coding Standards

### Naming Conventions

#### Classes
- Use PascalCase
- Be descriptive
- Examples: `LoginPage`, `UserRegistrationTest`, `ApiClient`

#### Methods
- Use camelCase
- Use verb-noun pattern for actions
- Examples: `clickSubmitButton()`, `verifyUserLoggedIn()`, `getUserData()`

#### Variables
- Use camelCase
- Be descriptive
- Examples: `userName`, `passwordField`, `testResults`

#### Constants
- Use UPPER_SNAKE_CASE
- Examples: `DEFAULT_TIMEOUT`, `BASE_URL`, `MAX_RETRY_COUNT`

#### Packages
- Use lowercase
- Use reverse domain notation
- Examples: `com.company.qa.pages`, `com.company.qa.utils`

### Code Organization

#### Package Structure
```
src/
  main/java/
    com/company/qa/
      pages/          # Page Object classes
      stepdefs/       # Cucumber step definitions
      utils/          # Utility classes
      config/         # Configuration classes
      data/           # Test data classes
  test/java/
    com/company/qa/
      tests/          # Test classes
      runners/        # Test runners
```

#### Class Structure
```java
// Package declaration
package com.company.qa.pages;

// Imports (grouped: java, third-party, project)
import java.util.List;
import org.openqa.selenium.WebDriver;
import com.company.qa.utils.WaitUtil;

// Class declaration
public class LoginPage {
    // Constants
    private static final String LOGIN_URL = "/login";
    
    // Fields
    private WebDriver driver;
    
    // Constructor
    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }
    
    // Public methods
    public void login(String username, String password) {
        // Implementation
    }
    
    // Private helper methods
    private void waitForPageLoad() {
        // Implementation
    }
}
```

### Code Formatting

#### Indentation
- Use 4 spaces (no tabs)
- Consistent indentation throughout

#### Line Length
- Maximum 120 characters per line
- Break long lines appropriately

#### Braces
- Use opening brace on same line
- Closing brace on new line
```java
if (condition) {
    // code
} else {
    // code
}
```

#### Spacing
- One blank line between methods
- Blank lines to separate logical sections
- No trailing whitespace

### Comments

#### JavaDoc Comments
```java
/**
 * Logs in a user with the provided credentials.
 * 
 * @param username The username to login with
 * @param password The password for the user
 * @throws TimeoutException if login page doesn't load
 */
public void login(String username, String password) {
    // Implementation
}
```

#### Inline Comments
- Use sparingly
- Explain "why" not "what"
- Keep comments up-to-date with code

### Best Practices

#### Page Object Model (POM)
- One class per page/screen
- Locators as private fields
- Public methods for user actions
- Return Page Objects for method chaining

#### Wait Strategies
- Use explicit waits (WebDriverWait)
- Avoid Thread.sleep()
- Set appropriate timeouts
- Use custom wait utilities

#### Exception Handling
- Handle expected exceptions
- Log exceptions appropriately
- Don't swallow exceptions silently
- Provide meaningful error messages

#### Test Data
- Externalize test data
- Use data providers for parameterized tests
- Avoid hardcoded values
- Use configuration files

#### Assertions
- Use TestNG assertions
- Provide meaningful assertion messages
- One logical assertion per test method
- Use soft assertions when appropriate

## Cucumber/Gherkin Standards

### Feature Files

#### Structure
```gherkin
Feature: Feature Name
  As a [role]
  I want to [action]
  So that [benefit]

  Background:
    Given [common setup]

  Scenario: Scenario Name
    Given [precondition]
    When [action]
    Then [verification]
```

#### Naming
- Feature files: `feature_name.feature`
- Use descriptive scenario names
- Use Given/When/Then structure

#### Best Practices
- Keep scenarios focused (one behavior)
- Use Background for common setup
- Use Scenario Outline for data-driven tests
- Avoid implementation details in steps

### Step Definitions

#### Naming
- Match Gherkin steps exactly
- Use descriptive method names
- Examples: `userNavigatesToLoginPage()`, `userEntersCredentials()`

#### Organization
- Group related steps in same class
- Reuse steps where possible
- Keep steps at appropriate abstraction level

## TestNG Standards

### Test Classes

#### Structure
```java
@Listeners(TestListener.class)
public class LoginTest {
    
    @BeforeClass
    public void setUpClass() {
        // Class-level setup
    }
    
    @BeforeMethod
    public void setUpMethod() {
        // Method-level setup
    }
    
    @Test(groups = {"smoke", "regression"})
    public void testValidLogin() {
        // Test implementation
    }
    
    @AfterMethod
    public void tearDownMethod() {
        // Method-level cleanup
    }
    
    @AfterClass
    public void tearDownClass() {
        // Class-level cleanup
    }
}
```

### Test Groups
- Use meaningful group names
- Examples: `smoke`, `regression`, `api`, `ui`
- Document group purposes

### Data Providers
```java
@DataProvider(name = "loginData")
public Object[][] getLoginData() {
    return new Object[][] {
        {"user1", "pass1"},
        {"user2", "pass2"}
    };
}

@Test(dataProvider = "loginData")
public void testLogin(String username, String password) {
    // Test implementation
}
```

## Code Review Checklist

- [ ] Follows naming conventions
- [ ] Proper code organization
- [ ] Appropriate comments and JavaDoc
- [ ] No hardcoded values
- [ ] Proper exception handling
- [ ] Follows POM pattern (for UI tests)
- [ ] Appropriate waits (no Thread.sleep)
- [ ] Meaningful assertions
- [ ] Test data externalized
- [ ] No code duplication
- [ ] Follows formatting standards

## Tools

### Code Formatting
- **Tool**: [Eclipse/IntelliJ formatter, Checkstyle, etc.]
- **Configuration**: [Location of config file]

### Static Analysis
- **Tool**: [SonarQube, FindBugs, etc.]
- **Rules**: [Key rules to follow]

### Linting
- **Tool**: [PMD, Checkstyle, etc.]
- **Configuration**: [Location of config file]

## Notes

[Any additional code standards or guidelines]
