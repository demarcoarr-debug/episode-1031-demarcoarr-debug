import sys
import random
total_darts=8
if len(sys.argv)>1:
    total_darts=int(sys.argv[1])

in_circle=0


for i in range(total_darts):
   dart_x= random.random()
   dart_y=random.random()
   if dart_x*dart_x + dart_y*dart_y<=1:
       in_circle+=1

print(f'We got {in_circle} out of {total_darts} inside the circle')

print('our estimate for Π is' ,{4.0* in_circle/total_darts})
