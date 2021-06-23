import numpy as np
import pandas as pd

#Reciprocal lattice in (H,K,0) plane for Gd2PdSi3
lmbda=1.5627
pi=np.pi
a_rcp=2*pi/4.234#a*
q=0.22

a_star = np.array([a_rcp,0,0])      # a* vector (parallel to the x axis at w=0)
b_star = np.array([0,a_rcp,0])     # b* vector
q1 = np.array([q,0,0]) 
q2 = np.array([0,q,0]) 
q3 = np.array([q/2,q/2,0]) 
q4 = np.array([q/2,-q/2,0]) 

Ht = 4.0     # target H。好きな値に変えよう！
Kt = 0.0        # target K。好きな値に変えよう！

tau = Ht*a_star + Kt*b_star +q1        # そのままベクトルの足し算が出来ます。tauはベクトル(np.array)です。
tau_length = np.linalg.norm(tau)    # np.linalg.norm( )　はnp.arrayで定義したベクトルの大きさを求める
target = "(%f -q/2, %f +q/2, 0)"%(Ht,Kt) #ターゲットベクトル変更
theta = np.arcsin(lmbda*tau_length/4/pi)*180/pi   #in bragg's law
alpha = np.arctan2(tau[1],tau[0])*180/pi    # np.arctan2(y,x) は、 (x,y)の点についてx軸から測った角度を求める。tau[0]はtau vectorのx成分、tau[1]はy成分。
omega = theta+90.0-alpha

print("For Gd2PdSi3 in (H,K,0) plane")
print("target : (%f, %f, 0) in r. l. u."%(Ht,Kt))
print("tau = (%f, %f, %f) in A-1 unit"%(tau[0],tau[1],tau[2]))
print("|tau| = %f A-1"%(tau_length))
print("2theta = %f deg."%(theta*2))
print("alpha = %f deg."%(alpha))
print("Omega = %f deg"%(omega))

listA = [target,tau_length,2*theta,alpha,omega]
listA
listall=[]
listall.append(listA)
listall
col = ['target','|tau|','2theta','alpha','omega']
df = pd.DataFrame(listall, columns=col)
