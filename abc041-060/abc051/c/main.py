d = 'URDL'
sx,sy,tx,ty = map(int,input().split())
dx = tx - sx
dy = ty - sy
print('U' * dy, 'R' * dx, 'D' * dy, 'L' * (dx + 1), 'U' * (dy + 1), 'R' * (dx + 1), 'D', 'R', 'D' * (dy + 1), 'L' * (dx + 1), 'U', sep='')
