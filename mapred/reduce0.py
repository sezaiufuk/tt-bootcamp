from collections import Counter, defaultdict
from pathlib import Path
from random import choice

REDUCER_COUNT=3

def line_generator():
    for file in Path("dfs").glob("text_file*.txt"):
        with file.open() as fp:
            for line in fp:
                yield line.strip()
                
def wc_reduce():
    for i, file in enumerate(Path("dfs/shuffle0").glob("shuffle*")):
        
        print(f"# Reducer {i}")
        with file.open() as fp:
            current_key = None
            current_sum = 0
            for line in fp:
                key, value = line.split(',')
                
                if key != current_key:                    
                    if current_key is not None:
                        print(f"{current_key},{current_sum}")
                        
                    current_sum = int(value)
                    current_key = key 

                else:
                    current_sum += int(value)
                    
            print(f"{current_key},{current_sum}")
            
def wc_reduce2():
    
    counter = defaultdict(int)
    for i, file in enumerate(Path("dfs/shuffle0").glob("shuffle*")):
        
        print(f"# Reducer {i}")
        with file.open() as fp:
            for line in fp:
                key, value = line.split(',')
                
                counter[key] += int(value)
                
            for k,v in counter.items():
                print(k,v)
                
def wc_reduce3():
    
    counter = Counter()
    for i, file in enumerate(Path("dfs/shuffle0").glob("shuffle*")):
        
        print(f"# Reducer {i}")
        with file.open() as fp:
            for line in fp:
                key, value = line.split(',')
                
                counter[key] += int(value)
                
                counter.add(key, int(value))
                
            for k,v in counter.items():
                print(k,v)                  
                 
if __name__ == "__main__":
    wc_reduce()
    