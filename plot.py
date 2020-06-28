import pandas as pd
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
import time
SEED_NUM = 2
ENV = "ant-dir"

if __name__ == '__main__':
    file = os.path.join(os.path.join("csv", ENV), "progress.csv")
    algo = ["maml","promp"]
    data = []
    for i in range(len(algo)):
        for seed in range(SEED_NUM):
            file = os.path.join(os.path.join(os.path.join(os.path.join("csv", algo[i]), ENV), ENV + "_s" + str(seed)), "progress.csv")
            pd_data = pd.read_csv(file)
            pd_data.insert(len(pd_data.columns), "Unit", seed)
            pd_data.insert(len(pd_data.columns), "Condition", algo[i])

            data.append(pd_data)
            #
            # print(data)
            # time.sleep(1111)



    data = pd.concat(data, ignore_index=True)
    # print("#################################")
    print(data)

    sns.set(style="darkgrid", font_scale=1.5)
    sns.tsplot(data=data, time="n_timesteps", value="Step_1-AverageReturn", condition="Condition", unit="Unit")

    xscale = np.max(data["n_timesteps"]) > 5e3
    if xscale:
        plt.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))

    plt.legend(loc='best').set_draggable(True)
    plt.tight_layout(pad=0.5)
    plt.show()








