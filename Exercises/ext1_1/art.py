# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    # SOLUTION - ADD RANGE
    # AS_IS - for r in rows:    
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))