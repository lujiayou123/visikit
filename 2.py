import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import os

SEED_NUM = 2
ENVs = ["ant-dir", "ant-goal", "cheetah-dir", "cheetah-vel", "humanoid-dir", "walker2d"]
TASK_LIMs = [3e6, 1e6, 1e6, 1e6, 1e6, 2e6]
task_index = 5
ENV = ENVs[task_index]
TASK_LIM = TASK_LIMs[task_index]

if task_index == 0:
    rl2_lim = 730
    maml_lim = 510
    promp_lim = 260
elif task_index == 1:
    rl2_lim = -510
    maml_lim = -370
    promp_lim = -420
elif task_index == 2:
    rl2_lim = 1020
    maml_lim = 450
    promp_lim = 760
elif task_index == 3:
    rl2_lim = -30
    maml_lim = -120
    promp_lim = -140
elif task_index == 4:
    rl2_lim = 518
    maml_lim = 189
    promp_lim = 290
elif task_index == 5:
    rl2_lim = 540
    maml_lim = 490
    promp_lim = 390

# explorer = []
# for seed in range(SEED_NUM):
#     file = os.path.join(os.path.join(os.path.join(os.path.join("csv", "explorer"), ENV), ENV + "_s" + str(seed)),
#                         "progress.csv")
#     pd_data = pd.read_csv(file)
#     pd_data.insert(len(pd_data.columns), "Unit", seed)
#     pd_data.insert(len(pd_data.columns), "Algorithm", "explorer")
#     explorer.append(pd_data)
# explorer = pd.concat(explorer, ignore_index=True)

rl2 = []
for seed in range(SEED_NUM):
    file = os.path.join(os.path.join(os.path.join(os.path.join("csv", "rl2"), ENV), ENV + "_s" + str(seed)),
                        "progress.csv")
    pd_data = pd.read_csv(file)
    pd_data.insert(len(pd_data.columns), "Unit", seed)
    pd_data.insert(len(pd_data.columns), "Algorithm", "rl2")
    rl2.append(pd_data)
rl2 = pd.concat(rl2, ignore_index=True)

maml = []
for seed in range(SEED_NUM):
    file = os.path.join(os.path.join(os.path.join(os.path.join("csv", "maml"), ENV), ENV + "_s" + str(seed)),
                        "progress.csv")
    pd_data = pd.read_csv(file)
    pd_data.insert(len(pd_data.columns), "Unit", seed)
    pd_data.insert(len(pd_data.columns), "Algorithm", "maml")
    maml.append(pd_data)
maml = pd.concat(maml, ignore_index=True)

promp = []
for seed in range(SEED_NUM):
    file = os.path.join(os.path.join(os.path.join(os.path.join("csv", "promp"), ENV), ENV + "_s" + str(seed)),
                        "progress.csv")
    pd_data = pd.read_csv(file)
    pd_data.insert(len(pd_data.columns), "Unit", seed)
    pd_data.insert(len(pd_data.columns), "Algorithm", "promp")
    promp.append(pd_data)
promp = pd.concat(promp, ignore_index=True)

pearl = []
for seed in range(SEED_NUM):
    file = os.path.join(os.path.join(os.path.join(os.path.join("csv", "pearl"), ENV), ENV + "_s" + str(seed)),
                        "progress.csv")
    pd_data = pd.read_csv(file)
    pd_data.insert(len(pd_data.columns), "Unit", seed)
    pd_data.insert(len(pd_data.columns), "Algorithm", "pearl")
    pearl.append(pd_data)
pearl = pd.concat(pearl, ignore_index=True)

def to_percent(temp, position):
    return '$%.1f$' % (temp / 1000000)
plt.style.use('seaborn')
plt.grid(True,color='white')
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))

sns.tsplot(data=rl2, time="n_timesteps", value="train-AverageReturn", condition="Algorithm", unit="Unit",color="purple")
sns.tsplot(data=maml, time="n_timesteps", value="Step_1-AverageReturn", condition="Algorithm", unit="Unit",color="green")
sns.tsplot(data=promp, time="n_timesteps", value="Step_1-AverageReturn", condition="Algorithm", unit="Unit",color="yellow")
sns.tsplot(data=pearl, time="Number of train steps total", value="AverageReturn_all_test_tasks", condition="Algorithm", unit="Unit", color="blue")

plt.hlines(rl2_lim,0,TASK_LIM,colors="purple",linestyles='--')
plt.hlines(maml_lim,0,TASK_LIM,colors="green",linestyles='--')
plt.hlines(promp_lim,0,TASK_LIM,colors="yellow",linestyles='--')
plt.xlabel("Million Train Steps")
plt.xlim(0 , TASK_LIM )
plt.ylabel("Average Return")
plt.title(ENV)
plt.savefig(ENV+".eps")
plt.show()