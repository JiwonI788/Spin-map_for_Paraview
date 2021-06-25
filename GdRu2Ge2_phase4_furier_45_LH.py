import numpy as np
import pandas as pd

#system size
points_x = 300
points_y = 300
num_points=points_x*points_y
mag=np.zeros((points_x, points_y))
#modulation period
Lambda_m=44.3

#scale factor for the length of arrows
Arrow_scale=1

#90 degree rotation matrix about the z axis
pi=np.pi
rad45=45*pi/180
Rot_45 = np.array([
[np.cos(rad45),np.sin(rad45),0.0],
[-np.sin(rad45),np.cos(rad45),0.0],
[0.0,0.0,1.0]
])


#definitions of lattice constants
a_len=4.234
c_len=9.901

a_vec=np.array([a_len,0.0,0.0])
b_vec=np.array([0.0,a_len,0.0])
c_vec=np.array([0.0,0.0,c_len])
a_vec_45=np.dot(Rot_45,a_vec)
b_vec_45=np.dot(Rot_45,b_vec)
c_vec_45=np.dot(Rot_45,c_vec)


#definitions of Q-vectors
#q-vectorはreciprocal lattice unit (a*, b*, c*のunit)で書くようにしましょう。a*を掛け算する必要はないです。
q_len = 0.05 #a*unit
Q1=np.array([q_len,0.0,0.0])
Q2=np.array([0.0,q_len,0.0])
Q3=np.array([q_len/2,q_len/2,0.0])
Q4=np.array([q_len/2,-q_len/2,0.0])
Q1_45=np.dot(Rot_45,Q1)
Q2_45=np.dot(Rot_45,Q2)
Q3_45=np.dot(Rot_45,Q3)
Q4_45=np.dot(Rot_45,Q4)

        
SA1_vec=np.array([0,0,-1])
SB1_vec=np.array([0,1,0])
SA2_vec=np.array([0,0,-1])
SB2_vec=np.array([-1,0,0])
SA3_vec=np.array([0,0,-1])
SB3_vec=np.array([1,-1,0])/np.sqrt(2)
SA4_vec=np.array([0,0,-1])
SB4_vec=np.array([-1,-1,0])/np.sqrt(2)


SA1_vec_45=np.dot(Rot_45,SA1_vec)
SB1_vec_45=np.dot(Rot_45,SB1_vec)
SA2_vec_45=np.dot(Rot_45,SA2_vec)
SB2_vec_45=np.dot(Rot_45,SB2_vec)
SA3_vec_45=np.dot(Rot_45,SA3_vec)
SB3_vec_45=np.dot(Rot_45,SB3_vec)
SA4_vec_45=np.dot(Rot_45,SA4_vec)
SB4_vec_45=np.dot(Rot_45,SB4_vec)


Fq00=np.array([0,0,0])
Fhqhq0=np.array([0,0,0])
Fqq0=np.array([0,0,0])
Fqmq0=np.array([0,0,0])
F2q00=np.array([0,0,0])

#位置座標の出力
for ii in range(points_x):
    for jj in range(points_y):
        r_vec=float(ii)*a_vec+float(jj)*b_vec #결정구조?

#スピンベクトルの計算
netMz=0
#formatrix, S스핀 돌려주고, 원하는 방향으로 돌리기
for ii in range(points_x):
    for jj in range(points_y):
        r_vec2=np.array([float(ii),float(jj),0.0])
        phase1=(2.0*np.pi)*np.dot(r_vec2,Q1_45)        # r=(na,nb,0)とQ1=(q,0,0)の内積(dot積)。rはa,b,c unit, Qはa*,b*,c* unit.
        phase2=(2.0*np.pi)*np.dot(r_vec2,Q2_45)
        phase3=(2.0*np.pi)*np.dot(r_vec2,Q3_45)
        phase4=(2.0*np.pi)*np.dot(r_vec2,Q4_45)

        Mz=0.43#2가 되면 스킬미온이 아니게됨. 스핀적분이 4pi가 되도록하려면..? 계산할 수도 있지만, 1(?)~1.9정도쯤 중앙부가 나오고 메론-안티메론상태가 없어지도록 해야함. 0일땐 제로자기장이라서 스킬미온이 아닌 메론-안티메론 상태가 됨.(IC-1)
        Sz_vec=np.array([0,0,Mz])
        S1=np.cos(phase1)*SA1_vec_45/3.464+2.464/3.464*np.sin(phase1)*SB1_vec_45 #a direction? or a* direction?
        S2=np.cos(phase2)*SA2_vec_45/3.464+2.464/3.464*np.sin(phase2)*SB2_vec_45
        S3=np.cos(phase3)*SA3_vec_45/1.513+0.513/1.513*np.sin(phase3)*SB3_vec_45
        S4=np.cos(phase4)*SA4_vec_45/1.513+0.513/1.513*np.sin(phase4)*SB4_vec_45

        S_all=(S1+S2)/2.662+(S3+S4)*1.662/2.662+Sz_vec
        S_all=S_all/np.linalg.norm(S_all)
        netMz=netMz+S_all[2]/float(points_x*points_y)#z成分なので、S_all[2]だけ抜き出して足し合わせる,#１スピンあたりのz成分に規格化する
        Fq00=Fq00+S_all*np.exp(1j*(2.0*np.pi)*np.dot(Q1_45,r_vec2))/float(points_x*points_y)
        F2q00=F2q00+S_all*np.exp(1j*(2.0*np.pi)*np.dot(2*Q1_45,r_vec2))/float(points_x*points_y)
        Fhqhq0=Fhqhq0+S_all*np.exp(1j*(2.0*np.pi)*np.dot(Q3_45,r_vec2))/float(points_x*points_y)
        Fqq0=Fqq0+S_all*np.exp(1j*(2.0*np.pi)*np.dot(Q3_45*2,r_vec2))/float(points_x*points_y)
        Fqmq0=Fqmq0+S_all*np.exp(1j*(2.0*np.pi)*np.dot(Q4_45*2,r_vec2))/float(points_x*points_y)
        

#スピンベクトル、Sx, Sy, Szはここまでで終わり。
print(Mz, 7*netMz,points_x, points_y)
#最後に色付けのためにSz成分だけ書き出す。

fq = np.array([Fq00,F2q00, Fhqhq0, Fqq0, Fqmq0])

fq=np.insert(fq,[3],[[0,0]],axis=1)

fq_abs = abs(fq)#np.array([abs(Fq00),abs(F2q00), abs(Fhqhq0), abs(Fqq0), abs(Fqmq0)])

for i in range(len(fq_abs)):
    fq_abs[i][3]=fq_abs[i][0]**2+fq_abs[i][2]**2
    fq_abs[i][4]=fq_abs[i][1]**2+fq_abs[i][2]**2

target_f = np.array(["F(q,0,0)","F(2q,0,0)","F(q/2,q/2,0)","F(q,q,0)","F(q,-q,0)"])#ターゲットベクトル変更

col_f = ['x','y','z','x^2+z^2', 'y^2+z^2']#
qv_45= pd.DataFrame(fq_abs, index=target_f, columns=col_f)#
print("For GdRu2Ge2 in all RH q-vector")
print(qv_45)