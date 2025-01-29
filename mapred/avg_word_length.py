from pathlib import Path
from random import choice

MAP_COUNT = 5
REDUCER_COUNT = 3


def line_generator():
    for file in Path("dfs").glob("text_file*.txt"):
        with file.open() as fp:
            for line in fp:
                yield line.strip()


class AvgWordLengthPhase1:
    def __init__(self, line_iter, reduce_key_count=1, identifier: int = 0) -> None:
        self.line_iter = line_iter
        self.map_dir = Path("dfs") / f"map{identifier}"
        self.shuffle_dir = Path("dfs") / f"shuffle{identifier}"
        self.reduce_dir = Path("dfs") / f"reduce{identifier}"

        self.k = reduce_key_count

        self.map_dir.mkdir(exist_ok=True, parents=True)
        self.shuffle_dir.mkdir(exist_ok=True, parents=True)
        self.reduce_dir.mkdir(exist_ok=True, parents=True)

    def map_writer(self):
        fps = [(self.map_dir / f"map_{i}").open("w") for i in range(MAP_COUNT)]

        for line in self.line_iter:
            fp = choice(fps)

            for tup in self.map(line):
                print(",".join([str(p) for p in list(tup)]), file=fp)

        for fp in fps:
            fp.close()

    def map(self, line: str):
        # User implemention required
        for word in line.split():
            yield word.lower().strip(".,"), len(word.lower().strip(".,")), 1

    def reduce(self):
        # User implemention required
        for i, file in enumerate(self.shuffle_dir.glob("shuffle*")):
            with file.open() as fp:
                current_key = None
                current_count = 0
                current_sum = 0
                for line in fp:
                    key, length, one = line.split(",")
                    key, length, one = key, int(length), int(one)

                    if key != current_key:
                        if current_key is not None:
                            yield current_key, current_sum, current_count, i

                        current_sum = length
                        current_count = one
                        current_key = key

                    else:
                        current_sum += length
                        current_count += one

                yield current_key, current_sum, current_count, i

    def shuffle_writer(self, inplace_sort: bool = True):
        lines_list = [[] for _ in range(REDUCER_COUNT)]

        for file in [(self.map_dir / f"map_{i}") for i in range(MAP_COUNT)]:
            with file.open() as rp:
                for line in rp:
                    tup = tuple(line.split(","))
                    key = tup[: self.k]

                    lines_list[hash(key) % REDUCER_COUNT].append(tup)

        for i in range(REDUCER_COUNT):
            with (self.shuffle_dir / f"shuffle_{i}").open("w") as wp:
                for tup in sorted(lines_list[i], key=lambda x: x[: self.k]):
                    print(",".join([str(p).strip() for p in list(tup)]), file=wp)

    def reduce_writer(self):
        fps = [
            (self.reduce_dir / f"reduce_{i}").open("w") for i in range(REDUCER_COUNT)
        ]

        for line in self.reduce():
            *tup, reducer_id = line

            print(",".join([str(p) for p in list(tup)]), file=fps[reducer_id])

        for fp in fps:
            fp.close()

    def run(self):
        self.map_writer()
        self.shuffle_writer()
        self.reduce_writer()
        
class AvgWordLengthPhase2:
    def __init__(self, line_iter, reduce_key_count=1, identifier: int = 0) -> None:
        self.line_iter = line_iter
        self.map_dir = Path("dfs") / f"map{identifier}"
        self.shuffle_dir = Path("dfs") / f"shuffle{identifier}"
        self.reduce_dir = Path("dfs") / f"reduce{identifier}"

        self.k = reduce_key_count

        self.map_dir.mkdir(exist_ok=True, parents=True)
        self.shuffle_dir.mkdir(exist_ok=True, parents=True)
        self.reduce_dir.mkdir(exist_ok=True, parents=True)

    def map_writer(self):
        fps = [(self.map_dir / f"map_{i}").open("w") for i in range(MAP_COUNT)]

        for line in self.line_iter:
            fp = choice(fps)

            for tup in self.map(line):
                print(",".join([str(p) for p in list(tup)]), file=fp)

        for fp in fps:
            fp.close()

    def map(self, line: str):
        # User implemention required
        yield "x", line

    def reduce(self):
        # User implementation required
        for i, file in enumerate(self.shuffle_dir.glob("shuffle*")):
            with file.open() as fp:
                current_count = 0
                current_sum = 0
                for line in fp:
                    _, _, length, count = line.split(",")
                    length, count = int(length), int(count)
                    
                    current_count += count
                    current_sum += length
                
                if current_count !=0:
                    yield current_sum/current_count, i

                    
    def shuffle_writer(self, inplace_sort: bool = True):
        lines_list = [[] for _ in range(REDUCER_COUNT)]

        for file in [(self.map_dir / f"map_{i}") for i in range(MAP_COUNT)]:
            with file.open() as rp:
                for line in rp:
                    tup = tuple(line.split(","))
                    key = tup[: self.k]

                    lines_list[hash(key) % REDUCER_COUNT].append(tup)

        for i in range(REDUCER_COUNT):
            with (self.shuffle_dir / f"shuffle_{i}").open("w") as wp:
                for tup in sorted(lines_list[i], key=lambda x: x[: self.k]):
                    print(",".join([str(p).strip() for p in list(tup)]), file=wp)

    def reduce_writer(self):
        fps = [
            (self.reduce_dir / f"reduce_{i}").open("w") for i in range(REDUCER_COUNT)
        ]

        for line in self.reduce():
            *tup, reducer_id = line

            print(",".join([str(p) for p in list(tup)]), file=fps[reducer_id])

        for fp in fps:
            fp.close()

    def run(self):
        self.map_writer()
        self.shuffle_writer()
        self.reduce_writer()        


if __name__ == "__main__":
    def reduce_iter():
        for p in Path("dfs/reduce9").glob("reduce*"):
            with p.open() as fp:
                for line in fp:
                    yield line.strip()
                    
    p1 = AvgWordLengthPhase1(line_generator(), identifier=9)
    p2 = AvgWordLengthPhase2(reduce_iter(), identifier=10)

    p1.run()
    p2.run()
