# Task 10 - Error Responses

## Objective

Return clear JSON responses when API errors occur.

## Implementation

The API returns JSON error messages for invalid requests and missing resources.

A custom 404 error handler returns a JSON response instead of the default HTML error page.

## Testing

Invalid endpoint:

404 Not Found

Response:

{"error": "Resource not found"}

## Key Takeaway

Consistent JSON error responses make REST APIs easier for clients to handle.
