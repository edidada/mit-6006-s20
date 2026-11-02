def satisfying_booking(R):
    """Return maximal constant-count intervals covering the half-open requests."""
    events = {}
    for start, end in R:
        if end < start:
            raise ValueError('A request cannot end before it starts')
        if end == start:
            continue
        events[start] = events.get(start, 0) + 1
        events[end] = events.get(end, 0) - 1
    result = []
    previous, active = None, 0
    for time, change in sorted(events.items()):
        if previous is not None and previous < time and active:
            if result and result[-1][0] == active and result[-1][2] == previous:
                result[-1] = (active, result[-1][1], time)
            else:
                result.append((active, previous, time))
        active += change
        previous = time
    return tuple(result)
