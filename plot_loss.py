import matplotlib.pyplot as plt


# input file to read
epochs = []
losses = []
with open('logs/training_logs_RN50.txt') as f:
    for index, line in enumerate(f):
        if "Epoch: " in line:
            epoch = line.split('Epoch: ')[-1].split(',')[0]
            loss = line.split('loss: ')[-1].split(' ')[0]
            if epoch not in epochs:
                epochs.append( epoch )
                losses.append( loss )

plt.plot(epochs, losses)
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()