#!/usr/bin/env python

    # DarkPoint - technomantic framework for mnemonic toolkit that is in accordance with singular principles of thought model system 
    # Copyright (C) 2024 Sett Sarverott (https://sarverott.com/) <sarverott@gmail.com>

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
    
    EXAMPLE_HEADER(__name__, "Changing context recursively")

    print(f"\n\t CONTEXT of palace:")
    print(f"\t    {palace.context}")
    print(f"\t hooks of palace with contexts")
    for hooked, info in palace:
        print(f"\t\t{hooked}/CONTEXT=\t\t{info.context}")
    print(f"\n\t Context change recursively in void")
    print(f"\t   palace['void']//'###_SPACE_DARKNESS_VOID_PALACE_###' \n\t RETURNS \n\t   '{ palace['void']//'###_SPACE_DARKNESS_VOID_PALACE_###' }'")
    print(f"\n\t CONTEXT of palace:")
    print(f"\t    {palace.context}")
    print(f"\t hooks of palace with contexts")
    for hooked, info in palace:
        print(f"\t\t{hooked}/CONTEXT=\t\t{info.context}")
    print(f"\t recurrent changes stops when iterated item's context is other then context of startpoint ")
    print(f"\t all previously related by hook chain from palace['void'] should have diffrent context, besides palace that had changed context before")

