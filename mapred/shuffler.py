from pathlib import Path
from random import choice

REDUCER_COUNT=3
                
def shuffle(map_files, k=1):
    directory = Path("dfs")/"shuffle0"
    
    directory.mkdir(exist_ok=True,parents=True)
    
    fps = [(directory/f"shuffle_{i}").open("w") for i in range(REDUCER_COUNT)]
    
  
    for file in map_files:
        print(file)
        with file.open() as rp:
            for line in rp:
                key = tuple(line.split(',')[:k]) 
                print(line.strip(), file=fps[hash(key)%REDUCER_COUNT])
            
if __name__ == "__main__":
    shuffle(Path("dfs/map0").glob("map*"))
    