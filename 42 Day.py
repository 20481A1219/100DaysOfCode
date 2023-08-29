class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start=0
        total=0
        current=0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            current+=gas[i]-cost[i]
            if current<0:
                # upto that index there is no such point
                start=i+1
                current=0
        if total<0:
            return -1
        return start
