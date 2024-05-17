"""Cookiecutter hook for pre project generation."""

from __future__ import annotations

import re
from typing import Pattern

# A valid name consists only of ASCII letters 
# and numbers, period, underscore and hyphen. 
# It must start and end with a letter or number.
# https://packaging.python.org/en/latest/specifications/name-normalization/ 
VALID_PROJECT_NAME: Pattern[str] = re.compile(
    r"^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$", re.IGNORECASE
)

# Package names must be lower-case letters,
# numbers, or dashes, but not start with a dash.
# The regex is from PEP508: https://peps.python.org/pep-0508/#names
# And, without allowing periods or underscores,
# as reflected in packaging name normalization:
# https://peps.python.org/pep-0503/#normalized-names.
VALID_PACKAGE_NAME: Pattern[str] = re.compile(r"^([a-z0-9]|[a-z0-9][a-z0-9-]*[a-z0-9])$")


# Checks repository url, assuming it is at GitHub.
VALID_REPO_URL: Pattern[str] = re.compile(
    r"^https:\/\/github\.com\/[A-Za-z0-9]([A-Za-z0-9_]|-(?!-))*[A-Za-z0-9_]"
    r"\/[A-Za-z0-9_]([A-Za-z0-9_]|-(?!-))*[A-Za-z0-9_]\/?$"
)


def validate_text(text: str, regex: Pattern[str], error_label: str) -> None:
    """Ensures that `text` is valid.

    Args:
        text: value to check.
        regex: regular expression to check "text" against.
        error_label: text to add to error message if the check fails.

    Raises:
        ValueError: if "text" does not match "regex".
    """
    if not text or regex.fullmatch(text) is None:
        message = f"Input <{text}> is not a valid {error_label}"
        raise ValueError(message)


def main() -> None:
    """Calls validation functions."""
    validate_text(
        text="{{ cookiecutter.project_name }}",
        regex=VALID_PROJECT_NAME,
        error_label="project name",
    )
    
    validate_text(
        text="{{ cookiecutter.package_name }}",
        regex=VALID_PACKAGE_NAME,
        error_label="python package name",
    )

    validate_text(
        text="{{ cookiecutter.github_url }}",
        regex=VALID_REPO_URL,
        error_label="github repository url",
    )


if __name__ == "__main__":
    main()
