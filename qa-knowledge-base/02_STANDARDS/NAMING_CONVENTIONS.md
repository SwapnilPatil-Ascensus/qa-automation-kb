# Naming Conventions

## Purpose

This document defines naming conventions for files, classes, methods, variables, and other elements in the QA automation codebase.

## File Naming

### Java Files
- **Classes**: PascalCase matching class name
  - Examples: `LoginPage.java`, `UserRegistrationTest.java`, `ApiClient.java`
- **Interfaces**: PascalCase, often ending with "Interface" or descriptive name
  - Examples: `TestDataProvider.java`, `ConfigReader.java`

### Feature Files (Cucumber)
- **Format**: `lowercase_with_underscores.feature`
- **Examples**: 
  - `login.feature`
  - `user_registration.feature`
  - `api_authentication.feature`

### Configuration Files
- **Properties**: `lowercase_with_underscores.properties`
  - Examples: `test_config.properties`, `environment.properties`
- **XML**: `lowercase_with_underscores.xml`
  - Examples: `testng.xml`, `pom.xml`

### Test Data Files
- **Format**: `descriptive_name.format`
- **Examples**: 
  - `user_credentials.json`
  - `test_data.xlsx`
  - `api_responses.json`

### Documentation Files
- **Format**: `UPPERCASE_WITH_UNDERSCORES.md`
- **Examples**: `CURRENT_STATE.md`, `TEST_PLAN_TEMPLATE.md`

## Java Naming

### Classes
- **Format**: PascalCase
- **Naming Pattern**: Noun or NounPhrase
- **Examples**: 
  - `LoginPage`
  - `UserRegistrationTest`
  - `ApiClient`
  - `TestDataProvider`

### Interfaces
- **Format**: PascalCase
- **Naming Pattern**: Adjective or NounPhrase
- **Examples**: 
  - `Configurable`
  - `TestDataProvider`
  - `ReportGenerator`

### Methods
- **Format**: camelCase
- **Naming Pattern**: Verb or VerbPhrase
- **Examples**: 
  - `clickSubmitButton()`
  - `verifyUserLoggedIn()`
  - `getUserData()`
  - `isElementDisplayed()`
  - `waitForPageLoad()`

### Variables
- **Format**: camelCase
- **Naming Pattern**: Noun or NounPhrase
- **Examples**: 
  - `userName`
  - `passwordField`
  - `testResults`
  - `driver`
  - `wait`

### Constants
- **Format**: UPPER_SNAKE_CASE
- **Naming Pattern**: Descriptive noun phrase
- **Examples**: 
  - `DEFAULT_TIMEOUT`
  - `BASE_URL`
  - `MAX_RETRY_COUNT`
  - `LOGIN_PAGE_TITLE`

### Packages
- **Format**: lowercase
- **Naming Pattern**: Reverse domain notation
- **Examples**: 
  - `com.company.qa.pages`
  - `com.company.qa.stepdefs`
  - `com.company.qa.utils`

## Selenium/WebDriver Naming

### WebElement Variables
- **Format**: camelCase with descriptive suffix
- **Suffixes**: `Button`, `Field`, `Link`, `Dropdown`, `Checkbox`, `Radio`, `Table`, etc.
- **Examples**: 
  - `loginButton`
  - `userNameField`
  - `submitLink`
  - `countryDropdown`
  - `termsCheckbox`

### Locator Variables
- **Format**: camelCase with "Locator" suffix or descriptive name
- **Examples**: 
  - `loginButtonLocator`
  - `userNameFieldLocator`
  - Or: `loginButtonBy` (if using By objects)

### Page Object Methods
- **Actions**: Verb + Object
  - Examples: `clickLoginButton()`, `enterUserName()`, `selectCountry()`
- **Getters**: get + Object
  - Examples: `getPageTitle()`, `getErrorMessage()`
- **Verifiers**: is/has + Object + State
  - Examples: `isLoginButtonDisplayed()`, `hasErrorMessage()`
- **Waiters**: waitFor + Object + State
  - Examples: `waitForPageLoad()`, `waitForElementVisible()`

## Cucumber/Gherkin Naming

### Feature Names
- **Format**: Title Case
- **Examples**: 
  - "User Login"
  - "Product Search"
  - "API Authentication"

### Scenario Names
- **Format**: Title Case, descriptive
- **Examples**: 
  - "Valid user login"
  - "Login with invalid credentials"
  - "Search product by name"

### Step Definitions
- **Format**: camelCase matching Gherkin text
- **Examples**: 
  - `@Given("user navigates to login page")` → `userNavigatesToLoginPage()`
  - `@When("user enters credentials")` → `userEntersCredentials()`
  - `@Then("user should be logged in")` → `userShouldBeLoggedIn()`

## TestNG Naming

### Test Methods
- **Format**: camelCase with "test" prefix (optional, depends on team preference)
- **Examples**: 
  - `testValidLogin()`
  - `testLoginWithInvalidCredentials()`
  - Or: `validLogin()`, `loginWithInvalidCredentials()`

### Test Groups
- **Format**: lowercase_with_underscores
- **Examples**: 
  - `smoke`
  - `regression`
  - `api_tests`
  - `ui_tests`

### Data Provider Names
- **Format**: camelCase
- **Examples**: 
  - `loginData`
  - `userCredentials`
  - `testScenarios`

## API Testing Naming

### Endpoint Variables
- **Format**: camelCase with "Endpoint" or "Url" suffix
- **Examples**: 
  - `loginEndpoint`
  - `userApiUrl`
  - `baseApiUrl`

### Request/Response Variables
- **Format**: camelCase with descriptive suffix
- **Examples**: 
  - `loginRequest`
  - `userResponse`
  - `errorResponse`

## Configuration Naming

### Property Keys
- **Format**: lowercase_with_underscores
- **Examples**: 
  - `base.url`
  - `default.timeout`
  - `browser.type`
  - `test.environment`

### Environment Variables
- **Format**: UPPER_SNAKE_CASE
- **Examples**: 
  - `TEST_ENVIRONMENT`
  - `BASE_URL`
  - `API_KEY`

## Database Naming (if applicable)

### Table Names
- **Format**: lowercase_with_underscores
- **Examples**: `test_users`, `test_data`

### Column Names
- **Format**: lowercase_with_underscores
- **Examples**: `user_name`, `created_date`

## Reporting Naming

### Report Files
- **Format**: `descriptive_name_timestamp.format`
- **Examples**: 
  - `test_execution_20260125_143022.html`
  - `regression_report_20260125.pdf`

### Screenshot Names
- **Format**: `testname_timestamp.format`
- **Examples**: 
  - `login_test_20260125_143022.png`
  - `registration_failure_20260125_143022.png`

## Best Practices

1. **Be Descriptive**: Names should clearly indicate purpose
2. **Be Consistent**: Follow established patterns
3. **Avoid Abbreviations**: Use full words unless abbreviation is standard
4. **Use Standard Suffixes**: Follow language/framework conventions
5. **Avoid Magic Numbers/Strings**: Use named constants
6. **Keep Names Reasonable Length**: Balance descriptiveness with readability

## Examples

### Good Naming
```java
public class LoginPage {
    private static final int DEFAULT_TIMEOUT = 30;
    private WebElement userNameField;
    private WebElement passwordField;
    private WebElement loginButton;
    
    public void enterCredentials(String username, String password) {
        userNameField.sendKeys(username);
        passwordField.sendKeys(password);
    }
    
    public void clickLoginButton() {
        loginButton.click();
    }
    
    public boolean isLoginButtonDisplayed() {
        return loginButton.isDisplayed();
    }
}
```

### Poor Naming
```java
public class LP {
    private WebElement e1;
    private WebElement e2;
    private WebElement btn;
    
    public void doStuff(String u, String p) {
        e1.sendKeys(u);
        e2.sendKeys(p);
    }
}
```

## Notes

[Any additional naming conventions or team-specific guidelines]
