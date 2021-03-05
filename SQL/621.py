#621. Task Scheduler:
class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
  	frequencies = [0] * 26
  	for t in tasks:
  	  frequencies[ord(t) - ord("A")] += 1
  	  frequencies.sort()
  	  totalIdle = n * (fmax - 1)
  	  #each step, we are going to get the optimal interval with minimal number of idles.
  	  while frequencies and totalIdle > 0:
  	  	totalIdle -= min(fmax - 1, frequencies.pop())
  	  totalIdle = max(0, totalIdle)
  	  return totalIdle + len(tasks)


