class DatabaseError(Exception):
    """Base exception for database-related errors."""


class DatabaseConnectionError(DatabaseError):
    """Raised when a database connection fails."""


class DatabaseOperationError(DatabaseError):
    """Raised when a database operation fails."""