# Local Setup Guide

## Purpose

This document provides step-by-step instructions for setting up the local development environment for QA automation.

## Prerequisites

### Required Software
- **Java**: [Version, e.g., Java 11 or 17]
- **Maven**: [Version, e.g., Maven 3.8+]
- **Git**: [Version]
- **IDE**: [IntelliJ IDEA, Eclipse, VS Code, etc.]
- **Browser**: Chrome, Firefox, Edge (for UI tests)

### System Requirements
- **OS**: [Windows, macOS, Linux]
- **RAM**: [Minimum, e.g., 8GB recommended]
- **Disk Space**: [Minimum, e.g., 10GB free]

## Setup Steps

### Step 1: Install Java

#### Windows
1. Download JDK from [Oracle/OpenJDK website]
2. Run installer
3. Set JAVA_HOME environment variable
4. Add Java to PATH
5. Verify: `java -version`

#### macOS
```bash
# Using Homebrew
brew install openjdk@11

# Or download from Oracle/OpenJDK website
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install openjdk-11-jdk

# Verify
java -version
```

### Step 2: Install Maven

#### Windows
1. Download Maven from [Apache Maven website]
2. Extract to desired location (e.g., `C:\Program Files\Apache\maven`)
3. Set M2_HOME environment variable
4. Add Maven bin to PATH
5. Verify: `mvn -version`

#### macOS
```bash
# Using Homebrew
brew install maven

# Verify
mvn -version
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install maven

# Verify
mvn -version
```

### Step 3: Install Git

#### Windows
1. Download Git from [Git website]
2. Run installer
3. Use default settings (or customize)
4. Verify: `git --version`

#### macOS
```bash
# Git usually pre-installed, or:
brew install git

# Verify
git --version
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install git

# Verify
git --version
```

### Step 4: Clone Repository

```bash
# Clone the repository
git clone [repository-url]

# Navigate to project directory
cd qa-automation-kb

# Verify structure
ls -la
```

### Step 5: IDE Setup

#### IntelliJ IDEA
1. Install IntelliJ IDEA (Community or Ultimate)
2. Open project: File → Open → Select project directory
3. Import Maven project (if prompted)
4. Wait for Maven dependencies to download
5. Configure JDK: File → Project Structure → Project → SDK
6. Install plugins (if needed):
   - Cucumber for Java
   - Gherkin
   - TestNG

#### Eclipse
1. Install Eclipse IDE for Java Developers
2. Import project: File → Import → Maven → Existing Maven Projects
3. Select project directory
4. Wait for Maven dependencies
5. Configure JDK: Project → Properties → Java Build Path

#### VS Code
1. Install VS Code
2. Install extensions:
   - Java Extension Pack
   - Test Runner for Java
   - Cucumber
3. Open project folder
4. Maven dependencies will download automatically

### Step 6: Maven Configuration

#### Verify Maven Settings
```bash
# Check Maven version
mvn -version

# Verify Maven can download dependencies
mvn dependency:resolve
```

#### Local Configuration
1. Create `config/local.properties` (copy from `config/local.properties.example`)
2. Update with local settings:
   ```properties
   # Environment
   test.environment=local
   
   # Browser
   browser.type=chrome
   
   # URLs (if applicable)
   base.url=http://localhost:8080
   ```

### Step 7: Browser Drivers

#### ChromeDriver
```bash
# Download ChromeDriver matching your Chrome version
# Place in project directory or system PATH
# Or use WebDriverManager (if configured in project)
```

#### GeckoDriver (Firefox)
```bash
# Download GeckoDriver
# Place in project directory or system PATH
```

#### EdgeDriver
```bash
# Download EdgeDriver matching your Edge version
# Place in project directory or system PATH
```

**Note**: If project uses WebDriverManager, drivers will be downloaded automatically.

### Step 8: Build Project

```bash
# Navigate to project directory
cd [project-directory]

# Clean and build
mvn clean install

# Or skip tests for initial build
mvn clean install -DskipTests
```

### Step 9: Run First Test

#### Run via Maven
```bash
# Run all tests
mvn test

# Run specific test class
mvn test -Dtest=LoginTest

# Run specific test group
mvn test -Dgroups=smoke
```

#### Run via IDE
1. Navigate to test class
2. Right-click → Run
3. Or use TestNG runner

### Step 10: Verify Setup

#### Checklist
- [ ] Java installed and configured
- [ ] Maven installed and configured
- [ ] Git installed and configured
- [ ] Repository cloned
- [ ] IDE set up and project imported
- [ ] Maven dependencies downloaded
- [ ] Local configuration file created
- [ ] Browser drivers available
- [ ] Project builds successfully
- [ ] Can run a test

## Common Issues

### Issue: Maven Dependencies Not Downloading
**Solution**:
- Check internet connection
- Verify Maven settings.xml
- Check proxy settings (if behind corporate proxy)
- Try: `mvn clean install -U`

### Issue: Java Version Mismatch
**Solution**:
- Verify JAVA_HOME points to correct Java version
- Check IDE Java version settings
- Ensure Maven uses correct Java version

### Issue: Browser Driver Not Found
**Solution**:
- Download correct driver version
- Add driver to PATH
- Or use WebDriverManager (if available)
- Check driver path in configuration

### Issue: Tests Fail with Connection Errors
**Solution**:
- Verify environment URL in configuration
- Check network connectivity
- Verify environment is accessible
- Check firewall settings

### More Issues
See `05_ONBOARDING/COMMON_FAILURES.md` for more common issues and solutions.

## Next Steps

1. Review `05_ONBOARDING/ONBOARDING_7_DAY.md`
2. Complete Day 1 tasks
3. Request environment access (see `05_ONBOARDING/ACCESS_SETUP.md`)
4. Start with first tasks (see `05_ONBOARDING/FIRST_5_TASKS.md`)

## Support

If you encounter issues:
1. Check `05_ONBOARDING/COMMON_FAILURES.md`
2. Ask mentor or team
3. Check team chat/channel
4. Review project documentation

## Notes

[Any additional setup information or team-specific notes]
