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
    
    EXAMPLE_HEADER(__name__, "showing context and changing it")

    print("\n### CONTEXT OF PALACE")
    print(f"\t PALACE: {palace}")
    print(f"\t CONTEXT: {palace.context}")

    print("\n### Changing context")
    print(f"\t method return value is SELF")
    print(f"\t   palace/'DARK_VOID' \n\t RETURNS \n\t  '{ palace/'DARK_VOID' }'")
    print(f"\tit's for optional involving it while chaining")
    print(f"\t CONTEXT of palace: {palace.context}")
