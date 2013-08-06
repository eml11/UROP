import numpy as np
import pylab as pb

a = 6.37122*10**6
omega = 7.292*10**-5
g = 9.80616

theta = np.linspace(-np.pi/2.0,np.pi/2.0,100)
lamb = np.linspace(0,2*np.pi,100)

alpha = np.array([0.0,0.05,np.pi/2.0-0.05,np.pi/2.0])
h_0 = 1000
theta_c=0
lamb_c=3*np.pi/2.0
u_0 = 40.0

theta_sq = np.outer(np.ones_like(lamb),theta)
lamb_sq = np.outer(lamb,np.ones_like(theta))
lamb_c_sq = np.ones_like(lamb_sq)*lamb_c

R = a/3.0 
pb.hold(False)

rad2deg = 180.0/np.pi
for i in alpha:
  u = u_0*(np.cos(theta_sq)*np.cos(i)+np.sin(theta_sq)*np.cos(lamb_sq)*np.sin(i))
  v = -u_0*np.sin(lamb)*np.sin(i)
  if i != 0:
    CS = pb.contour(lamb_sq*rad2deg,theta_sq*rad2deg,np.outer(v,np.ones_like(theta)))
    pb.clabel(CS, inline=1, fontsize=10)
    pb.gray()
    pb.savefig('vvelocity_a'+str(i)+'.png')
  CS = pb.contour(lamb_sq*rad2deg,theta_sq*rad2deg,u)
  pb.clabel(CS, inline=1, fontsize=10)
  pb.gray()
  pb.savefig('uvelocity_a'+str(i)+'.png')
  
r = a*np.arccos(np.sin(theta_c)*np.sin(theta_sq)+np.cos(theta_c)*np.cos(theta_sq)*np.cos(lamb_sq - lamb_c_sq))
h = (h_0/2.0)*(1 + np.cos(np.pi*r/R))
h = np.where(r >= R, 0, h)

CS = pb.contour(lamb_sq*rad2deg,theta_sq*rad2deg,h)
pb.clabel(CS, inline=1, fontsize=10)
pb.gray()
pb.savefig('bell_displacement'+'.png')
