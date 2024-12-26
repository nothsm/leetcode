def distinct(xs):
    seen = set()
    d = []
    for x in xs:
        if x not in seen:
            d.append(x)
        seen.add(x)
    return d

def count_chars(s):
  chars = {}
  for c in s:
    chars[c] = chars.get(c, 0) + 1
  return chars
