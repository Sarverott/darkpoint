#!/usr/bin/env python

# DarkPoint - technomantic framework for mnemonic toolkit that is in accordance with singular principles of thought model system
# Copyright (C) 2024   Sett Sarverott <sett@sarverott.com> (https://sarverott.com)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from _helpers import EXAMPLE_HEADER


def EXAMPLE(palace):

    EXAMPLE_HEADER(__name__, "adding hooks to existing points")

    # adding hooks to existing points
    palace * "information" + palace["info"]
    palace["hook"] * "point" + palace["point"]

    # spaces are fluid thing
    palace["singular principles"] * "THE PALACE" + palace
    # for better readability i will play with spaced gaps
    palace * "palace" + palace["singular principles"]["idea of thought palace"]
    # this variant looks ok
    palace * "what is that" + palace["palace"]
