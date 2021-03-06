#811.py
class Solution:
  def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
    result = collections.Counter()
    for dom in cpdomains:
      cur_count, domain = dom.split()
      cur_count = int(cur_count)
      fract = domain.split('.')
      for i in range(len(fract)):
      	result['.'.join(fract[i:])] += cur_count
    return ["{}{}".format(c1, c2) for c2, c1 in result.items()]




