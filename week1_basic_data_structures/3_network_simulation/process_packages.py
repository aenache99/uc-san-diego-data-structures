from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.end_times = deque()

    def process(self, request):
        current_time = request.arrived_at

        # Remove finished requests
        while self.end_times and self.end_times[0] <= current_time:
            self.end_times.popleft()

        if len(self.end_times) >= self.size:
            return Response(True, -1)

        if not self.end_times:
            start_time = current_time
        else:
            start_time = max(self.end_times[-1], current_time)

        end_time = start_time + request.time_to_process
        self.end_times.append(end_time)

        return Response(False, start_time)


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = [Request(*map(int, input().split())) for _ in range(n_requests)]

    buffer = Buffer(buffer_size)
    responses = []

    for request in requests:
        response = buffer.process(request)
        responses.append(response)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
