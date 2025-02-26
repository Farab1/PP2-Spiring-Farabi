import re

text = "a_b a_aab aaaaaa_aaaaaaab a_b_b_bbb ab ab_b abb_bb abbb_bbbb"

x = re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower()

print(x)