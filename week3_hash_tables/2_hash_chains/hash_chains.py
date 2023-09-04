class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.buckets = [[] for _ in range(bucket_count)]  # Use a list of lists (chaining)

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        bucket_idx = self._hash_func(query.s) if hasattr(query, 's') else query.ind
        bucket = self.buckets[bucket_idx]

        if query.type == "check":
            self.write_chain(bucket)  # Print the entire bucket, not reversed
        else:
            if query.type == 'find':
                self.write_search_result(query.s in bucket)
            elif query.type == 'add':
                if query.s not in bucket:
                    bucket.insert(0, query.s)  # Insert at the beginning
            else:
                # Remove all occurrences of the element from the bucket
                bucket[:] = [item for item in bucket if item != query.s]

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
