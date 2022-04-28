# oldmac.py 
# This program will use functions and module definitions for
# the nursy rhyme for Old MacDonald.

def animal(name, sound):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a " + name + "Ee-igh, Ee-igh, Oh!")
    print("With a " + sound + "," + sound + " here and a " + sound + "," + sound + " there.")
    print("Here a " + sound + ", there a " + sound + ", everywhere a " + sound + sound + ".")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
def main():
    animal("cow", "moo")
    animal("horse", "neigh")
    animal("dog", "woof")
main()