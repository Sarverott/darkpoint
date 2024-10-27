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

flag = True

if flag:
    print(
        "\n\n\t \33[7m                   ",
        "                 \33[0m",
        "\n\33[0m\t \33[7m █▀▄ ▄▀█ █▀█ █▄▀ █▀█ █▀█ █ █▄░█ ▀█▀ \33[0m",
        "\n\t \33[7m █▄▀ █▀█ █▀▄ █░█ █▀▀ █▄█ █ █░▀█ ░█░ \33[0m",
        "\n\t \33[7m                                    \33[0m\n",
        "\n\tDarkPoint   ",
        "Copyright (C) 2024  Sett Sarverott ",
        "<sett@sarverott.com> (https://sarverott.com)",
        "\n\tThis program comes with ABSOLUTELY NO WARRANTY;",
        ' for details read file "LICENSE".',
        "\n\tThis is free software, and you are welcome to redistribute it",
        "\n\tunder certain conditions of license GNU GPL v3.\n\n",
    )
    flag = False


def EXAMPLE_HEADER(example_name, description):
    print(
        "\33[31m\r       \n|",
        "\r\n|---------------------------------------------",
        f"\r\n|\t EXAMPLE: {example_name}  ",
        f"\r\n|\t --- {description}  \r\n\x1b[0m\r       ",
    )


def IS_PACKAGE_INSTALLED():
    print("\n|\n|--BEFORE LOUNCH CHECKUP begins")
    output = None

    try:
        print("trying to import DarkPoint from package library...")
        from darkpoint.Point import Point

        print("DarkPoint IMPORTED!")
        print("checking if content of package is not blank...")
        x = Point("dark void testing here", "DARKNESS - test scope")
        print(" X = new Point ")
        print(f"\tpoint X = '{x}'")
        print(f"\tcontext of X = '{x.context}'")

    except Exception as ISSUE:
        print("\33[41m")
        print("!!! ERROR !!!")
        print("\t", ISSUE)
        print("\t-TYPE: ", type(ISSUE))
        print("\t-ARGS:\n\t\t", "\n\t\t".join(ISSUE.args))
        print("~import-darkpoint~:: CHECKUP FAILS!")
        print("\33[0m")
        output = False

    else:
        print("\33[42m")
        print("CHECKUP PASSED!\t\33[0m")
        print("")
        output = True

    print("|--BEFORE LOUNCH CHECKUP ends\n|\n")
    return output
