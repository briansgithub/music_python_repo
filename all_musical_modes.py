diatonics = {
        "c": 0,
        "d": 2,
        "e": 4,
        "f": 5,
        "g": 7,
        "a": 9,
        "b": 11
        }

diatonic_ring = ['c', 'd', 'e', 'f', 'g', 'a', 'b']

offsets = {
        "lydian":       [0, 2, 4, 6, 7, 9, 11],
        "ionian":       [0, 2, 4, 5, 7, 9, 11],
        "major":        [0, 2, 4, 5, 7, 9, 11],
        "mixolydian":   [0, 2, 4, 5, 7, 9, 10],
        "dorian":       [0, 2, 3, 5, 7, 9, 10],
        "aeolian":      [0, 2, 3, 5, 7, 8, 10],
        "minor":        [0, 2, 3, 5, 7, 8, 10],
        "phrygian":     [0, 1, 3, 5, 7, 8, 10],
        "locrian":      [0, 1, 3, 5, 6, 8, 10],
        }

def main(): 

    scale_pretty = ["", "", "", "", "", "", ""]

    root = input("Enter a root: ").lower()
    if root[0] not in diatonics:
        print("\tInvalid Root, please choose from:\n",
                "\t", list(diatonics.keys()), "(trailing '#' or 'b' chars ok)"
                )
        return

    mode = input("Enter a mode: ").lower()
    if mode not in list(offsets.keys()):
        print("\tInvalid mode, please choose from:\n",
                "\t", offsets.keys()
                )
        return
    num_accidentals = root[1:].count('#') - root[1:].count('b')

    scale = scale_generator(root, mode)
    print(scale)



    return

def scale_generator(root, mode):
    scale = [0, 0, 0, 0, 0, 0, 0]
    root = note_to_num(root)
    #convert root note to integer
    #apply scale steps
    scale = [root + offsets.get(mode)[degree] for degree in range(len(scale))]
    #perform modulo on each scale degree 
    scale = [degree % 12 for degree in scale]
    #convert list of scale degrees back to notes
    #(if root is -7 to -1, then map to flats and double flats)
    #(if root is 0 to +7, then map to sharps and double sharps)
    return scale

def note_to_num(note_name):
    note_letter = note_name[0]
    accidentals = note_name[1:]
    num_accidentals = accidentals.count('#') - accidentals.count('b')

    return (diatonics[note_letter] + num_accidentals) % 12

#you need a root and a mode in order to infer the proper role of the note in the context in which it is being played
def num_to_note(note_num, root, mode):
    scale = scale_generator(root, mode)
    num_accidentals = 0
    note_letter = diatonic_ring[0]
    None

#list the diatonic note letters in the proper order, starting on the root label
#map the diatonic note labels to their numbers
#if there are accidentals on the root, apply them to the note numbers
#
#find the note in the original scale 

main()
