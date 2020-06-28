import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
exp = pd.read_csv('csv/exp/ant-dir/progress.csv')
maml = pd.read_csv('csv/maml/ant-dir/progress.csv')
pearl = pd.read_csv('csv/pearl/ant-dir/progress.csv')#源数据
pearl_mirror = pd.read_csv('csv/pearl-mirror/ant-dir/progress.csv')#复现
pearl_czx = pd.read_csv('csv/pearl-czx/ant-dir/progress.csv')
promp = pd.read_csv('csv/promp/ant-dir/progress.csv')
rl2 = pd.read_csv('csv/rl2/ant-dir/progress.csv')
recurrent = pd.read_csv('csv/recurrent/ant-dir/oyster2020/progress.csv')
recurrent = pd.read_csv('csv/recurrent/ant-dir/recurrent/progress.csv')

# print(exp['Number of train steps total'])
def to_percent(temp, position):
    return '$%.1f$' % (temp / 1000000)
plt.style.use('seaborn')
plt.grid(True,color='white')
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
plt.plot(exp['Number of train steps total'],exp['AverageReturn_all_test_tasks'],c='red')
#plt.plot(pearl['Number of train steps total'],pearl['AverageReturn_all_test_tasks'],c='blue')
plt.plot(pearl_mirror['Number of train steps total'],pearl_mirror['AverageReturn_all_test_tasks'],c='blue')
#plt.plot(pearl_czx['Number of train steps total'],pearl_czx['AverageReturn_all_test_tasks'],c='black')
plt.plot(maml['n_timesteps'],maml['Step_1-AverageReturn'],c='green')
plt.plot(rl2['n_timesteps'],rl2['train-AverageReturn'],c='purple')
plt.plot(promp['n_timesteps'],promp['Step_1-AverageReturn'],c='yellow')
plt.plot(recurrent['Number of train steps total'],recurrent['AverageReturn_all_train_tasks'],c='black')
plt.hlines(730,0,1e6,colors="purple",linestyles='--')
plt.hlines(510,0,1e6,colors="green",linestyles='--')
plt.hlines(260,0,1e6,colors="yellow",linestyles='--')
plt.xlabel("百万训练时间步")
plt.xlim(0 , 2e6 )
plt.ylabel("平均回报")
plt.title("ant-dir")
plt.savefig("ant-dir.eps")
plt.show()