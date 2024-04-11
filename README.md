# Evaluation Review

## Overview
This project aims to provide a solution for managing content compliance within enterprises. It facilitates the creation, upload, review, and tracking of content adherence to predefined guidelines.


## Setup and Running the Project
- Instructions for installing dependencies and running the project:
  1. Clone the repository: `git clone <repository_url>`
  2. Navigate to the project directory: `cd <project_directory>`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Apply migrations: `python manage.py migrate`
  5. Run the development server: `python manage.py runserver`
  6. Access the project in your web browser at `http://127.0.0.1:8000/`


## Approach to the Problem
- Understanding the requirements.
- Breaking down the problem into smaller tasks.

## Design Decisions
- Design approach:
  - Domain-Driven Design (DDD): Each Django app represents a specific domain or component of the system, such as compliance, content, and review. Each app encapsulates related models, views, serializers, and URLs, focusing on specific functionalities within that domain.
  - MVC architecture

- Object-oriented design principles followed, SOLID principals:
  - Single Responsibility Principle (SRP)
  - Open/Closed Principle (OCP)
  - Liskov Substitution Principle (LSP)
  - Interface Segregation Principle (ISP)
  - Dependency Inversion Principle (DIP)


## Code Readability and Conventions
- Focucing on code readability, adherence to language conventions, and logical packaging/directory structure.

## Testing
- **Testing Approach:** Implemented unit tests and integration tests for critical functionalities.
- **Test Coverage:** Aimed for high test coverage, especially for core functionalities.
- **Testing Tools/Frameworks:** Used Django's built-in testing framework for writing and executing tests.
- To run the test:
```@bash
    cd apps/
    python3 ../manage.py test
```

## Version Control
- The commits to the project are intended to be modular as best as possible following the best industrial foramt.

## Usage
Here are the curls that can be used for the operations performed by user onto the system.
### Compliance User APIs:
1. Define Guideline:
```@bash
    curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"title": "Do not use discriminative language in job descriptions", "description": "Ensure job descriptions do not contain discriminative language."}' \
  http://127.0.0.1:8000/api/v1/compliance/
```
2. Update Guideline:

```@bash
    curl -X PUT \
    -H "Content-Type: application/json" \
    -d '{"title": "Do not use discriminative language in job descriptions", "description": "Ensure job descriptions do not contain discriminatory language."}' \
    http://127.0.0.1:8000/api/v1/guidelines/<int:pk>/
```
### Author APIs for Content Upload:
1. Upload Content:
```@bash
    curl -X POST -F "file=@/path/to/your/file.txt"              http://127.0.0.1:8000/api/v1/content/upload/
```
2. Update Content:
```@bash
    curl -X PUT -F "file=@/path/to/your/updated_file.txt" http://127.0.0.1:8000/api/v1/content/update/<int:pk>/
```
3. Track Review Status:
```@bash
    curl -X GET http://127.0.0.1:8000/api/v1/content/1/review/status/
```
### Reviewer APIs for Fetching Content and Status:
1. Fetch All Content and Status:
```@bash
    curl -X GET http://127.0.0.1:8000/api/v1/review/content-review-detail/
```
### Reviewer APIs for Reviewing Content:
1. Review Create:
```@bash
   curl --location 'http://127.0.0.1:8000/api/v1/review/create/' \
    --header 'Content-Type: application/json' \
    --data '{
    "content_id": 2,
    "guideline": 1,
    "passed": true
}'
```
2. Review Update:
```@bash
        curl --location --request PATCH 'http://127.0.0.1:8000/api/v1/review/update/<int:pk>/' \
    --header 'Content-Type: application/json' \
    --data '{
    "passed": true
}'

## Future Improvements
- Implementing the Auth framework will help in user identification and actions based on permissions.
- Tests can be added covering all the test cases for each operation
