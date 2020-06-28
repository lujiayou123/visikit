import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

exp = pd.read_csv('csv/exp/cheetah-vel/progress.csv')
maml = pd.read_csv('csv/maml/cheetah-vel/progress.csv')
pearl = pd.read_csv('csv/pearl/cheetah-vel/progress.csv')
pearl_mirror = pd.read_csv('csv/pearl-mirror/cheetah-vel/progress.csv')
promp = pd.read_csv('csv/promp/cheetah-vel/progress.csv')
rl2 = pd.read_csv('csv/rl2/cheetah-vel/progress.csv')
recurrent = pd.read_csv('csv/recurrent/cheetah-vel/oyster2020/progress.csv')
# recurrent = pd.read_csv('csv/recurrent/cheetah-vel/recurrent/progress.csv')

def to_percent(temp, position):
    return '$%.1f$' % (temp / 1000000)
plt.style.use('seaborn')
plt.grid(True,color='white')
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
plt.plot(recurrent['Number of train steps total'],recurrent['AverageTrainReturn_all_train_tasks'],c='black')
plt.plot(pearl_mirror['Number of train steps total'],pearl_mirror['AverageReturn_all_test_tasks'],c='red',label="αpearl")
plt.plot(pearl['Number of train steps total'],pearl['AverageReturn_all_test_tasks'],c='blue',label="pearl")
plt.plot(maml['n_timesteps'],maml['Step_1-AverageReturn'],c='green',label="maml")
plt.plot(rl2['n_timesteps'],rl2['train-AverageReturn'],c='purple',label="rl2")
plt.plot(promp['n_timesteps'],promp['Step_1-AverageReturn'],c='yellow',label="promp")
plt.hlines(-30,0,1e6,colors="purple",linestyles='--')
plt.hlines(-120,0,1e6,colors="green",linestyles='--')
plt.hlines(-140,0,1e6,colors="yellow",linestyles='--')
plt.xlabel("百万训练时间步")
plt.xlim(0 , 1e6 )
plt.ylabel("平均回报")
plt.title("cheetah-vel")
plt.savefig("cheetah-vel.eps")
plt.show()



