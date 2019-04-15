#Tail Sizing

#volume coefficients
V_h=0.61
V_v=0.037
#area of main wing
S=138    #****Pretty sure this changed to higher number
#mean chord length
c=4.2
#wing span
b=33
#distance between aerodynamic center of the wing to the tail
x_h=18
x_v=17


#tail area in ft
S_h= V_h*S*c/x_h

S_v= V_v*S*b/x_v

print (S_h, S_v)

