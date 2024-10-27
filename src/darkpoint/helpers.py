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


default_hard_chars_replacing = [
    ["\n","\\n"],
    ["\'","\\'"],
    ["\"","\\\""],
    ["\b","\\b"],
    ["\0","\\0"],
    ["\t","\\t"],
    ["\r","\\r"],
    ["\\","\\\\"]
]

def soft_string(input_str, hard_char_replacing = default_hard_chars_replacing):
    output_str = None # better return nothing to indicade error

    for replacement in hard_char_replacing:
         
         if output_str is None:
              output_str = input_str

         output_str = output_str.replace(replacement[0],replacement[1])
    
    return output_str
         
