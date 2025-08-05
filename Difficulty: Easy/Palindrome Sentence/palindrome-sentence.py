import re
class Solution:
	def isPalinSent(self, s):
		# code here
		s=s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        return s==s[::-1]