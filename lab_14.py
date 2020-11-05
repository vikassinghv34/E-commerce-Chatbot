import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

dust=np.arange(0,11,1)
cloth=np.arange(0,11.1)
wash=np.arange(0,26,1)

dust_low=fuzz.trimf(dust,[0,0,5])
dust_mid=fuzz.trimf(dust,[0,5,10])
dust_high=fuzz.trimf(dust,[5,10,10])
cloth_low=fuzz.trimf(cloth,[0,0,5])
cloth_mid=fuzz.trimf(cloth,[0,5,10])
cloth_high=fuzz.trimf(cloth,[5,10,10])
wash_low=fuzz.trimf(wash,[0,0,13])
wash_mid=fuzz.trimf(wash,[0,13,25])
wash_high=fuzz.trimf(wash,[13,25,25])

fig,(ax0,ax1,ax2)=plt.subplots(nrows=3,figsize=(8,9))

ax0.plot(dust,dust_low,'b',linewidth=1.5,label='low')
ax0.plot(dust,dust_mid,'g',linewidth=1.5,label='medium')
ax0.plot(dust,dust_high,'r',linewidth=1.5,label='high')
ax0.set_title('Dust')
ax0.legend()

ax1.plot(cloth,cloth_low,'b',linewidth=1.5,label='poor')
ax1.plot(cloth,cloth_mid,'g',linewidth=1.5,label='acceptable')
ax1.plot(cloth,cloth_high,'r',linewidth=1.5,label='amazing')
ax1.set_title('Type of cloth')
ax1.legend()

ax2.plot(wash,wash_low,'b',linewidth=1.5,label='good')
ax2.plot(wash,wash_mid,'g',linewidth=1.5,label='nice')
ax2.plot(wash,wash_high,'r',linewidth=1.5,label='excellent')
ax2.set_title('wash Amount')
ax2.legend()

for ax in (ax0,ax1,ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
plt.tight_layout()
    

dust_level_low=fuzz.interp_membership(dust,dust_low,6.5)
dust_level_mid=fuzz.interp_membership(dust,dust_mid,6.5)
dust_level_high=fuzz.interp_membership(dust,dust_high,6.5)

cloth_level_low=fuzz.interp_membership(cloth,cloth_low,9.8)
cloth_level_mid=fuzz.interp_membership(cloth,cloth_mid,9.8)
cloth_level_high=fuzz.interp_membership(cloth,cloth_high,9.8)

active_rule1=np.fmax(dust_level_low,cloth_level_low)
wash_activation_low=np.fmin(active_rule1,wash_low)

# active_rule2=np.fmax(dust_level_mid,cloth_level_mid)
wash_activation_mid=np.fmin(cloth_level_mid,wash_mid)

active_rule3=np.fmax(dust_level_high,cloth_level_high)
wash_activation_high=np.fmin(active_rule3,wash_high)

wash0=np.zeros_like(wash)

fig,ax0=plt.subplots(figsize=(8,3))

ax0.fill_between(wash,wash0,wash_activation_low,facecolor='b',alpha=0.7)
ax0.plot(wash,wash_low,'b',linewidth=0.5,linestyle='--')
ax0.fill_between(wash,wash0,wash_activation_mid,facecolor='g',alpha=0.7)
ax0.plot(wash,wash_mid,'g',linewidth=0.5,linestyle='--')
ax0.fill_between(wash,wash0,wash_activation_high,facecolor='r',alpha=0.7)
ax0.plot(wash,wash_high,'r',linewidth=0.5,linestyle='--')

ax0.set_title('Output membership activity')

for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

aggregated=np.fmax(wash_activation_low,np.fmax(wash_activation_mid,wash_activation_high))

washp=fuzz.defuzz(wash,aggregated,'centroid')
wash_activation=fuzz.interp_membership(wash,aggregated,washp)

fig,ax0=plt.subplots(figsize=(8,3))

ax0.plot(wash,wash_low,'b',linewidth=0.5,linestyle='--')
ax0.plot(wash,wash_mid,'g',linewidth=0.5,linestyle='--')
ax0.plot(wash,wash_high,'r',linewidth=0.5,linestyle='--')

ax0.fill_between(wash,wash0,aggregated,facecolor='Orange',alpha=0.7)

ax0.plot([washp,washp],[0,wash_activation],'k',linewidth=1.5,alpha=0.9)

ax0.set_title('Aggregated membership and result(line)')

for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()