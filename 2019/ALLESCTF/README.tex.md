So to start of the challenge we take a look at the instructions page and
see the definitions for this random secret gate of theirs.

$U_{r}|x,y\rangle=|x,y \oplus r(x)\rangle$

$r(x)=q \oplus\left(x \wedge s_{i}\right)$

Since I have worked we these kinds of gates before I see that the definitions
closely resemble that of the gate used for a Deutsch algorithm.
This is a algorithm that is used to minimize function calls to tell
whether a function is balanced or constant. The algorithm uses a auxiliary
qubit which is our second qubit in the $|1\rangle$ state. Both qubits are then brought
into superposition using two hadamards and the unitary gate $U_r$ is applied across the two
qubits. The first qubit is then brought back to a single state using another hadamard.
In the case of Deutsch reading the first qubit then gives us the function calls
$|f(0) \oplus f(1)\rangle$ which is completely equal to $r(x)$.

Thus xor'ing these two possible function calls is given by

$\left(q \oplus\left(0 \wedge s_{i}\right)\right) \oplus \left(q \oplus\left(1 \wedge s_{i}\right)\right)$

$\left(0 \oplus\left(0 \wedge s_{i}\right)\right) \oplus \left(1 \wedge s_{i}\right)$

Where the first term will always be zero thus

$0 \oplus \left(1 \wedge s_{i}\right)$

So depending on the outcome of the first qubit we can find $s_i$. If the out come is
0 $s_i$ and same for the outcome of 1.

Now the trouble was that we are only given a specific $s_i$ and we would really like all of $s$.
This part is probably obvious to most but it took me a while to figure out. I discovered after
using Chrome's dev tools and looking around for a bit, that we get one cookie named "randomness"
which is set to a specific numeric value. I figured that this is probably used to set the value
for $s_i$. So I wrote up a script in python (Babyquantum.py in rep) using selenium passed the circuit from Deutsch as

\- H U1 H D

X H U2 H D

and went through the values 0-200 for the cookie, reading the output of the first qubit.
this gave me a binary.

10000010 00110010 00110010 10100010 11001010 11011110
11001110 11000110 00010110 01001110 11110110 10100110
00100110 10010110 01110110 11100110 10100110 01001110
11001110 11111010 01000110 10000110 01000110 10011110
10111110

Which again I looked at for quite a while not able to make sense of it.
I finally figured that since nothing else was given the flag probably had
ALLES in the start, which almost fit with what I had, Mathing up the letters
I realized that the binary string was flipped. Thus after flipping and converting
to ascii I got a flipped string which I again flipped giving the flag

ALLES{schroedingers_baby}
