import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('tech_analysis.csv')

for col in df.columns[:-1]:
    scaler = MinMaxScaler((-1,1))
    df[col] = scaler.fit_transform(df[[col]])

window = 15
delay = 6
images = []
labels = []
for i in range(3*window+5, len(df)-delay):
    X = df[['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']]
    image = X[i-15:i].values
    label = df['label'][i+delay]
    images.append(image)
    labels.append(label)
    break


for counter, (img, lab) in enumerate(zip(images, labels)):
    with open('raw_dataset_ibm/'+str(counter), 'w+') as f:
        f.write(str(lab)+'\n')
        for row in img:
            for item in row:
                f.write(str(item)+'\n')
