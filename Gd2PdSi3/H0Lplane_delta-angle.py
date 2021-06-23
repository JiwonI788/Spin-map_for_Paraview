import numpy as np
#Reciprocal lattice in (H,0,L) plane for Gd2PdSi3
lmbda=1.5
a_rcp=1.78042#a*
c_rcp=1.53248#c*
q=1/7
pi=np.pi
delta =0.04#unknown value. change it!

#(1,0,0)
tau0=a_rcp#reciprocal length to the peak
theta0=np.arcsin(lmbda*tau0/4/pi)*180/pi#in bragg's law

#(1+q,0,delta)
tau1=np.sqrt(np.square(a_rcp*(1+q))+np.square(c_rcp*delta))
theta1=np.arcsin(lmbda*tau1/4/pi)*180/pi
alpha1=np.arctan(delta/(1+q))*180/pi

#(1+q,0,-delta)

#(1-q,0,delta)
tau3=np.sqrt(np.square(a_rcp*(1-q))+np.square(c_rcp*delta))
theta3=np.arcsin(lmbda*tau3/4/pi)*180/pi
alpha2=np.arctan(delta/(1-q))*180/pi

#(1-q,0,-delta)

#make array
tau=np.array([tau0,tau1,tau1,tau3,tau3])#tau2=tau1, tau4=tau3
theta=np.array([theta0,theta1,theta1,theta3,theta3])
omega=np.array([90+theta0,90+theta1-alpha1,90+theta1+alpha1,90+theta3-alpha2,90+theta3+alpha2])
#print
print("For Gd2PdSi3 in (H,0,L) plane\n[(1,0,0),(1+q,0,delta),(1+q,0,-delta),(1-q,0,delta),(1-q,0,-delta)] =\n",omega)
print("Delta_omega =",np.max(omega)-np.min(omega))
print("measure_omega=",np.max(omega)+5," - ",np.min(omega)-5," = ",np.max(omega)-np.min(omega)+10)
print("tau =", tau)
print("2theta =", theta*2)
print("alpha =",alpha1, alpha2)