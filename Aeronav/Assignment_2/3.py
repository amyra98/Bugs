s  ="Dear Diary,Need me some vitamin c, maybe some salad or a chowder would do. And what was that about a mechanical brain? Honestly this technology will be our demise. These are the best of times, and the worst of times. Sorry for the short note today, my mother is calling, we got tickets to the game! I need to go. Honestly this mundane life is driving me mad, I should consider getting some help. Bye!"
ans = ""
for i in s.split():
    i.lower()
    ans+=chr(ord('a')-1+len(i))
print(ans)