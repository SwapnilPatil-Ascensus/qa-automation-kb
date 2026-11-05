# API Automation Architecture

## Purpose

This document describes the architecture and design of API automation framework using REST Assured.

## Architecture Overview

```
Test Layer (TestNG)
    ↓
API Test Classes
    ↓
API Client/Request Builder
    ↓
REST Assured
    ↓
HTTP Client
    ↓
API Endpoints
```

## REST Assured Framework

### Basic Setup

```java
import io.restassured.RestAssured;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;

public class ApiClient {
    private String baseUrl;
    private RequestSpecification requestSpec;
    
    public ApiClient(String baseUrl) {
        this.baseUrl = baseUrl;
        RestAssured.baseURI = baseUrl;
        requestSpec = RestAssured.given();
    }
}
```

### Request Building

#### GET Request

```java
Response response = RestAssured.given()
    .header("Content-Type", "application/json")
    .header("Authorization", "Bearer " + token)
    .queryParam("userId", "123")
    .when()
    .get("/api/users")
    .then()
    .extract()
    .response();
```

#### POST Request

```java
Response response = RestAssured.given()
    .header("Content-Type", "application/json")
    .header("Authorization", "Bearer " + token)
    .body(requestBody)
    .when()
    .post("/api/users")
    .then()
    .extract()
    .response();
```

#### PUT Request

```java
Response response = RestAssured.given()
    .header("Content-Type", "application/json")
    .header("Authorization", "Bearer " + token)
    .body(requestBody)
    .when()
    .put("/api/users/123")
    .then()
    .extract()
    .response();
```

#### DELETE Request

```java
Response response = RestAssured.given()
    .header("Authorization", "Bearer " + token)
    .when()
    .delete("/api/users/123")
    .then()
    .extract()
    .response();
```

## Request Specification

### Reusable Request Spec

```java
RequestSpecification requestSpec = RestAssured.given()
    .baseUri("https://api.example.com")
    .basePath("/api/v1")
    .header("Content-Type", "application/json")
    .header("Accept", "application/json")
    .log().all();

// Use in requests
Response response = RestAssured.given()
    .spec(requestSpec)
    .header("Authorization", "Bearer " + token)
    .when()
    .get("/users");
```

### Request Builder Pattern

```java
public class ApiRequestBuilder {
    private RequestSpecification request;
    
    public ApiRequestBuilder() {
        this.request = RestAssured.given();
    }
    
    public ApiRequestBuilder withBaseUrl(String baseUrl) {
        RestAssured.baseURI = baseUrl;
        return this;
    }
    
    public ApiRequestBuilder withHeader(String name, String value) {
        request.header(name, value);
        return this;
    }
    
    public ApiRequestBuilder withBody(Object body) {
        request.body(body);
        return this;
    }
    
    public ApiRequestBuilder withQueryParam(String name, String value) {
        request.queryParam(name, value);
        return this;
    }
    
    public Response get(String endpoint) {
        return request.when().get(endpoint).then().extract().response();
    }
    
    public Response post(String endpoint) {
        return request.when().post(endpoint).then().extract().response();
    }
}
```

## Response Validation

### Status Code Validation

```java
RestAssured.given()
    .when()
    .get("/api/users")
    .then()
    .statusCode(200);
```

### Response Body Validation

```java
// JSON Path validation
RestAssured.given()
    .when()
    .get("/api/users/123")
    .then()
    .statusCode(200)
    .body("id", equalTo(123))
    .body("name", equalTo("John Doe"))
    .body("email", equalTo("john@example.com"));

// Extract and validate
Response response = RestAssured.given()
    .when()
    .get("/api/users/123")
    .then()
    .extract()
    .response();

int id = response.jsonPath().getInt("id");
String name = response.jsonPath().getString("name");
```

### Response Schema Validation

```java
RestAssured.given()
    .when()
    .get("/api/users/123")
    .then()
    .statusCode(200)
    .body(matchesJsonSchemaInClasspath("user-schema.json"));
```

## Authentication

### Bearer Token

```java
RestAssured.given()
    .header("Authorization", "Bearer " + token)
    .when()
    .get("/api/users");
```

### Basic Authentication

```java
RestAssured.given()
    .auth().basic("username", "password")
    .when()
    .get("/api/users");
```

### OAuth 2.0

```java
RestAssured.given()
    .auth().oauth2(accessToken)
    .when()
    .get("/api/users");
```

### API Key

```java
RestAssured.given()
    .header("X-API-Key", apiKey)
    .when()
    .get("/api/users");
```

## Request/Response Models

### POJO for Request Body

```java
public class UserRequest {
    private String name;
    private String email;
    private String role;
    
    // Getters and setters
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    // ... other getters/setters
}
```

### POJO for Response Body

```java
public class UserResponse {
    private int id;
    private String name;
    private String email;
    private String role;
    private String createdAt;
    
    // Getters and setters
}
```

### Using POJOs

```java
// Create request
UserRequest userRequest = new UserRequest();
userRequest.setName("John Doe");
userRequest.setEmail("john@example.com");

// Send request
Response response = RestAssured.given()
    .body(userRequest)
    .when()
    .post("/api/users")
    .then()
    .extract()
    .response();

// Parse response
UserResponse userResponse = response.as(UserResponse.class);
```

## API Client Pattern

### Centralized API Client

```java
public class UserApiClient {
    private String baseUrl;
    private String token;
    
    public UserApiClient(String baseUrl, String token) {
        this.baseUrl = baseUrl;
        this.token = token;
    }
    
    public Response getUser(int userId) {
        return RestAssured.given()
            .baseUri(baseUrl)
            .header("Authorization", "Bearer " + token)
            .when()
            .get("/api/users/" + userId)
            .then()
            .extract()
            .response();
    }
    
    public Response createUser(UserRequest userRequest) {
        return RestAssured.given()
            .baseUri(baseUrl)
            .header("Authorization", "Bearer " + token)
            .header("Content-Type", "application/json")
            .body(userRequest)
            .when()
            .post("/api/users")
            .then()
            .extract()
            .response();
    }
    
    public Response updateUser(int userId, UserRequest userRequest) {
        return RestAssured.given()
            .baseUri(baseUrl)
            .header("Authorization", "Bearer " + token)
            .header("Content-Type", "application/json")
            .body(userRequest)
            .when()
            .put("/api/users/" + userId)
            .then()
            .extract()
            .response();
    }
    
    public Response deleteUser(int userId) {
        return RestAssured.given()
            .baseUri(baseUrl)
            .header("Authorization", "Bearer " + token)
            .when()
            .delete("/api/users/" + userId)
            .then()
            .extract()
            .response();
    }
}
```

## Test Data Management

### JSON Request Body

```java
// From file
String requestBody = new String(Files.readAllBytes(
    Paths.get("src/test/resources/data/user-request.json")));

// From string
String requestBody = "{\"name\":\"John Doe\",\"email\":\"john@example.com\"}";

// From POJO
UserRequest userRequest = new UserRequest();
userRequest.setName("John Doe");
```

### Data Providers

```java
@DataProvider(name = "userData")
public Object[][] getUserData() {
    return new Object[][] {
        {"John Doe", "john@example.com"},
        {"Jane Smith", "jane@example.com"}
    };
}

@Test(dataProvider = "userData")
public void testCreateUser(String name, String email) {
    UserRequest userRequest = new UserRequest();
    userRequest.setName(name);
    userRequest.setEmail(email);
    
    Response response = userApiClient.createUser(userRequest);
    Assert.assertEquals(response.getStatusCode(), 201);
}
```

## Error Handling

### Expected Errors

```java
RestAssured.given()
    .when()
    .get("/api/users/999")
    .then()
    .statusCode(404)
    .body("error", equalTo("User not found"));
```

### Exception Handling

```java
try {
    Response response = RestAssured.given()
        .when()
        .get("/api/users/999");
    
    if (response.getStatusCode() != 200) {
        logger.error("API call failed with status: " + response.getStatusCode());
    }
} catch (Exception e) {
    logger.error("Error calling API", e);
}
```

## Logging

### Request/Response Logging

```java
// Log all
RestAssured.given()
    .log().all()
    .when()
    .get("/api/users");

// Log only if validation fails
RestAssured.given()
    .log().ifValidationFails()
    .when()
    .get("/api/users")
    .then()
    .statusCode(200);

// Log request only
RestAssured.given()
    .log().method()
    .log().uri()
    .when()
    .get("/api/users");
```

## Best Practices

1. **Use Request Specifications**: Reusable request configs
2. **Centralize API Clients**: One client per API/service
3. **Use POJOs**: Type-safe request/response handling
4. **Validate Responses**: Always validate status codes and body
5. **Handle Errors**: Proper error handling and logging
6. **Externalize Test Data**: Don't hardcode test data
7. **Use Data Providers**: For parameterized tests
8. **Log Appropriately**: Log requests/responses for debugging

## Common Patterns

### Base API Client

```java
public abstract class BaseApiClient {
    protected String baseUrl;
    protected String token;
    
    protected RequestSpecification getRequestSpec() {
        return RestAssured.given()
            .baseUri(baseUrl)
            .header("Authorization", "Bearer " + token)
            .header("Content-Type", "application/json");
    }
}
```

### Response Validator

```java
public class ResponseValidator {
    public static void validateStatusCode(Response response, int expectedStatus) {
        Assert.assertEquals(response.getStatusCode(), expectedStatus,
            "Expected status code " + expectedStatus + " but got " + response.getStatusCode());
    }
    
    public static void validateResponseTime(Response response, long maxTime) {
        Assert.assertTrue(response.getTime() < maxTime,
            "Response time exceeded " + maxTime + "ms");
    }
}
```

## Related Documents

- `03_ARCHITECTURE/OVERVIEW.md` - Overall architecture
- `02_STANDARDS/CODE_STANDARDS.md` - Coding standards
- `03_ARCHITECTURE/TEST_DATA_STRATEGY.md` - Test data management

## Notes

[Any additional API automation architecture information]
