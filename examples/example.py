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

from ..src.darkpoint.Point import Point

# definition of palace

palace = Point("darkness")

# quick hooking of new information

palace["palace"]="THE PALACE for mind is common place to put enormous ammounts of threads, so having infinite space in there is nice"
palace["color"]="dark"
palace["templates"]="templates for repetitive constructs"
palace["hook"]="hooks are self-explanatory named reference to points with data mentioned by name"
palace["point"]="information that is also node for hooks to recognized points with informations that are associated with this one"
palace["info"]="data content of point"

# chaining data with quick hooking

palace["singular principles"]="this is main set of rules"

palace["singular principles"]["points are data"]="Each piece of information is represented as a point"
palace["singular principles"]["Points have hooks"]="most common are point that has a hook."
palace["singular principles"]["hooks are ended with points"]="The hooks lead to additional points, creating a chain of information."
palace["singular principles"]["points are related by hooking"]="Informations are related by hooking. The connections between points are established through hooks."
palace["singular principles"]["one direction of hook"]="Hooks are one-directional. The connections only go in one direction, leading from one point to another with evental resulting nature, not dimentional."
palace["singular principles"]["templates of points"]="Points can be extended by templates. This is for type of information grouping and categorization - for point, that are similar to each other thay can have obvious associations with other points or standard procedures - these can be added through templates."
palace["singular principles"]["starting point"]="Set starting point of each mindset. There is a designated starting point from which the connections begin that is easy to access by first thought about that topic."
palace["singular principles"]["idea of thought palace"]="For The PALACE there is special starting point. this is root placed in the middle of memories, every time after reset or starting, the point of focus lands here. For example my palace is: `dark void` and reset for me runs through simply thinking about `darkness`."






# printing
print("\n---------------------------------------------")
print("\tprinting")

print("#### DARKNESS")
print("\t",palace)
print("#### COLOR")
print("\t",palace["color"])
print("#### TEMPLATES ? ")
print("\t",palace["templates"])





# printing with for loop iterating
print("\n---------------------------------------------")
print("\t printing with for loop iterating")

print("### DARKNESS; What's in here?")
for hooked, info in palace:
    print(f"\t{hooked} --- {info}")






# grabing hook and printing with for loop iterating
print("\n---------------------------------------------")
print("\t grabing hook and printing with for loop iterating")

print("### singular principles ")
for hooked, info in palace["singular principles"]:
    print(f"\t{hooked} --- {info}")


# adding hooks to existing points
palace * "information" + palace["info"]
palace["hook"] * "point" + palace["point"]

# spaces are fluid thing
palace["singular principles"] *"THE PALACE" +palace
# for better readability i will play with spaced gaps
palace  *"palace"   +palace["singular principles"]["idea of thought palace"]
# this variant looks ok
palace    *"what is that"+palace["palace"]

# absolute path traversal 

print("\n---------------------------------------------")
print("\t hooking ant pathing")

print("### ABSOLUTE PATH TRAVERSAL")
palace["singular principles"]["THE PALACE"]["what is that"] *"example"+palace
print("\t\tcontent of palace['singular principles']['idea of thought palace']['example']:")
print(f"\t{palace['singular principles']['idea of thought palace']['example']}")
print("\t\tis it palace?")
print(f"\t{palace['singular principles']['idea of thought palace']['example']==palace}")





# chaining example
print("\n---------------------------------------------")
print("\t chaining example")
palace["void"]="void is emptyness, void is darkness, void is all that IS, void is default state of space"

# let's make some explaining presets for commentary before next example
# # # ~RULES~
# PALACE == darkness as root point
# [...label] == point's absolute path from PALACE 
# point->other_point == hooking
# ---arguments == reason why that is hooked

# in this inline chain are several hookings
print(
    palace   *"darkness"+palace["void"]    *"color"+palace["color"]    *"space"+palace["void"]     *"darkness"+palace
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
palace["void"]    *"space"+palace    *"space"+palace["void"]
# ["void", "space"]->PALACE ---void space is palace
# THEN
# ["space"]->["void"] ---space in palace is void


# context
print("\n---------------------------------------------")
print("\t context")
print("\n### CONTEXT OF PALACE")
print(f"\t PALACE: {palace}")
print(f"\t CONTEXT: {palace.context}")

print("\n### Changing context")
print(f"\t method return value is SELF")
print(f"\t   palace/'DARK_VOID' \n\t RETURNS \n\t  '{ palace/'DARK_VOID' }'")
print(f"\tit's for optional involving it while chaining")
print(f"\t CONTEXT of palace: {palace.context}")

print("\n---------------------------------------------")
print("\t recurrent methods")

print("### Changing context recursively")
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

#### supreme ultrahooking
#palace    **"THE PALACE"+palace 





#### filters
## grab first find in context
#palace    %{"/":"darkness"}*"space"+palace     
## grab all of context
#palace    %{"/":"darkness"}**"space"+palace  

