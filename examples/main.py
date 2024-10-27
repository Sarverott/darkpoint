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

# package installed checkup
from _helpers import IS_PACKAGE_INSTALLED

if not IS_PACKAGE_INSTALLED():
    print("try next time after installing package")
    print("\tSEE:")
    print("\t\t- dev/unix/install-local.sh")
    print("\t\t- dev/unix/install-public.sh")
    print("\t\t- dev\\dos\\install-local.bat")
    print("\t\t- dev\\dos\\install-public.bat")
    exit(1)

# intro

from darkpoint.Point import Point

palace = Point("darkness")

# all examples loading

from _1_quick_hooking import EXAMPLE as quick_hooking
from _2_hooking_path import EXAMPLE as hooking_path
from _3_printing import EXAMPLE as printing
from _4_print_hooks import EXAMPLE as print_hooks
from _5_for_loop_with_hooking_path import EXAMPLE as for_loop_with_hooking_path
from _6_hook_existing_points import EXAMPLE as hook_existing_points
from _7_absolute_path_traversal import EXAMPLE as absolute_path_traversal
from _8_chaining import EXAMPLE as chaining
from _9_context_change import EXAMPLE as context_change
from _10_multiple_context_change import EXAMPLE as multiple_context_change
#from _11_supreme_hooking import EXAMPLE
#from _12_filters import EXAMPLE

# example 1
quick_hooking( palace )

# example 2
hooking_path( palace )

# example 3
printing( palace )

# example 4
print_hooks( palace )

# example 5
for_loop_with_hooking_path( palace )

# example 6
hook_existing_points( palace )

# example 7
absolute_path_traversal( palace )

# example 8
chaining( palace )

# example 9
context_change( palace )

# example 10
multiple_context_change( palace )




