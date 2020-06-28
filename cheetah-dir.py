import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
exp = []
maml = []
promp = []
rl2 = []
pearl = []
exp = pd.read_csv('csv/exp/cheetah-dir/progress.csv')
maml = pd.read_csv('csv/maml/cheetah-dir/progress.csv')
pearl = pd.read_csv('csv/pearl/cheetah-dir/progress.csv')
pearl_mirror = pd.read_csv('csv/pearl-mirror/cheetah-dir/progress.csv')
promp = pd.read_csv('csv/promp/cheetah-dir/progress.csv')
rl2 = pd.read_csv('csv/rl2/cheetah-dir/progress.csv')
pearl_fix = pd.read_csv('csv/pearl-fix/cheetah-dir/progress.csv')
# recurrent = pd.read_csv('csv/recurrent/cheetah-dir/oyster2020/progress.csv')
# recurrent = pd.read_csv('csv/recurrent/cheetah-dir/recurrent/progress.csv')
def to_percent(temp, position):
    return '$%.1f$' % (temp / 1000000)
plt.style.use('seaborn')
plt.grid(True,color='white')
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
# print(exp['Number of train steps total'])
# plt.plot(recurrent['Number of train steps total'],recurrent['AverageTrainReturn_all_train_tasks'],c='black')
plt.plot(exp['Number of train steps total'],exp['AverageTrainReturn_all_train_tasks'],c='red')
# plt.plot(exp['Number of train steps total'],exp['AverageReturn_all_train_tasks'],c='red')
# plt.plot(exp['Number of train steps total'],exp['AverageReturn_all_test_tasks'],c='red')
# plt.plot(pearl['Number of train steps total'],pearl['AverageReturn_all_test_tasks'],c='blue')
plt.plot(pearl_mirror['Number of train steps total'],pearl_mirror['AverageReturn_all_test_tasks'],c='blue')
# plt.plot(pearl_fix['Number of train steps total'],pearl_fix['AverageReturn_all_test_tasks'],c='black')
plt.plot(maml['n_timesteps'],maml['Step_1-AverageReturn'],c='green')
plt.plot(rl2['n_timesteps'],rl2['train-AverageReturn'],c='purple')
plt.plot(promp['n_timesteps'],promp['Step_1-AverageReturn'],c='yellow')
plt.hlines(1020,0,1e6,colors="purple",linestyles='--')
plt.hlines(450,0,1e6,colors="green",linestyles='--')
plt.hlines(760,0,1e6,colors="yellow",linestyles='--')
plt.xlabel("百万训练时间步")
plt.xlim(0 , 1e6 )
plt.ylabel("平均回报")
plt.title("cheetah-dir")
plt.savefig("cheetah-dir.eps")
plt.show()