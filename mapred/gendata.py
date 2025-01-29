from typing import Iterable

from faker import Faker

if __name__ =="__main__":
    fake = Faker()
    
    for i in range(100):
        with open(f"dfs/text_file_{i}.txt", "w") as fp:
            for sent in fake.sentences():
                print(sent, file=fp)

    