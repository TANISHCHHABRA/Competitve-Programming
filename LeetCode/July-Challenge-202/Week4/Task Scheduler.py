class Solution:
    def leastInterval(self, tasks: 'List[str]', n: 'int') -> 'int':
        
        counts = collections.Counter(tasks)
        counts = list(counts.values())
        res = (n+1)*(max(counts)-1)+counts.count(max(counts))
        return max(res,len(tasks))
