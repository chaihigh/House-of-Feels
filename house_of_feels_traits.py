from house_of_feels_classes import *

# -INDEX-

# -LIVING ROOM-
    # -FRONT_DOOR-
# -WEST HALLWAY-
    # -PHOTO-
# -BLACKWELL'S ROOM-
    # BLACKS_DESK-


# In the -LIVING ROOM-...

# -FRONT_DOOR- traits...
peephole = Trait("peephole", "It's a peephole.", "a ", " It has a peephole.")


# In the -WEST HALLWAY-...

# -PHOTO- traits...
tree = Trait("tree", "It's a honey locust.", "a ", " There's a tree on a hill,")
lake = Trait("lake", "Sunlight glistens on its surface.", "a ", " overlooking a lake.")
bird = Hidden_Trait("bird", "smudge", "It's a fox kestrel.", \
                    "You peer closer - it's a bird.", "a ", "a ", \
                    " You notice a smudge in the corner.", " There's a bird in the corner.")


# In -BLACKWELL'S ROOM-...

# -BLACKS_DESK- traits...
sticky_note = Trait("sticky note", "It has a grocery list written on it.", "a ", " A sticky note is stuck to the surface.")
smiley_face = Hidden_Trait("smiley face", "mark", "It's happy. And permanent.", "You look closer - it's a smiley face, drawn in permanent marker.", "a ", "a ", \
                           " There's a mark on the wood.", " There's a smiley face drawn on the wood.")
stain = Trait("stain", "It looks like it could be ink.", "a ", " There's a stain in the bottom.", False)
staple = Hidden_Trait("staple", "thing stuck in wood", "It's embedded in the wood.", "It seems to be a staple.", "a ", "a ", \
                      " You notice something stuck in the wood in the side of the drawer.", " There's a staple stuck in the side of the drawer.", False, False)
staple.is_external = False


trait_list = [peephole, tree, lake, bird, sticky_note, smiley_face, stain, staple]
