"""Udemy - 100 Days of Code"""
scores = [100, 22, 300, 125, 331, 238, 234732, 34181, 123827, 126345, 12847124, 8471,21738]
high_score = 0
for score in scores:
    if score > high_score:
        high_score = score
print(high_score)

print(max(scores))

print(sorted(scores)[-1])