A program to test how long it takes to break a given password with lookup tables and brute force.
1) Checks the most common passwords worldwide and in Finland, as well as names and surnames.
2) Checks all combinations of digits.
3) Checks all combinations of digits and extended ASCII characters.

The used lookup tables can be found at:
- https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials (most common passwords)
- https://wiki.skullsecurity.org/index.php/Passwords (Finnish passwords)
- https://github.com/zeraye/names-surnames-list (names)
- https://github.com/dwyl/english-words (English words)
- https://github.com/hugovk/everyfinnishword (Finnish words)

&nbsp;
Of course, you may also choose to use different files or omit this step entirely.

&nbsp;

<sub>Probably not very efficient to use Python for this in actual practise, though.</sub>
