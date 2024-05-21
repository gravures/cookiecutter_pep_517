"""Local Jinja2 extensions module."""

from __future__ import annotations

from typing import TYPE_CHECKING

from jinja2.ext import Extension


if TYPE_CHECKING:
    from jinja2.environment import Environment


LICENSES = {
    "Apache-2.0": "License :: OSI Approved :: Apache Software License",
    "BSD-2-Clause": "License :: OSI Approved :: BSD License",
    "GPL-3.0-only": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "GPL-3.0-or-later": "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    "MIT": "License :: OSI Approved :: MIT License",
}

STATUS = {
    "Alpha": "Development Status :: 3 - Alpha",
    "Beta": "Development Status :: 4 - Beta",
    "Stable": "Development Status :: 5 - Production/Stable",
    "Inactive": "Development Status :: 7 - Inactive",
}

OS = {
    "Any": "Operating System :: OS Independent",
    "Win": "Operating System :: Microsoft :: Windows",
    "OSX": "Operating System :: MacOS :: MacOS X",
    "Linux": "Operating System :: POSIX :: Linux",
    "Win/OSX": ("Operating System :: Microsoft :: Windows\"\n  \"Operating System :: MacOS :: MacOS X"),
    "Win/Linux": ("Operating System :: Microsoft :: Windows\"\n  \"Operating System :: POSIX :: Linux"),
    "OSX/Linux": ("Operating System :: MacOS :: MacOS X\"\n  \"Operating System :: POSIX :: Linux"),
}


class TroverClassifierExtension(Extension):
    """Jinja2 extension."""

    def __init__(self, environment: Environment) -> None:
        """Initialize the extension with the given environment."""
        super().__init__(environment)

        def licences_classifier(value: str) -> str:
            """Return a trover license classifier given an SPDX epression."""
            return LICENSES.get(value, "License :: OSI Approved")

        def dev_status_classifier(value: str) -> str:
            """Return a trover status classifier given an status string."""
            return STATUS.get(value, STATUS["Alpha"])

        def os_classifier(value: str) -> str:
            """Return trover os classifier(s) given a os string."""
            return OS.get(value, OS["Any"])

        environment.filters["licences_classifier"] = licences_classifier
        environment.filters["dev_status_classifier"] = dev_status_classifier
        environment.filters["os_classifier"] = os_classifier
