
import cmath
print ('solve the quadratic equation: ax**2+bx+c=0')
a = float (input ('please enter a : '))
b = float (input ('please enter b : '))
c = float (input ('please enter c : '))
#let u present (b**2) - (4*a*c)
u = (b**2)-(4*a*c)
solution1 =(-b-cmath.sqrt(u))/(2*a)
solution2 =(-b+cmath.sqrt(u))/(2*a)
print('the solutions are (0) and (1)' .format(solution1, solution2))
           
