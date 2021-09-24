From the event: https://ctftime.org/event/854/tasks/

So to start of the challenge we take a look at the instructions page and
see the definitions for this random secret gate of theirs.

<img src="/2019/ALLESCTF/tex/166ec9a8fa1d0703dd6161f0c1fabafb.svg?invert_in_darkmode&sanitize=true" align=middle width=163.18329224999997pt height=24.65753399999998pt/>

<img src="/2019/ALLESCTF/tex/9e8514ae528c0c828aea8603bce5e0a1.svg?invert_in_darkmode&sanitize=true" align=middle width=133.61367855pt height=24.65753399999998pt/>

Since I have worked we these kinds of gates before I see that the definitions
closely resemble that of the gate used for a Deutsch algorithm.
This is a algorithm that is used to minimize function calls to tell
whether a function is balanced or constant. The algorithm uses a auxiliary
qubit which is our second qubit in the <img src="/2019/ALLESCTF/tex/ec2376fb49efb4243a3f5d76fe720bbb.svg?invert_in_darkmode&sanitize=true" align=middle width=19.178149649999988pt height=24.65753399999998pt/> state. Both qubits are then brought
into superposition using two hadamards and the unitary gate <img src="/2019/ALLESCTF/tex/f30c6bdebe1ddebdec6bb56fee7a3364.svg?invert_in_darkmode&sanitize=true" align=middle width=17.68118549999999pt height=22.465723500000017pt/> is applied across the two
qubits. The first qubit is then brought back to a single state using another hadamard.
In the case of Deutsch reading the first qubit then gives us the function calls
<img src="/2019/ALLESCTF/tex/31a6bef948c533616d360da71a62ac2a.svg?invert_in_darkmode&sanitize=true" align=middle width=92.69424285pt height=24.65753399999998pt/> which is completely equal to <img src="/2019/ALLESCTF/tex/c73b6615f0c7bd519371e439b4efff6d.svg?invert_in_darkmode&sanitize=true" align=middle width=30.05337719999999pt height=24.65753399999998pt/>.

Thus xor'ing these two possible function calls is given by

<img src="/2019/ALLESCTF/tex/70c04e97552b8950725615a8c02fc4b8.svg?invert_in_darkmode&sanitize=true" align=middle width=206.59578059999996pt height=24.65753399999998pt/>

<img src="/2019/ALLESCTF/tex/0fd22aefb18e071e1162d7d79754c301.svg?invert_in_darkmode&sanitize=true" align=middle width=166.08222179999999pt height=24.65753399999998pt/>

Where the first term will always be zero thus

<img src="/2019/ALLESCTF/tex/95397cbaab58b38a581647f951865244.svg?invert_in_darkmode&sanitize=true" align=middle width=80.75801414999998pt height=24.65753399999998pt/>

So depending on the outcome of the first qubit we can find <img src="/2019/ALLESCTF/tex/4fa3ac8fe93c68be3fe7ab53bdeb2efa.svg?invert_in_darkmode&sanitize=true" align=middle width=12.35637809999999pt height=14.15524440000002pt/>. If the outcome is
0 then <img src="/2019/ALLESCTF/tex/4fa3ac8fe93c68be3fe7ab53bdeb2efa.svg?invert_in_darkmode&sanitize=true" align=middle width=12.35637809999999pt height=14.15524440000002pt/> is also 0 and the same for the outcome of 1.

Now the trouble was that we are only given a specific <img src="/2019/ALLESCTF/tex/4fa3ac8fe93c68be3fe7ab53bdeb2efa.svg?invert_in_darkmode&sanitize=true" align=middle width=12.35637809999999pt height=14.15524440000002pt/> and we would really like all of <img src="/2019/ALLESCTF/tex/6f9bad7347b91ceebebd3ad7e6f6f2d1.svg?invert_in_darkmode&sanitize=true" align=middle width=7.7054801999999905pt height=14.15524440000002pt/>.
This part is probably obvious to most but it took me a while to figure out. I discovered after
using Chrome's dev tools and looking around for a bit, that we get one cookie named "randomness"
which is set to a specific numeric value. I figured that this is probably used to set the value
for <img src="/2019/ALLESCTF/tex/4fa3ac8fe93c68be3fe7ab53bdeb2efa.svg?invert_in_darkmode&sanitize=true" align=middle width=12.35637809999999pt height=14.15524440000002pt/>. So I wrote up a script in python (Babyquantum.py in rep) using selenium passed the circuit from Deutsch as

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
