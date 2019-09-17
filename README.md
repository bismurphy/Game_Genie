# Game_Genie
Set of python scripts to decode and encode game genie codes

As per: http://tuxnes.sourceforge.net/gamegenie.html

You can run the encode script to take a set of "address, data, [compare]", and turn it into a new Game Genie code. Alternatively,
you can take a Game Genie code and find out what it's doing under the hood.

Note that there is a fundamental ambiguity in Game Genie codes, in that the third character in the code's top bit doesn't do anything.
This means that, for any given desired effect, there will be two Game Genie codes. For example, "GOSSIP" and "GOISIP" do the exact same thing.

Thus the third letter can always be swapped to another particular letter. These pairs are:
A/E
P/O
Z/X
L/U
G/K
I/S
T/V
Y/N
So if your code has a K in the third spot, you can change it to Z. If it has a T, you can change it to V. It won't matter.

Happy to take any requests for changes. This is what I had set out to do though for myself.
