class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count=[0]*26
        for task in tasks:
            task_count [ord(task) - ord('A')] +=1
        task_count.sort(reverse=True)
        max_count= task_count[0]-1
        idle_slots= max_count*n
        for i in range (1,len(task_count)):
            idle_slots -= min(task_count[i],max_count)
        idle_slots =max(0, idle_slots)
        return len(tasks)+ idle_slots
        