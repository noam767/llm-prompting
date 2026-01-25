# Python Documentation Skill

## Overview
This skill provides comprehensive guidance for documenting Python code following official PEP standards and industry best practices. It covers all Python constructs including modules, functions, classes, methods, decorators, and more.

## Core Standards & PEPs

### PEP 8 - Style Guide for Python Code
- **Line Length**: 79 characters for code, 72 characters for docstrings and comments
- **Indentation**: 4 spaces (never tabs)
- **Quotes**: Use `"""triple double quotes"""` for all docstrings
- **Blank Lines**: 2 blank lines around top-level functions/classes, 1 blank line between methods

### PEP 257 - Docstring Conventions
- **Placement**: Immediately after definition (module, class, function, method)
- **One-line docstrings**: Opening and closing quotes on same line
- **Multi-line docstrings**: Summary line first, blank line, then details, closing quotes on separate line
- **Content**: Describe what the code does, not how it does it
- **Imperative mood**: "Return" not "Returns", "Calculate" not "Calculates"

### PEP 484 - Type Hints
- **Function annotations**: `def func(arg: str) -> int:`
- **Variable annotations**: `my_var: int = 5`
- **Optional types**: Use `Optional[Type]` or `Type | None` (Python 3.10+)
- **Collections**: `List[int]`, `Dict[str, Any]`, `Tuple[str, ...]`
- **Compatibility**: When using type hints, types in docstrings can be omitted

### PEP 526 - Variable Annotations
- Syntax for annotating class and instance variables
- Example: `class_var: ClassVar[int] = 0`

## Docstring Formats

Choose ONE format per project and use it consistently. The three major formats are:

### 1. Google Style (Recommended for General Use)
**Best for**: Most projects, good readability, clean syntax

```python
def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle.
    
    This function takes length and width measurements and returns
    the calculated area. Supports both integer and float inputs.
    
    Args:
        length: The length of the rectangle in meters.
        width: The width of the rectangle in meters.
    
    Returns:
        The calculated area in square meters.
    
    Raises:
        ValueError: If length or width is negative.
    
    Example:
        >>> calculate_area(5.0, 3.0)
        15.0
    """
    if length < 0 or width < 0:
        raise ValueError("Dimensions must be positive")
    return length * width
```

### 2. NumPy Style (Recommended for Scientific Computing)
**Best for**: Data science, scientific computing, mathematical functions

```python
def calculate_statistics(data: np.ndarray) -> dict:
    """Calculate statistical measures for a dataset.
    
    Computes mean, median, and standard deviation for the input array.
    Handles missing values by ignoring them in calculations.
    
    Parameters
    ----------
    data : np.ndarray
        Input array containing numerical data. NaN values are ignored.
    
    Returns
    -------
    dict
        Dictionary with keys 'mean', 'median', 'std' containing the
        respective statistical measures.
    
    Raises
    ------
    ValueError
        If input array is empty or contains only NaN values.
    
    See Also
    --------
    numpy.nanmean : Compute mean, ignoring NaNs
    numpy.nanstd : Compute standard deviation, ignoring NaNs
    
    Notes
    -----
    This function uses NumPy's nan-aware statistical functions
    internally for robust handling of missing data.
    
    Examples
    --------
    >>> import numpy as np
    >>> data = np.array([1, 2, 3, 4, 5])
    >>> calculate_statistics(data)
    {'mean': 3.0, 'median': 3.0, 'std': 1.41}
    """
    pass
```

### 3. Sphinx/reST Style (Recommended for Complex Documentation)
**Best for**: Large projects with extensive cross-referencing needs

```python
def process_data(input_file: str, output_format: str = 'json') -> bool:
    """Process data from input file and convert to specified format.
    
    :param input_file: Path to the input data file
    :type input_file: str
    :param output_format: Desired output format ('json', 'csv', 'xml')
    :type output_format: str
    :returns: True if processing succeeded, False otherwise
    :rtype: bool
    :raises FileNotFoundError: If input file doesn't exist
    :raises ValueError: If output_format is not supported
    """
    pass
```

## Documentation by Code Element

### Module-Level Documentation

```python
"""Module for data processing and analysis.

This module provides utilities for loading, transforming, and analyzing
large datasets. It includes functions for data validation, cleaning,
and statistical analysis.

Example:
    Basic usage of the module::
    
        from data_utils import load_data, analyze
        
        data = load_data('input.csv')
        results = analyze(data)

Attributes:
    DEFAULT_ENCODING (str): Default character encoding for file operations.
    MAX_CHUNK_SIZE (int): Maximum size in bytes for chunked processing.

Todo:
    * Add support for Parquet files
    * Implement parallel processing for large datasets
"""

DEFAULT_ENCODING = 'utf-8'
MAX_CHUNK_SIZE = 1024 * 1024  # 1MB
```

### Function Documentation

```python
def validate_email(email: str, allow_subdomains: bool = True) -> bool:
    """Validate email address format.
    
    Checks if the provided string matches standard email format
    requirements including local part, @ symbol, and domain.
    
    Args:
        email: Email address string to validate.
        allow_subdomains: Whether to allow subdomain addresses.
            Defaults to True.
    
    Returns:
        True if email is valid, False otherwise.
    
    Raises:
        TypeError: If email is not a string.
    
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid.email")
        False
    """
    pass
```

### Class Documentation

```python
class DataProcessor:
    """Process and transform structured data.
    
    This class provides methods for loading, validating, and transforming
    data from various sources. It maintains internal state for configuration
    and cached results.
    
    Attributes:
        config (dict): Configuration settings for processing.
        cache_enabled (bool): Whether to cache processed results.
        _cache (dict): Internal cache storage (private).
    
    Example:
        >>> processor = DataProcessor(cache_enabled=True)
        >>> processor.load('data.csv')
        >>> results = processor.transform()
    """
    
    def __init__(self, cache_enabled: bool = False):
        """Initialize DataProcessor.
        
        Args:
            cache_enabled: Enable result caching. Defaults to False.
        """
        self.config = {}
        self.cache_enabled = cache_enabled
        self._cache = {}
    
    def load(self, filepath: str) -> None:
        """Load data from file.
        
        Args:
            filepath: Path to the data file.
        
        Raises:
            FileNotFoundError: If filepath doesn't exist.
            ValueError: If file format is unsupported.
        """
        pass
    
    @property
    def processed_count(self) -> int:
        """int: Number of processed records (read-only)."""
        return len(self._cache)
    
    @staticmethod
    def validate_format(data: dict) -> bool:
        """Validate data structure format.
        
        Args:
            data: Dictionary to validate.
        
        Returns:
            True if format is valid, False otherwise.
        
        Note:
            This is a static method and doesn't require instance state.
        """
        pass
```

### Decorator Documentation

```python
from functools import wraps
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def retry(max_attempts: int = 3):
    """Decorator to retry function execution on failure.
    
    Wraps a function to automatically retry execution if an exception
    is raised, up to the specified maximum number of attempts.
    
    Args:
        max_attempts: Maximum number of retry attempts. Defaults to 3.
    
    Returns:
        Decorated function that implements retry logic.
    
    Example:
        >>> @retry(max_attempts=5)
        ... def fetch_data(url):
        ...     return requests.get(url)
    
    Note:
        Each retry includes exponential backoff delay.
    """
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        """Inner decorator function.
        
        Args:
            func: Function to wrap with retry logic.
        
        Returns:
            Wrapped function with retry capability.
        """
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            """Execute function with retry logic.
            
            Args:
                *args: Positional arguments for wrapped function.
                **kwargs: Keyword arguments for wrapped function.
            
            Returns:
                Result from successful function execution.
            
            Raises:
                Exception: The last exception if all retries fail.
            """
            pass
        return wrapper
    return decorator
```

### Generator Documentation

```python
from typing import Generator

def read_chunks(filepath: str, chunk_size: int = 1024) -> Generator[bytes, None, None]:
    """Read file in chunks.
    
    Args:
        filepath: Path to file to read.
        chunk_size: Size of each chunk in bytes. Defaults to 1024.
    
    Yields:
        Bytes object containing next chunk of file data.
    
    Raises:
        FileNotFoundError: If filepath doesn't exist.
    
    Example:
        >>> for chunk in read_chunks('large_file.bin'):
        ...     process(chunk)
    """
    pass
```

### Exception Documentation

```python
class DataValidationError(Exception):
    """Exception raised for data validation failures.
    
    Attributes:
        message: Human-readable error description.
        field: Name of the field that failed validation.
        value: The invalid value that was provided.
    
    Example:
        >>> raise DataValidationError("Invalid age", field="age", value=-5)
    """
    
    def __init__(self, message: str, field: str = None, value: any = None):
        """Initialize exception.
        
        Args:
            message: Error description.
            field: Field name that failed validation. Defaults to None.
            value: Invalid value. Defaults to None.
        """
        self.message = message
        self.field = field
        self.value = value
        super().__init__(self.message)
```

## Type Hinting Best Practices

### Basic Type Hints

```python
from typing import List, Dict, Optional, Union, Tuple, Any, Callable

def process_items(
    items: List[str],
    config: Dict[str, Any],
    max_count: Optional[int] = None
) -> Tuple[int, List[str]]:
    """Process list of items with configuration.
    
    Args:
        items: List of item identifiers to process.
        config: Configuration dictionary with processing parameters.
        max_count: Maximum items to process. None means no limit.
    
    Returns:
        Tuple containing processed count and list of failed items.
    """
    pass
```

### Modern Type Hints (Python 3.10+)

```python
def find_user(user_id: int) -> dict[str, str] | None:
    """Find user by ID.
    
    Args:
        user_id: Unique user identifier.
    
    Returns:
        User data dictionary or None if not found.
    """
    pass
```

### Generic Types

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Container(Generic[T]):
    """Generic container for items of any type.
    
    Type Parameters:
        T: The type of items stored in the container.
    
    Attributes:
        items: List of stored items.
    
    Example:
        >>> container = Container[int]()
        >>> container.add(42)
    """
    
    def __init__(self):
        """Initialize empty container."""
        self.items: List[T] = []
    
    def add(self, item: T) -> None:
        """Add item to container.
        
        Args:
            item: Item to add.
        """
        self.items.append(item)
```

## Special Cases

### Property Documentation

```python
class User:
    """Represent a user account."""
    
    def __init__(self, username: str, email: str):
        self._username = username
        self._email = email
    
    @property
    def username(self) -> str:
        """str: The user's username (read-only)."""
        return self._username
    
    @property
    def email(self) -> str:
        """str: The user's email address."""
        return self._email
    
    @email.setter
    def email(self, value: str) -> None:
        """Set user's email address.
        
        Args:
            value: New email address.
        
        Raises:
            ValueError: If email format is invalid.
        """
        if '@' not in value:
            raise ValueError("Invalid email format")
        self._email = value
```

### Abstract Base Class Documentation

```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    """Abstract base class for data sources.
    
    Defines the interface that all data source implementations must follow.
    Subclasses must implement the load and save methods.
    
    Example:
        To create a custom data source::
        
            class MySource(DataSource):
                def load(self, path):
                    # implementation
                    pass
                
                def save(self, data, path):
                    # implementation
                    pass
    """
    
    @abstractmethod
    def load(self, path: str) -> Any:
        """Load data from source.
        
        Args:
            path: Location identifier for data.
        
        Returns:
            Loaded data in appropriate format.
        
        Raises:
            NotImplementedError: Must be implemented by subclass.
        """
        pass
```

### Async Function Documentation

```python
async def fetch_data(url: str, timeout: int = 30) -> dict:
    """Asynchronously fetch data from URL.
    
    Args:
        url: Target URL to fetch from.
        timeout: Request timeout in seconds. Defaults to 30.
    
    Returns:
        Parsed JSON response as dictionary.
    
    Raises:
        asyncio.TimeoutError: If request exceeds timeout.
        aiohttp.ClientError: If request fails.
    
    Example:
        >>> data = await fetch_data('https://api.example.com/data')
    """
    pass
```

## Documentation Workflow

### Step 1: Analyze the Code
Before documenting, understand:
- What does it do? (purpose)
- What are the inputs? (parameters, types)
- What are the outputs? (return values, types)
- What can go wrong? (exceptions)
- How should it be used? (examples)

### Step 2: Choose Format
- **Google**: General-purpose projects, clean and readable
- **NumPy**: Scientific/data science projects, detailed sections
- **Sphinx**: Large projects with complex cross-references

### Step 3: Document Structure
**For Functions/Methods**:
1. Summary line (one sentence, < 80 chars)
2. Blank line (if multi-line)
3. Extended description (optional)
4. Args/Parameters section
5. Returns section
6. Raises section (if applicable)
7. Example section (encouraged)
8. Notes (optional)

**For Classes**:
1. Summary line
2. Extended description
3. Attributes section
4. Example of class usage

**For Modules**:
1. Summary line
2. Extended description
3. Module-level attributes
4. Usage example

### Step 4: Include Type Information
- Use PEP 484 type hints in function signatures
- With type hints, you can omit types from docstring (Google/NumPy style)
- Without type hints, include types in docstring

### Step 5: Add Examples
- Include at least one example for public APIs
- Use doctest format when possible
- Show realistic usage patterns

## Common Patterns

### Documentation with Type Hints (Preferred)

```python
def merge_dicts(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    """Merge two dictionaries, summing values for common keys.
    
    Args:
        dict1: First dictionary to merge.
        dict2: Second dictionary to merge.
    
    Returns:
        Merged dictionary with summed values.
    
    Example:
        >>> merge_dicts({'a': 1}, {'a': 2, 'b': 3})
        {'a': 3, 'b': 3}
    """
    pass
```

### Documentation without Type Hints

```python
def merge_dicts(dict1, dict2):
    """Merge two dictionaries, summing values for common keys.
    
    Args:
        dict1 (dict[str, int]): First dictionary to merge.
        dict2 (dict[str, int]): Second dictionary to merge.
    
    Returns:
        dict[str, int]: Merged dictionary with summed values.
    
    Example:
        >>> merge_dicts({'a': 1}, {'a': 2, 'b': 3})
        {'a': 3, 'b': 3}
    """
    pass
```

### Private Methods

```python
class DataHandler:
    """Handle data operations."""
    
    def process(self, data: List[Any]) -> List[Any]:
        """Process data through validation and transformation.
        
        Args:
            data: Input data to process.
        
        Returns:
            Processed and validated data.
        """
        validated = self._validate(data)
        return self._transform(validated)
    
    def _validate(self, data: List[Any]) -> List[Any]:
        # Private method - comment explains implementation
        # Validates data against schema rules
        # Returns only valid items
        return [item for item in data if self._is_valid(item)]
```

## Tools for Enforcement

### Linters and Formatters
- **ruff**: Fast, comprehensive linter and formatter
- **pylint**: Traditional linter with extensive checks
- **flake8**: Combines multiple tools (pycodestyle, pyflakes, mccabe)
- **black**: Opinionated code formatter
- **pydocstyle/docformatter**: Docstring-specific linters

### Type Checkers
- **mypy**: The standard static type checker
- **pyright**: Microsoft's fast type checker
- **pyre**: Facebook's type checker

### Documentation Generators
- **Sphinx**: Industry standard, supports all formats
- **pdoc**: Lightweight auto-documentation
- **mkdocs**: Modern Markdown-based documentation
- **mkdocstrings**: MkDocs with Python docstring support

## Quick Reference

### One-Line Docstring Template
```python
def simple_func(x: int) -> str:
    """Convert integer to string representation."""
    return str(x)
```

### Multi-Line Docstring Template (Google Style)
```python
def complex_func(param1: Type1, param2: Type2 = default) -> ReturnType:
    """Brief summary of function purpose.
    
    More detailed description if needed, explaining behavior,
    algorithms used, or important considerations.
    
    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to default.
    
    Returns:
        Description of return value.
    
    Raises:
        ExceptionType: When this exception occurs.
    
    Example:
        >>> complex_func(value1, value2)
        expected_result
    """
    pass
```

### Class Template (Google Style)
```python
class ExampleClass:
    """Brief description of the class.
    
    Extended description explaining class purpose, behavior,
    and usage patterns.
    
    Attributes:
        attr1: Description of attr1.
        attr2: Description of attr2.
    
    Example:
        >>> obj = ExampleClass(value)
        >>> result = obj.method()
    """
    
    def __init__(self, param: Type):
        """Initialize ExampleClass.
        
        Args:
            param: Description of initialization parameter.
        """
        self.attr1 = param
        self.attr2 = None
```

## Critical Rules

1. **Always document public APIs** - modules, functions, classes, methods
2. **Be concise** - summary line must be one line, under 80 characters
3. **Use imperative mood** - "Return value" not "Returns value"
4. **Include examples** - especially for non-obvious behavior
5. **Document exceptions** - list all exceptions that can be raised
6. **Keep docstrings current** - update when code changes
7. **Don't repeat signatures** - type hints make parameter types redundant
8. **Use consistent format** - choose one style per project
9. **Private methods use comments** - full docstrings only for public API
10. **Test your examples** - ensure doctest examples actually work

## Anti-Patterns to Avoid

### ❌ Don't: Redundant information
```python
def add(a: int, b: int) -> int:
    """Add two integers.
    
    Args:
        a (int): The first integer to add
        b (int): The second integer to add
    
    Returns:
        int: The sum of a and b
    """
    return a + b
```

### ✅ Do: Concise with type hints
```python
def add(a: int, b: int) -> int:
    """Return sum of two integers."""
    return a + b
```

### ❌ Don't: Implementation details in docstring
```python
def calculate_total(items: List[float]) -> float:
    """Calculate total by iterating through items list and using
    the sum() built-in function to add all values together."""
    return sum(items)
```

### ✅ Do: What it does, not how
```python
def calculate_total(items: List[float]) -> float:
    """Calculate sum of all item values.
    
    Args:
        items: List of numeric values to sum.
    
    Returns:
        Total sum of all values.
    """
    return sum(items)
```

### ❌ Don't: Incorrect multi-line format
```python
def bad_format(x):
    """This is wrong.
    It doesn't have a blank line after summary."""
    pass
```

### ✅ Do: Correct multi-line format
```python
def good_format(x: int) -> str:
    """This is correct.
    
    It has a blank line separating the summary from details.
    
    Args:
        x: Input value.
    
    Returns:
        String representation.
    """
    pass
```

## Implementation Guide

When Claude uses this skill to document Python code:

1. **Read the code** to understand functionality, inputs, outputs, exceptions
2. **Identify the code type** - module/function/class/method/decorator/etc
3. **Check for type hints** - if present, omit types from docstring
4. **Choose appropriate format** - default to Google unless specified
5. **Write summary line** - one line, imperative mood, < 80 chars
6. **Add sections** - Args, Returns, Raises, Example as applicable
7. **Include example** - at least one for non-trivial public APIs
8. **Verify format** - check spacing, quote style, section order
9. **Keep it maintainable** - concise but complete

## Format Comparison Chart

| Aspect | Google | NumPy | Sphinx |
|--------|--------|-------|--------|
| Readability | High | Medium | Medium |
| Verbosity | Low | High | Medium |
| Scientific use | Good | Excellent | Good |
| Tool support | Excellent | Excellent | Excellent |
| Learning curve | Easy | Medium | Medium |
| Horizontal space | More | Less | Medium |
| Vertical space | Less | More | Medium |

## Example: Complete Module

```python
"""Utilities for data validation and transformation.

This module provides functions and classes for validating, cleaning,
and transforming structured data from various sources.

Classes:
    DataValidator: Validate data against schemas.
    DataTransformer: Transform data between formats.

Functions:
    validate_schema: Validate data against JSON schema.
    clean_data: Remove invalid entries from dataset.

Example:
    Basic usage::
    
        from data_utils import DataValidator
        
        validator = DataValidator(schema)
        if validator.validate(data):
            cleaned = clean_data(data)
"""

from typing import Any, Dict, List, Optional
import json

class DataValidator:
    """Validate data against defined schemas.
    
    Attributes:
        schema: JSON schema definition for validation.
        strict_mode: Whether to fail on first error.
    """
    
    def __init__(self, schema: Dict[str, Any], strict_mode: bool = True):
        """Initialize validator.
        
        Args:
            schema: JSON schema definition.
            strict_mode: Fail on first error if True. Defaults to True.
        """
        self.schema = schema
        self.strict_mode = strict_mode
    
    def validate(self, data: Dict[str, Any]) -> bool:
        """Validate data against schema.
        
        Args:
            data: Data to validate.
        
        Returns:
            True if valid, False otherwise.
        
        Raises:
            ValueError: If strict_mode is True and validation fails.
        """
        pass

def clean_data(data: List[Dict[str, Any]], remove_nulls: bool = True) -> List[Dict[str, Any]]:
    """Remove invalid entries from dataset.
    
    Args:
        data: List of data dictionaries to clean.
        remove_nulls: Remove entries with null values. Defaults to True.
    
    Returns:
        Cleaned dataset with invalid entries removed.
    
    Example:
        >>> data = [{'id': 1}, {'id': None}, {'id': 2}]
        >>> clean_data(data)
        [{'id': 1}, {'id': 2}]
    """
    pass
```

## Resources

- **PEP 8**: https://peps.python.org/pep-0008/
- **PEP 257**: https://peps.python.org/pep-0257/
- **PEP 484**: https://peps.python.org/pep-0484/
- **Google Style Guide**: https://google.github.io/styleguide/pyguide.html
- **NumPy Style**: https://numpydoc.readthedocs.io/en/latest/format.html
- **Sphinx**: https://www.sphinx-doc.org/

## Final Checklist

Before finalizing documentation:
- [ ] Summary line is one line, imperative mood, < 80 characters
- [ ] Multi-line docstrings have blank line after summary
- [ ] All public APIs are documented
- [ ] Type hints are present OR types in docstring
- [ ] Args/Parameters section lists all parameters
- [ ] Returns section describes return value
- [ ] Raises section lists possible exceptions
- [ ] At least one example for non-trivial functions
- [ ] Examples use doctest format when possible
- [ ] Consistent format used throughout project
- [ ] No redundant information (don't repeat type hints)
- [ ] Closing quotes on separate line (multi-line only)