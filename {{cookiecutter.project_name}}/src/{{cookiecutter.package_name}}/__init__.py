# Copyright (c) {{ cookiecutter.package_year }} - {{ cookiecutter.author_name }}
# See end of file for extended copyright information
"""{{ cookiecutter.package_name|capitalize() }} package.

{{ cookiecutter.package_description }}
"""
import logging

try:
    from . import _version
    __version__ = _version.__version__
except ImportError:
    pass
else:
    __version__ =  "{{ cookiecutter.version }}"


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


# Copyright (c) 2023 - {{ cookiecutter.author_name }}
# This file is part of {{ cookiecutter.project_name }}.
#
# Lyndows is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# Lyndows is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Lyndows. If not, see <https://www.gnu.org/licenses/>
