def firstNonRepChar(string):
   char_order = []
   times = {}
   for c in string:
      if c in times:
         times[c] += 1
      else:
         times[c] = 1
         char_order.append(c)
   for c in char_order:
      if times[c] == 1:
       return c
   return None
