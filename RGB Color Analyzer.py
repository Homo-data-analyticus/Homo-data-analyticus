#import imageio
import matplotlib.pyplot as plt
import pandas as pd
#%matplotlib inline

#pic = imageio.imread('\Users\gabel\Documents\Omni-man.jpg')
#lt.figure(figsize =(15,15))
#plt.imshow(pic)
for i in range(3):
    filename = 'StudentsPerformance.csv'.format(str(i))
    print(filename)
    
    try:
        df = pd.read_csv(filename)
        print(df)
    except FileNotFoundError as e:
        print('File pathway wasnt found'.format(filename))
    print()