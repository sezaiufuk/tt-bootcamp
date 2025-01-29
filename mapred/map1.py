from pathlib import Path
from random import choice

MAP_COUNT=5

def line_generator():
    for file in Path("dfs").glob("text_file*.txt"):
        with file.open() as fp:
            for line in fp:
                yield line.strip()
                
def wc_map(line_iter):
    directory = Path("dfs")/"map0"
    
    directory.mkdir(exist_ok=True,parents=True)
    
    fps = [(directory/f"map_{i}").open("w") for i in range(MAP_COUNT)]
    
    for line in line_iter:
        fp = choice(fps)
        
        for word in line.split():
            print(f"{word.lower().strip('.,')},1",file=fp)
                
if __name__ == "__main__":
    wc_map(line_generator())
    