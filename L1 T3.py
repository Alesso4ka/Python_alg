# Задание 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

ax = int(input('Enter the X coordinate of point A '))
ay = int(input('Enter the Y coordinate of point A '))
bx = int(input('Enter the X coordinate of point B '))
by = int(input('enter the Y coordinate of point B '))

if ax == ay and bx == by:
    exit('The coordinates of the points are the same. It is impossible to draw a straight line through one point.')

k = (ay - by) / (ax - bx)
b = by - k * bx
print('The equation of a straight line through these 2 points will look like this:\n'
      'y = {:.2f}*x {} {:.2f}'.format(k, '+' if b >= 0 else '', b))
