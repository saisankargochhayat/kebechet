#!/usr/bin/env python3
# Kebechet
# Copyright(C) 2020 Sai Sankar Gochhayat
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Body of issues and pull requests automatically opened."""

RELEASE_TAG_MISSING_WARNING = """
---
**WARNING NOTE**
The release version mentioned in the source-code couldn't be found in git tags, \
    hence the release is created from the start.
If that is not the right behavior:

- Close this pull request & release issue.
- Fix the version string in source-code to reflect the latest git-tag, or create \
    the missing tag pointing to the last release sha.
- Create a new release issue.
---
"""
