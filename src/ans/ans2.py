def merge_intervals(intervals):
    if len(intervals) == 0:
        return []
    
    intervals.sort(key=lambda x:x[0])
    
    results = [intervals[0]]
    
    for interval in intervals:
        if interval[0] <= results[-1][1]:
            results[-1] = (results[-1][0], max(interval[1], results[-1][1]))
        else:
            results.append(interval)
    return results