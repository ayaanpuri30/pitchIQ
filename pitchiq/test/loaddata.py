import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
# Load the .npy file
data = np.load(r'C:\Python312\Lib\site-packages\england_epl\2015-2016\2016-04-09 - 19-30 Manchester City 2 - 1 West Brom\1_ResNET_TF2_PCA512.npy', allow_pickle=True)


print(type(data))  # Check the data type (e.g., dict, list, array)
print(data.shape)  # If it's an array or matrix, check the shape
print(data)  # Get a glimpse of the actual contents


plt.hist(data.flatten(), bins=50)
plt.title("Distribution of Features")
plt.show()



# Reduce to 2D
pca = PCA(n_components=2)
data_reduced = pca.fit_transform(data)


