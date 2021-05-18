l = [1,2,1,3,4,4,2]
s = set (l)
u = {1,2,7}
print ("s", s)
print ("u", u)
print ("union",s|u) #union
print ("diff s-u", s-u) #diff
print ("unique s^u", s^u) #unique
print ("unique u^s", u^s) #unique
print ("is s subset of u:", s<=u)
