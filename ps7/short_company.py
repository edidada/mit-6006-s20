def short_company(C, P, n, k):
    '''
    Input:  C | Tuple of s = |C| strings representing names of companies
            P | Tuple of s lists each of size nk representing prices
            n | Number of days of price information
            k | Number of prices in one day
    Output: c | Name of a company with highest shorting value
            S | List containing a longest subsequence of 
              | decreasing prices from c that doesn't skip days
    '''
    c, S = C[0], []
    for company, prices in zip(C, P):
        length = [1] * len(prices)
        parent = [-1] * len(prices)
        for i, price in enumerate(prices):
            # The predecessor must be today or yesterday: jumping over an
            # entire day violates the constraint even if prices decrease.
            first = max(0, (i // k - 1) * k)
            for j in range(first, i):
                if prices[j] > price and length[j] + 1 > length[i]:
                    length[i], parent[i] = length[j] + 1, j
        if not prices:
            continue
        end = max(range(len(prices)), key=length.__getitem__)
        if length[end] > len(S):
            chain = []
            while end != -1:
                chain.append(prices[end])
                end = parent[end]
            c, S = company, chain[::-1]
    return c, S
