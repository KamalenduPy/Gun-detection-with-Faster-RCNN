#### create a text file having required format to feed the model; Change image file location accordingly
### here base path should contain the csv file called bbox.csv. whaic holds the information about file location, bbox informations in filename,Xmin,XMax,Ymin,Ymax, ClassLabel as columns.
##### Base path should contain Folder named 'WeaponS', that contains images of weapons.


base_path=home_dir      
train_df= pd.read_csv('bbox.csv')

# For training
# f= open(base_path + "/annotation.txt","w+")
f= open('annotation.txt',"w+")
for idx, row in train_df.iterrows():

    img = cv2.imread((base_path + '/WeaponS/' + row['filepath'] + '.jpg'))
#     height, width = img.shape[:2]
    x1 = int(row['XMin'])
    x2 = int(row['XMax'])
    y1 = int(row['YMin'])
    y2 = int(row['YMax'])
    
    google_colab_file_path = os.path.join(home_dir,'WeaponS')
    fileName = os.path.join(google_colab_file_path, row['filepath'])
    className = row['ClassName']
    f.write(fileName +'.jpg' + ',' + str(x1) + ',' + str(y1) + ',' + str(x2) + ',' + str(y2) + ',' + className + '\n')
f.close()