\# Task 14 - API Testing Using Postman



\## Objective



Test the Flask REST API endpoints using Postman.



\## Testing Results



| Method | Endpoint | Result |

|---|---|---|

| GET | /employees | 200 OK |

| GET | /employees/1 | 200 OK |

| POST | /employees | 201 Created |

| PUT | /employees/4 | 200 OK |

| DELETE | /employees/4 | 200 OK |



\## Postman Collection



The Postman collection is included in:



`PY-ADV-08/postman/Employee REST API.postman\_collection.json`



\## Testing Summary



All main employee CRUD API endpoints were tested successfully using Postman.



A temporary employee was created for POST and PUT testing and deleted after testing.



\## Key Takeaway



Postman can be used to send API requests and verify responses, status codes, and CRUD operations.

