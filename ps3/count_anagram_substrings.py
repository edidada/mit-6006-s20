from collections import Counter


def count_anagram_substrings(T, S):
    """Count fixed-length anagram windows using a shared frequency index."""
    if not S:
        return ()
    length = len(S[0])
    if any(len(pattern) != length for pattern in S):
        raise ValueError('Pattern lengths must be equal')
    alphabet = sorted(set(T).union(*(set(pattern) for pattern in S)))
    indices = {character: index for index, character in enumerate(alphabet)}
    def signature(pattern):
        counts = [0] * len(alphabet)
        for character in pattern:
            counts[indices[character]] += 1
        return tuple(counts)
    frequencies = Counter()
    if length == 0:
        frequencies[signature('')] = len(T) + 1
    elif length <= len(T):
        counts = list(signature(T[:length]))
        frequencies[tuple(counts)] += 1
        for right in range(length, len(T)):
            counts[indices[T[right - length]]] -= 1
            counts[indices[T[right]]] += 1
            frequencies[tuple(counts)] += 1
    return tuple(frequencies[signature(pattern)] for pattern in S)
