import numpy as np
#Reciprocal lattice in (H,K,0) plane for Gd2PdSi3
lmbda=1.5
a_rcp=1.78042#a*
q=1/7
pi=np.pi
delta =0.04#unknown value. change it!

a_star = np.array([a_rcp,0,0])      # a* vector (parallel to the x axis at w=0)
b_star = np.array([a_rcp/2.0,a_rcp*np.sqrt(3.0)/2.0,0])     # b* vector

Ht = 1.0     # target H。好きな値に変えよう！
Kt = 0.0        # target K。好きな値に変えよう！

tau = Ht*a_star + Kt*b_star         # そのままベクトルの足し算が出来ます。tauはベクトル(np.array)です。
tau_length = np.linalg.norm(tau)    # np.linalg.norm( )　はnp.arrayで定義したベクトルの大きさを求める
theta = np.arcsin(lmbda*tau_length/4/pi)*180/pi   #in bragg's law
alpha = np.arctan2(tau[1],tau[0])*180/pi    # np.arctan2(y,x) は、 (x,y)の点についてx軸から測った角度を求める。tau[0]はtau vectorのx成分、tau[1]はy成分。
omega = theta+90.0-alpha

print("For Gd2PdSi3 in (H,K,0) plane")
print("target : (%f, %f, 0) in r. l. u."%(Ht,Kt))
print("tau = (%f, %f, %f) in A-1 unit"%(tau[0],tau[1],tau[2]))
print("|tau| = %f A-1"%(tau_length))
print("2theta = %f deg."%(theta*2))
print("Omega = %f deg"%(omega))

'''
#(1,0,0)
tau0=a_rcp#reciprocal length to the peak
theta0=np.arcsin(lmbda*tau0/4/pi)*180/pi#in bragg's law

#(1+q,0,0)
tau1=a_rcp*(1+q)
theta1=np.arcsin(lmbda*tau1/4/pi)*180/pi

#(1-q,0,0)
tau2=a_rcp*(1-q)
theta2=np.arcsin(lmbda*tau2/4/pi)*180/pi

#(1,q,0)
tau3=a_rcp*np.sqrt(np.square((1+q/2))+np.square(q*np.sqrt(3)/2))
theta3=np.arcsin(lmbda*tau3/4/pi)*180/pi
alpha1=np.arctan(np.sqrt(3)*q/2/(1+q/2))*180/pi

#(1,-q,0)
tau4=a_rcp*np.sqrt(np.square((1-q/2))+np.square(q*np.sqrt(3)/2))
theta4=np.arcsin(lmbda*tau4/4/pi)*180/pi
alpha2=np.arctan(np.sqrt(3)*q/2/(1-q/2))*180/pi

#(1+q,-q,0)
tau5=tau3
theta5=theta3
#(1-q,q,0)
tau6=tau4
theta6=theta4

#make array
tau=np.array([tau0,tau1,tau2,tau3,tau4,tau5,tau6])#tau2=tau1, tau4=tau3
theta=np.array([theta0,theta1,theta2,theta3,theta4,theta5,theta6])
omega=np.array([90+theta0,90+theta1,90+theta2,90+theta3-alpha1,90+theta4+alpha2,90+theta5+alpha1,90+theta6-alpha2])
#print
print("For Gd2PdSi3 in (H,0,L) plane\n[(1,0,0),(1+q,0,0),(1-q,0,0),(1,q,0),(1,-q,0),(1+q,-q,0),(1-q,q,0)] =\n",omega)
print("Delta_omega =",np.max(omega)-np.min(omega))
print("tau =", tau)
print("2theta =", theta*2)
print("alpha =",alpha1, alpha2)
'''