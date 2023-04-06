# Tower of Honoi Solver
Programatically solve the Tower of Honoi child's puzzle.

I ran across the statement that the Tower of Honoi puzzle could be solved with a recursive algorithm while
reading a book.  I love puzzles and recursion is fun, so I skipped the solution and decided to try it for
myself.  Here is the result displayed to a text terminal.

#Usage:
<pre>
    tower-of-honoi [size] [q|Q]
        [size] and [q|Q] are optional parameters.
        size indicates the number of tiles in the puzzle
        q|Q  a case-insensitive letter q indicating to use quiet mode.  In quiet mode, the puzzle is solved
                and each step is output to the screen.  In default mode, the user is prompted for a key between
                each step in the solution.
</pre>

#Example:
<pre>
    tower-of-honoi 3

    will start with:
               ||          ||          ||
               ||          ||          ||
              ====         ||          ||
             ======        ||          ||
            ========       ||          ||

    and end with:
               ||          ||          ||
               ||          ||          ||
               ||          ||         ====
               ||          ||        ======
               ||          ||       ========
</pre>
