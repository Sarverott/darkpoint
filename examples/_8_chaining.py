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

    EXAMPLE_HEADER(__name__, "couple chaining examples")

    # chaining example
    palace["void"] = (
        "void is emptyness, void is darkness, void is all that IS, void is default state of space"
    )

    # let's make some explaining presets for commentary before next example
    # # # ~RULES~
    # PALACE == darkness as root point
    # [...label] == point's absolute path from PALACE
    # point->other_point == hooking
    # ---arguments == reason why that is hooked

    # in this inline chain are several hookings
    print(
        palace * "darkness"
        + palace["void"] * "color"
        + palace["color"] * "space"
        + palace["void"] * "darkness"
        + palace
    )
    # ["darkness"]->["void"] ---darkness is void
    # THEN
    # ["void"]->["color"] ---void is dark
    # THEN
    # ["color", "space"]->["void"] ---dark space is void
    # THEN
    # ["void", "darkness"]->PALACE ---void is darkness

    # ...and prints out data in last attached node in chain as latest result on top

    # another inline hooking that fills some gaps in fallback nett around root of palace
    palace["void"] * "space" + palace * "space" + palace["void"]
    # ["void", "space"]->PALACE ---void space is palace
    # THEN
    # ["space"]->["void"] ---space in palace is void
