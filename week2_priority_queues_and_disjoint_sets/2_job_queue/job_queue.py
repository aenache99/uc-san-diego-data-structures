import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [(0, worker) for worker in range(n_workers)]
    heapq.heapify(next_free_time)

    for job in jobs:
        start_time, worker = heapq.heappop(next_free_time)
        result.append(AssignedJob(worker, start_time))
        heapq.heappush(next_free_time, (start_time + job, worker))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
