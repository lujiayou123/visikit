import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

exp = pd.read_csv('csv/exp/walker2d/progress.csv')
maml = pd.read_csv('csv/maml/walker2d/progress.csv')
pearl = pd.read_csv('csv/pearl/walker2d/progress.csv')
pearl_mirror = pd.read_csv('csv/pearl-mirror/walker2d/progress.csv')
promp = pd.read_csv('csv/promp/walker2d/progress.csv')
rl2 = pd.read_csv('csv/rl2/walker2d/progress.csv')

def to_percent(temp, position):
    return '$%.1f$' % (temp / 1000000)
plt.style.use('seaborn')
plt.grid(True,color='white')
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
plt.plot(pearl_mirror['Number of train steps total'],pearl_mirror['AverageReturn_all_test_tasks'],c='red',label='α-PEARL')
plt.plot(pearl['Number of train steps total'],pearl['AverageReturn_all_test_tasks'],c='blue',label='PEARL')
plt.plot(maml['n_timesteps'],maml['Step_1-AverageReturn'],c='green',label='MAML')
plt.plot(rl2['n_timesteps'],rl2['train-AverageReturn'],c='purple',label='RL2')
plt.plot(promp['n_timesteps'],promp['Step_1-AverageReturn'],c='yellow',label='ProMP')
plt.hlines(540,0,1e6,colors="purple",linestyles='--')
plt.hlines(490,0,1e6,colors="green",linestyles='--')
plt.hlines(390,0,1e6,colors="yellow",linestyles='--')
plt.xlabel("百万训练时间步")
plt.xlim(0 , 1e6 )
plt.ylabel("平均回报")
plt.legend(loc='best')
plt.title("walker2d")
plt.savefig("walker2d.eps")
plt.show()