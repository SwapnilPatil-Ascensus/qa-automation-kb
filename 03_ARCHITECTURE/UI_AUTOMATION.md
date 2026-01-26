# UI Automation Architecture

## Purpose

This document describes the architecture and design of UI automation framework using Selenium WebDriver and Page Object Model.

## Architecture Overview

```
Test Layer (Cucumber/TestNG)
    ↓
Step Definitions
    ↓
Page Objects (POM)
    ↓
Selenium WebDriver
    ↓
Browser
```

## Page Object Model (POM)

### Design Pattern

The Page Object Model pattern encapsulates page elements and actions into reusable classes.

### Structure

```java
public class LoginPage {
    // Locators (private)
    private By userNameField = By.id("username");
    private By passwordField = By.id("password");
    private By loginButton = By.id("login-btn");
    
    // WebDriver instance
    private WebDriver driver;
    private WebDriverWait wait;
    
    // Constructor
    public LoginPage(WebDriver driver) {
        this.driver = driver;
        this.wait = new WebDriverWait(driver, Duration.ofSeconds(30));
    }
    
    // Action methods
    public void enterUserName(String username) {
        wait.until(ExpectedConditions.presenceOfElementLocated(userNameField));
        driver.findElement(userNameField).sendKeys(username);
    }
    
    public void enterPassword(String password) {
        driver.findElement(passwordField).sendKeys(password);
    }
    
    public void clickLoginButton() {
        driver.findElement(loginButton).click();
    }
    
    // Verification methods
    public boolean isLoginButtonDisplayed() {
        return driver.findElement(loginButton).isDisplayed();
    }
    
    // Navigation methods (return Page Objects)
    public HomePage login(String username, String password) {
        enterUserName(username);
        enterPassword(password);
        clickLoginButton();
        return new HomePage(driver);
    }
}
```

### Page Object Guidelines

1. **One Class Per Page**: Each page/screen has its own Page Object class
2. **Locators as Fields**: Store locators as private fields
3. **Public Methods**: Expose user actions as public methods
4. **Return Page Objects**: Methods that navigate return the next page object
5. **No Assertions in POM**: Assertions belong in test classes
6. **Wait Strategies**: Use explicit waits within page objects

## Locator Strategy

### Locator Priority

1. **ID**: Most stable, use when available
2. **Name**: Good for form elements
3. **CSS Selector**: Flexible, good performance
4. **XPath**: Use when other locators don't work, prefer relative XPath
5. **Link Text/Partial Link Text**: For links
6. **Class Name**: Use with caution (often changes)

### Locator Management

#### Centralized Locators
```java
public class LoginPageLocators {
    public static final By USER_NAME_FIELD = By.id("username");
    public static final By PASSWORD_FIELD = By.id("password");
    public static final By LOGIN_BUTTON = By.id("login-btn");
}
```

#### Properties File
```properties
login.page.username.field=id:username
login.page.password.field=id:password
login.page.login.button=id:login-btn
```

## Wait Strategies

### Explicit Waits (Preferred)

```java
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(30));
wait.until(ExpectedConditions.elementToBeClickable(loginButton));
```

### Custom Wait Utilities

```java
public class WaitUtil {
    public static void waitForElementVisible(WebDriver driver, By locator, int timeout) {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(timeout));
        wait.until(ExpectedConditions.visibilityOfElementLocated(locator));
    }
    
    public static void waitForPageLoad(WebDriver driver) {
        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(30));
        wait.until(driver -> ((JavascriptExecutor) driver)
            .executeScript("return document.readyState").equals("complete"));
    }
}
```

### Wait Conditions

- `presenceOfElementLocated`: Element exists in DOM
- `visibilityOfElementLocated`: Element is visible
- `elementToBeClickable`: Element is clickable
- `textToBePresentInElement`: Text is present
- `invisibilityOfElementLocated`: Element is not visible

### Avoid Thread.sleep()

- **Never use** `Thread.sleep()` in production code
- Use explicit waits instead
- Only use for debugging purposes

## Driver Management

### Driver Factory

```java
public class DriverFactory {
    public static WebDriver createDriver(String browserType) {
        WebDriver driver = null;
        
        switch(browserType.toLowerCase()) {
            case "chrome":
                driver = new ChromeDriver();
                break;
            case "firefox":
                driver = new FirefoxDriver();
                break;
            case "edge":
                driver = new EdgeDriver();
                break;
            default:
                throw new IllegalArgumentException("Unsupported browser: " + browserType);
        }
        
        driver.manage().window().maximize();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        return driver;
    }
}
```

### Driver Lifecycle

```java
@BeforeMethod
public void setUp() {
    driver = DriverFactory.createDriver("chrome");
    driver.get(baseUrl);
}

@AfterMethod
public void tearDown() {
    if (driver != null) {
        driver.quit();
    }
}
```

## Browser Configuration

### Chrome Options

```java
ChromeOptions options = new ChromeOptions();
options.addArguments("--start-maximized");
options.addArguments("--disable-notifications");
options.addArguments("--disable-infobars");
options.setHeadless(false); // Set to true for headless mode

WebDriver driver = new ChromeDriver(options);
```

### Firefox Options

```java
FirefoxOptions options = new FirefoxOptions();
options.addArguments("--start-maximized");
options.setHeadless(false);

WebDriver driver = new FirefoxDriver(options);
```

## Element Interaction

### Common Actions

```java
// Click
element.click();

// Type text
element.sendKeys("text");

// Clear and type
element.clear();
element.sendKeys("text");

// Get text
String text = element.getText();

// Get attribute
String value = element.getAttribute("value");

// Check if displayed
boolean isDisplayed = element.isDisplayed();

// Check if enabled
boolean isEnabled = element.isEnabled();

// Select from dropdown
Select dropdown = new Select(element);
dropdown.selectByVisibleText("Option");
```

### JavaScript Execution

```java
JavascriptExecutor js = (JavascriptExecutor) driver;

// Scroll to element
js.executeScript("arguments[0].scrollIntoView(true);", element);

// Click element
js.executeScript("arguments[0].click();", element);

// Get page title
String title = (String) js.executeScript("return document.title;");
```

## Screenshot Capture

### On Test Failure

```java
@AfterMethod
public void captureScreenshot(ITestResult result) {
    if (result.getStatus() == ITestResult.FAILURE) {
        TakesScreenshot screenshot = (TakesScreenshot) driver;
        File sourceFile = screenshot.getScreenshotAs(OutputType.FILE);
        // Save screenshot
    }
}
```

### Custom Screenshot Utility

```java
public class ScreenshotUtil {
    public static void captureScreenshot(WebDriver driver, String testName) {
        TakesScreenshot screenshot = (TakesScreenshot) driver;
        File sourceFile = screenshot.getScreenshotAs(OutputType.FILE);
        String destination = "screenshots/" + testName + "_" + 
            System.currentTimeMillis() + ".png";
        // Save file
    }
}
```

## Handling Dynamic Elements

### Dynamic Locators

```java
// Using XPath with contains
By dynamicElement = By.xpath("//div[contains(@class, 'dynamic-')]");

// Using CSS with attribute starts with
By dynamicElement = By.cssSelector("div[class^='dynamic-']");
```

### Wait for Dynamic Content

```java
wait.until(ExpectedConditions.textToBePresentInElement(
    driver.findElement(By.id("status")), "Complete"));
```

## Handling Frames/IFrames

```java
// Switch to frame by index
driver.switchTo().frame(0);

// Switch to frame by name/ID
driver.switchTo().frame("frame-name");

// Switch to frame by element
driver.switchTo().frame(frameElement);

// Switch back to default content
driver.switchTo().defaultContent();
```

## Handling Alerts

```java
// Accept alert
Alert alert = driver.switchTo().alert();
alert.accept();

// Dismiss alert
alert.dismiss();

// Get alert text
String alertText = alert.getText();

// Send text to prompt
alert.sendKeys("text");
```

## Handling Windows/Tabs

```java
// Get current window handle
String mainWindow = driver.getWindowHandle();

// Get all window handles
Set<String> windows = driver.getWindowHandles();

// Switch to new window
for (String window : windows) {
    if (!window.equals(mainWindow)) {
        driver.switchTo().window(window);
        break;
    }
}

// Close current window and switch back
driver.close();
driver.switchTo().window(mainWindow);
```

## Best Practices

1. **Use Page Object Model**: Encapsulate page logic
2. **Use Explicit Waits**: Avoid Thread.sleep()
3. **Centralize Locators**: Easy to maintain
4. **Handle Dynamic Elements**: Use appropriate wait strategies
5. **Capture Screenshots**: On failures for debugging
6. **Clean Up**: Properly close drivers and resources
7. **Error Handling**: Handle exceptions gracefully
8. **Logging**: Log important actions and errors

## Common Patterns

### Page Factory Pattern (Alternative)

```java
@FindBy(id = "username")
WebElement userNameField;

@FindBy(id = "password")
WebElement passwordField;

public LoginPage(WebDriver driver) {
    PageFactory.initElements(driver, this);
}
```

### Fluent Interface Pattern

```java
public LoginPage enterUserName(String username) {
    userNameField.sendKeys(username);
    return this;
}

public LoginPage enterPassword(String password) {
    passwordField.sendKeys(password);
    return this;
}

// Usage: loginPage.enterUserName("user").enterPassword("pass").clickLogin();
```

## Related Documents

- `03_ARCHITECTURE/OVERVIEW.md` - Overall architecture
- `02_STANDARDS/CODE_STANDARDS.md` - Coding standards
- `02_STANDARDS/NAMING_CONVENTIONS.md` - Naming conventions

## Notes

[Any additional UI automation architecture information]
