from model import load_neural_data
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('dark_background')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

emo_dataframe  = load_neural_data()
instances = emo_dataframe.shape[0]
print instances

def animate(i):
    csv_path = "./emo_raw_reordings.csv"



    xs = []
    ys = []

    # Step 3: Create feature vectors
    x = emo_dataframe.ix[:,:-1].values
    xs.append(x)
    ys.append(instances)

    ax1.clear()
    ax1.plot(xs, ys)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()