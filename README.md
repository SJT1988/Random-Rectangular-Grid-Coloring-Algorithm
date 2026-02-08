# Random-Rectangular-Grid-Coloring-Algorithm
Python console proof-of-concept that randomly "colors" tiles of a rectangular grid such that adjacent tiles do not have the same color, whenever possible.

Suppose you have an M x N rectangular grid and X colors.

  - If X < 4, the tiles of the grid will be colored randomly.
  - If X = 4, the tiles of the grid will be colored randomly such that no same-colored tiles share an edge.
  - If X >= 4, the tiles of the grid will be colored randomly such that no same-colored tiles share a corner.

What the program actually does is print a rectangular array of the first X characters randomly selected from the alphabet such that the above conditions are met. Examples below:

```text
Enter number of colors: 3
Enter grid size M,N:    5,5
B C A A A 
B A B B C
C B A B C
A B C A A
C A A A A
```

```text
Enter number of colors: 4
Enter grid size M,N:    5,5
A B D B C 
D C B C D 
C D C D B 
B A D C A 
D B C D C
```

```text
Enter number of colors: 5
Enter grid size M,N:    5,5
D C A D A 
A E B E C
D C D A B
B E B E C
D C A D A
```

```text
Enter number of colors: 5
Enter grid size M,N:    11,9
E B E A D B D B A 
D C D B C A C E D
E B A E D E B A B
A D C B C A D C E
C E A E D E B A D
A D C B A C D E B
E B A D E B A C D
A D E C A C D B A
B C A D E B A C E
E D E C A D E D B
C B A D B C A C A
```

```text
Enter number of colors: 7
Enter grid size M,N:    13,14
E F B E F E F A G D G F D A 
G A G A B A B E C A E C B C
F E D E C E C A D F B D E G
C B F B D B F B E C G A B C
F G E G F C A G D A B C D G
A B C B D B D E F E F G B E
E D A G F C F C A B A C A D
A C B E D B D G F G E B F C
B D A F C G C E B C D C D A
C G B D B D A D G F E F E F
A E F A F G C E A D B C B D
C B D E C B D G B E F E G C
F A F B G A F C F G D A B F
```

I wrote this to help me solve a problem in 3D modeling, computer animation, and game design where I may want to distribute random materials or objects over a rectangular grid.
You are welcome to use my program as-is or modify it into your own solution provided you credit me as a source.
