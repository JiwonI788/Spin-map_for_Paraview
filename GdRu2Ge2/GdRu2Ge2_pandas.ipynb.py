{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python382jvsc74a57bd031f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6",
   "display_name": "Python 3.8.2 64-bit"
  },
  "metadata": {
   "interpreter": {
    "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "For GdRu2Ge2 in (H,K,0) plane\n"
     ]
    },
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "                                                               tau     |tau|  \\\n",
       "(4.000000 , 0.000000 , 0)            [5.935933214151711, 0.0, 0.0]  5.935933   \n",
       "(4.000000 +q, 0.000000 , 0)          [6.155933214151711, 0.0, 0.0]  6.155933   \n",
       "(4.000000 -q, 0.000000 , 0)          [5.715933214151711, 0.0, 0.0]  5.715933   \n",
       "(4.000000 , 0.000000 +q, 0)         [5.935933214151711, 0.22, 0.0]  5.940009   \n",
       "(4.000000 , 0.000000 -q, 0)        [5.935933214151711, -0.22, 0.0]  5.940009   \n",
       "(4.000000 +q/2, 0.000000 +q/2, 0)   [6.045933214151711, 0.11, 0.0]  6.046934   \n",
       "(4.000000 -q/2, 0.000000 -q/2, 0)  [5.825933214151711, -0.11, 0.0]  5.826972   \n",
       "(4.000000 +q/2, 0.000000 -q/2, 0)  [6.045933214151711, -0.11, 0.0]  6.046934   \n",
       "(4.000000 -q/2, 0.000000 +q/2, 0)   [5.825933214151711, 0.11, 0.0]  5.826972   \n",
       "\n",
       "                                      2theta     alpha       omega  \n",
       "(4.000000 , 0.000000 , 0)          95.049731  0.000000  137.524866  \n",
       "(4.000000 +q, 0.000000 , 0)        99.797368  0.000000  139.898684  \n",
       "(4.000000 -q, 0.000000 , 0)        90.507968  0.000000  135.253984  \n",
       "(4.000000 , 0.000000 +q, 0)        95.135701  2.122548  135.445302  \n",
       "(4.000000 , 0.000000 -q, 0)        95.135701 -2.122548  139.690399  \n",
       "(4.000000 +q/2, 0.000000 +q/2, 0)  97.417143  1.042327  137.666244  \n",
       "(4.000000 -q/2, 0.000000 -q/2, 0)  92.776665 -1.081679  137.470011  \n",
       "(4.000000 +q/2, 0.000000 -q/2, 0)  97.417143 -1.042327  139.750899  \n",
       "(4.000000 -q/2, 0.000000 +q/2, 0)  92.776665  1.081679  135.306654  "
      ],
      "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>tau</th>\n      <th>|tau|</th>\n      <th>2theta</th>\n      <th>alpha</th>\n      <th>omega</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>(4.000000 , 0.000000 , 0)</th>\n      <td>[5.935933214151711, 0.0, 0.0]</td>\n      <td>5.935933</td>\n      <td>95.049731</td>\n      <td>0.000000</td>\n      <td>137.524866</td>\n    </tr>\n    <tr>\n      <th>(4.000000 +q, 0.000000 , 0)</th>\n      <td>[6.155933214151711, 0.0, 0.0]</td>\n      <td>6.155933</td>\n      <td>99.797368</td>\n      <td>0.000000</td>\n      <td>139.898684</td>\n    </tr>\n    <tr>\n      <th>(4.000000 -q, 0.000000 , 0)</th>\n      <td>[5.715933214151711, 0.0, 0.0]</td>\n      <td>5.715933</td>\n      <td>90.507968</td>\n      <td>0.000000</td>\n      <td>135.253984</td>\n    </tr>\n    <tr>\n      <th>(4.000000 , 0.000000 +q, 0)</th>\n      <td>[5.935933214151711, 0.22, 0.0]</td>\n      <td>5.940009</td>\n      <td>95.135701</td>\n      <td>2.122548</td>\n      <td>135.445302</td>\n    </tr>\n    <tr>\n      <th>(4.000000 , 0.000000 -q, 0)</th>\n      <td>[5.935933214151711, -0.22, 0.0]</td>\n      <td>5.940009</td>\n      <td>95.135701</td>\n      <td>-2.122548</td>\n      <td>139.690399</td>\n    </tr>\n    <tr>\n      <th>(4.000000 +q/2, 0.000000 +q/2, 0)</th>\n      <td>[6.045933214151711, 0.11, 0.0]</td>\n      <td>6.046934</td>\n      <td>97.417143</td>\n      <td>1.042327</td>\n      <td>137.666244</td>\n    </tr>\n    <tr>\n      <th>(4.000000 -q/2, 0.000000 -q/2, 0)</th>\n      <td>[5.825933214151711, -0.11, 0.0]</td>\n      <td>5.826972</td>\n      <td>92.776665</td>\n      <td>-1.081679</td>\n      <td>137.470011</td>\n    </tr>\n    <tr>\n      <th>(4.000000 +q/2, 0.000000 -q/2, 0)</th>\n      <td>[6.045933214151711, -0.11, 0.0]</td>\n      <td>6.046934</td>\n      <td>97.417143</td>\n      <td>-1.042327</td>\n      <td>139.750899</td>\n    </tr>\n    <tr>\n      <th>(4.000000 -q/2, 0.000000 +q/2, 0)</th>\n      <td>[5.825933214151711, 0.11, 0.0]</td>\n      <td>5.826972</td>\n      <td>92.776665</td>\n      <td>1.081679</td>\n      <td>135.306654</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
     },
     "metadata": {},
     "execution_count": 2
    }
   ],
   "source": [
    "import numpy as np\n",
    "import math\n",
    "import pandas as pd\n",
    "\n",
    "#for range\n",
    "#Reciprocal lattice in (H,K,0) plane for Gd2PdSi3\n",
    "pi=np.pi\n",
    "E=7.935\n",
    "lmbda=12.39/E\n",
    "k=2*pi/lmbda\n",
    "a_rcp=2*pi/4.234#a*\n",
    "q=0.22\n",
    "listall = []\n",
    "\n",
    "a_star = np.array([a_rcp,0,0])      # a* vector (parallel to the x axis at w=0)\n",
    "b_star = np.array([0,a_rcp,0])     # b* vector\n",
    "q1 = np.array([q,0,0]) \n",
    "q2 = np.array([0,q,0]) \n",
    "q3 = np.array([q/2,q/2,0]) \n",
    "q4 = np.array([q/2,-q/2,0]) \n",
    "\n",
    "Ht = 4.0     # target H。好きな値に変えよう！\n",
    "Kt = 0.0        # target K。好きな値に変えよう！\n",
    "\n",
    "tau = np.array([Ht*a_star + Kt*b_star,\n",
    "               Ht*a_star + Kt*b_star +q1,\n",
    "               Ht*a_star + Kt*b_star -q1,\n",
    "               Ht*a_star + Kt*b_star +q2,\n",
    "               Ht*a_star + Kt*b_star -q2,\n",
    "               Ht*a_star + Kt*b_star +q3,\n",
    "                Ht*a_star + Kt*b_star -q3,\n",
    "                Ht*a_star + Kt*b_star +q4,\n",
    "                Ht*a_star + Kt*b_star -q4]\n",
    "              )# そのままベクトルの足し算が出来ます。tauはベクトル(np.array)です。\n",
    "target = np.array([\"(%f , %f , 0)\"%(Ht,Kt),\n",
    "                  \"(%f +q, %f , 0)\"%(Ht,Kt),\n",
    "                  \"(%f -q, %f , 0)\"%(Ht,Kt),\n",
    "                  \"(%f , %f +q, 0)\"%(Ht,Kt),\n",
    "                  \"(%f , %f -q, 0)\"%(Ht,Kt),\n",
    "                  \"(%f +q/2, %f +q/2, 0)\"%(Ht,Kt),\n",
    "                  \"(%f -q/2, %f -q/2, 0)\"%(Ht,Kt),\n",
    "                  \"(%f +q/2, %f -q/2, 0)\"%(Ht,Kt),\n",
    "                  \"(%f -q/2, %f +q/2, 0)\"%(Ht,Kt)\n",
    "                  ])#ターゲットベクトル変更\n",
    "\n",
    "for i in range(len(tau)):\n",
    "    tau_length = np.linalg.norm(tau[i])    # np.linalg.norm( )　はnp.arrayで定義したベクトルの大きさを求める\n",
    "    theta = np.arcsin(lmbda*tau_length/4/pi)*180/pi   #in bragg's law\n",
    "    alpha = np.arctan2(tau[i][1],tau[i][0])*180/pi    # np.arctan2(y,x) は、 (x,y)の点についてx軸から測った角度を求める。tau[0]はtau vectorのx成分、tau[1]はy成分。\n",
    "    omega = theta+90.0-alpha\n",
    "    listall.append([tau[i],tau_length,2*theta,alpha,omega])\n",
    "\n",
    "col = ['tau','|tau|','2theta','alpha','omega']\n",
    "\n",
    "df = pd.DataFrame(listall,index=target, columns=col)\n",
    "print(\"For GdRu2Ge2 in (H,K,0) plane\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}