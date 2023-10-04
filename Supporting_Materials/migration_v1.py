import os 
import pandas as pd

csv_path = '/home/Plant_Disease_DataSet/Data_Base/Meta_data_01/'
print('Started....')

####################################################################

# SUPPPORTIVE FUNCTINS
PDD217_01 = ['squash virus disease','Pumpkin Powdery Mildew','Pumpkin downy mildew','mustard greens for health','sunflower bacterial leaf spot','sunflower black spot',
 'ChineseCabbage Gray spot','ChineseCabbage anthracnose','ChineseCabbage blight','ChineseCabbage virus disease',
 'ChineseCabbage white spot','ChineseCabbage bacterial brown spot','ChineseCabbage bacterial black spot','ChineseCabbage Magnesium Deficiency Disease',
 'ChineseCabbage injury','ChineseCabbage downy mildew','ChineseCabbage black spot','ChineseCabbage black rot',
 'soybean leaf blight','soybean sunburn','soybean gray spot','Soybean Botrytis','soybean anthracnose','Soybean Soot',
 'soybean blight','soybean virus disease','soybean bacterial spot','Soybean Nitrogen Deficiency','Soy Magnesium Deficiency','soybean mosaic disease','Soybean phytotoxicity',
 'soybean Alternaria black spot','soybean rust','Soybean Jiankang leaves','Soybean Herbicide Injury','soybean downy mildew',
 'soybean target disease','wheat leaf blight','Wheat leaf embroidery','wheat Septoria wheat leaf blight','Wheat Spot Blight','wheat stripe blight',
 'wheat stripe mosaic disease','Wheat shuttle streak mosaic disease','wheat powdery mildew','wheat bacterial leaf blight','wheat mosaic disease',
 'wheat macular blight','Hawthorn Leaf Spot','Hawthorn Rust','Lentil spot disease','Lentil virus disease','Lentil leukoplakia',
 'Lentil brown spot','Jujube Rust','Walnut Black Spot','peach latent mosaic disease','Peach Tree Iron Deficiency',
 'Mulberry Healthy Leaf','Mulberry Anthracnose','Mulberry sooty disease','mulberry Leukoplakia','Mulberry Brown Spot',
 'Pear gray spot','pear tree soot','pear tree brown spot','Pear Rust','Cotton Healthy Leaf','cotton leaf burn',
 'cotton anthracnose','cotton blight','cotton eye spot','Cotton Potassium Deficiency','Cotton Magnesium Deficiency',
 'cotton stem blight','cotton leaf spot','Cotton Herbicide Injury','cotton verticillium wilt','Cherry Bacterial Hole','cherry mosaic virus disease',
 'Cherry Brown Spot Hole','Nectarine Bacterial Hole','Tobacco Leaf Spot','tobacco mosaic disease','Tobacco Scorch','tobacco virus disease','Tobacco rotting leaf spot','tobacco mosaic virus disease',
 'Tobacco frog eye disease','Tobacco spot disease''Tobacco Potato Virus Y','Kiwifruit Leaf Spot','kiwifruit Gray spot',
 'Kiwi Mosaic Virus','Kiwi brown spot disease','corn health','corn spot disease','corn leaf spot','Corn spot disease','maize Curvularia maize leaf spot','corn sunburn',
 'corn root rot leaf spot','corn gray spot','corn soot','corn virus disease','maize dwarf mosaic virus','corn red leaf disease','corn sheath blight',
 'corn Bacterial spot disease','corn bacterial wilt','corn Bacterial red streak disease','corn Phosphorus deficiency','Corn Potassium Deficiency',
 'corn Zinc deficiency','corn brown spot','corn hereditary stripes','corn rust','corn top rot','Kale Health','cabbage phytotoxicity','SweetPotato Healthy Leaves',
 'sweetpotato frost damage','SweetPotato Leaf Spot','sweetpotato Cercospora leaf spot','SweetPotato soot','SweetPotato virus disease',
 'sweetpotato blast','SweetPotato Magnesium Deficiency','SweetPotato Phytotoxicity','SweetPotato scab','melon health','Melon powdery mildew','Melon downy mildew',
 'ginger leaf curl disease','Ginger Anthracnose','Ginger White Spot','Ginger Bacterial Leaf Spot','Ginger mosaic virus disease','Ginger phytotoxicity',
 'Tomato Leaf Spot','Tomato spot blight','Tomato gray leaf spot','PurpleSweetPotato Healthy Leaf','MungBean healthy plant key leaf','MungBean sooty disease',
 'MungBean Magnesium Deficiency','MungBean brown spot','Sesame leaf spot','Sesame leaf blight','Sesame yellow dwarf virus disease','Peanut Healthy Leaf',
 'Peanut Anthracnose','Peanut scorch','Peanut scab','Peanut powdery mildew','peanuts Phosphorus deficiency','Peanut Iron Deficiency',
 'Peanuts Magnesium Deficiency','Peanut net spot and brown spot mixed','Peanut ozone damage','Peanut Brown Spot','Peanut Rust','Peanut Black Spot',
 'Peanut Black Spot and Scorch Spot Mix','Peanut black spot mixed with net spot','Celery Health','Celery Leaf Spot','Celery Leaf Spot','celery Spot blight',
 'celery Mixture of celery spot blight and phytotoxicity','Celery Bacterial Leaf Spot','Celery Bacterial Leaf Blight','Celery phytotoxicity','Celery Black Spot','Apple round spot',
 'Apple lobular disease','Apple spotted defoliation disease','Apple Gray Spot','Apple powdery mildew','Apple Nitrogen Deficiency','Apple phosphorus deficiency',
 'Apple Brown Spot','Apple Rust','Apple herbicide phytotoxicity','Eggplant Health','Strawberry Leaf Blight','Strawberry snake eye disease','Strawberry Brown Spot','Bean powdery mildew',
 'Bean Bacterial Blight','Spinach Healthy','Spinach Black Spot','Radish Leukoplakia','Radish shrunken virus disease','Radish Fat Harm',
 'Radish mosaic virus disease','Radish macular blight','Radish black spot','Radish black rot','Grape Leaf Roll','Grape fan leaf disease','Grape Herbicide Hazards',
 'Grape black pox','Onion Health','Onion Sclerotinia','cinerea Botrytis','Onion Blight','Onion virus disease','Onion purple spot','Onion downy mildew','Onion Black Spot','Blueberry Health','Blueberry Leaf Spot','Blueberry red ring spot virus disease','Blueberry Iron Deficiency','Zucchini powdery mildew','Millet Healthy Leaf','Millet leaf blight','Millet white disease',
 'Millet black sheath disease','Millet Bacterial Stripe','Cowpea spotted blight','cinerea Botrytis','Cowpea Sooty Blight','Cowpea shrunken virus disease',
 'Cowpea red spot disease','cowpea mosaic virus','Cowpea rust','Pepper Health','Pepper Leaf Blight','Pepper Blight','Pepper Blight','Capsicum virus disease',
 'Pepper Leukoplakia','Pepper powdery mildew','Capsicum navel rot','Pepper Brown Spot','Pepper Black Spot','Leek hail damage','cinerea Botrytis','Leek fertilizer damage',
 'Toon powdery mildew mixed with rust','Toon bacterial brown spot','Toon brown spot','Toon Rust','Potato Health','Potato Early Blight','Potato late blight',
 'Sorghum Healthy Leaf','Sorghum leaf spot','Sorghum Anthracnose','Sorghum coal streak','Sorghum coccidioides leaf spot','Sorghum dwarf mosaic disease',
 'Sorghum purple spot','Sorghum sheath blight','Sorghum Bacterial Stripe','Sorghum Bacterial Red Streak','Sorghum mosaic disease','Sorghum leopard spot disease',
 'Sorghum target spot','Cucumber Health','Cucumber Anthracnose','Cucumber Leukoplakia','Cucumber powdery mildew','Cucumber shrunken virus disease',
 'cucumber Bacterial angular leaf spot','Cucumber Angular Spot Leukoplakia Mix','Cucumber downy mildew','Cucumber target spot','Cucumber Black Spot','Cucumber Black Spot','Cucumber Black Spot']


def image_extraction(directory):
    file = []
    for i in range(len(directory)):
        list_img = []
        list_files = os.listdir(directory[i])
        for j in list_files:
            if j == '.ipynb_checkpoints':
                continue
            list_img.append(j)
        file.append(list_img)
    return file

def extract_first_word(text):
    if isinstance(text, str):
        words = text.split()
        if words:
            return words[0]
        else:
            return ""
    else:
        return ""
    
def extracting_directory(path): #This function is for those datasets which has directory structure like database_name/train/disease/file_name
    directory = []
    for i in os.listdir(path):
        concat_path_01 = os.path.join(path,i)
        dir_01 = os.listdir(concat_path_01)
        for k in dir_01:
            p =os.path.join(concat_path_01,k)
            directory.append(p)
    return directory



def sample_extracting_directory(path): # This function is for those datasets which has directory structure like database_name/disease/file_name
    directory = []
    for i in os.listdir(path):
        concat_path_01 = os.path.join(path,i)
        directory.append(concat_path_01)
    return directory



##################################################################################################


def plant_village():
    
    print('Creating Plant village Meta Version_01')
    # Extracting directories within the main folder

    path = '/home/Plant_Disease_DataSet/PlantVillage/plant_village'
    directory = extracting_directory(path)
    # Extracting images out of each directories
    file = image_extraction(directory)
    
    # Creating csv using above data
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        path = l.split('/')[-4:]
        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-3])
            Plantname.append(l.split('/')[-1].split('__')[0])
            imagetype.append('leaves')
            disease.append(l.split('/')[-1].split('__')[1].replace('_','',1))
            location.append('/'.join(path))
        for j in file[i]:
            imageid.append(j)
        combined_data = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
    }
    df = pd.DataFrame(combined_data)
    df.to_csv(csv_path + 'plant_vilage_meta_v1_01.csv', index = False)


def plant_doc():
    
    print('Creating Plant Docs Meta Version_01')
    path = '/home/Plant_Disease_DataSet/plant_docs/PlantDoc/annoatations_01.csv'
    df1 = pd.read_csv(path)
    plant = df1['plant_name']
    for i in range(len(plant.unique())):
        df1['data_set'] = 'plant docs'
        df1['plant_part'] = 'leaf'
        df1['disease'] = df1['class']
        df1['file_name'] = df1['filename']
        df1['file_location'] = 'PlantDocs/train'
    # drop some un-important cols
    drop_cols = ['width','height' ,'filename', 'class' , 'xmin','ymin','xmax','ymax','Unnamed: 8'  ] 
    final_df = df1.drop(columns= drop_cols)
    desired_cols = ['data_set' ,'plant_name' , 'plant_part', 'disease', 'file_name','file_location']
    final_df = final_df[desired_cols]
    final_df.to_csv(csv_path + 'plantdocs_meta_v1.csv', index = False)

def apple2020():
    
    print('Creating apple2020 meta version_01')
    path = '/home/Plant_Disease_DataSet/apple2020/train.csv'
    data = pd.read_csv(path)
    scab = data[data['scab'] == 1]
    scab = scab[['image_id']]
    scab['data_set'] = 'apple2020'
    scab['plant_name'] = 'Apple'
    scab['plant_part'] = 'Leaves'
    scab['disease'] = 'scab'
    scab['file_name'] = scab['image_id']
    scab['file_location'] = 'apple2020/images'
    rust = data[data['rust'] == 1]
    rust = rust[['image_id']]
    rust['data_set'] = 'apple2020'
    rust['plant_name'] = 'Apple'
    rust['plant_part'] = 'Leaves'
    rust['disease'] = 'rust'
    rust['file_name'] = rust['image_id']
    rust['file_location'] = 'apple2020/images'
    healthy = data[data['healthy'] == 1]
    healthy = healthy[['image_id']]
    healthy['data_set'] = 'apple2020'
    healthy['plant_name'] = 'Apple'
    healthy['plant_part'] = 'Leaves'
    healthy['disease'] = 'healthy'
    healthy['file_name'] = healthy['image_id']
    healthy['file_location'] = 'apple2020/images'
    df = pd.concat([scab,rust,healthy])
    df.sort_index()
    col = ['data_set', 'plant_name', 'plant_part', 'disease','file_name', 'file_location']
    df = df[col]
    df = df.sort_index()
    df.to_csv(csv_path + 'apple2020_meta_v1.csv', index= False)
    
def apple2021():
    
    print('Creating apple2021 meta version_01')
    path = '/home/Plant_Disease_DataSet/apple2021/train.csv'
    df = pd.read_csv(path)
    disease = df['labels'].unique()
    list_df = []
    for i in disease:

        a = df[df['labels'] == i].copy()
        a['data_set'] = 'apple2021'
        a['plant_name'] = 'Apple'
        a['plant_part'] = 'Leaves'
        a['disease'] = i
        a['file_name'] = a['image']
        a['file_location'] = 'Apple2021/test_images'
        list_df.append(a)
    final_df = pd.concat(list_df, ignore_index = True)
    drop_cols = ['image','labels' ] 
    final_df = final_df.drop(columns= drop_cols)
    final_df.to_csv(csv_path + 'apple2021_meta_v1.csv', index = False)
    
def citrus():
    
    print('Creating cirtus meta version_01')
    path = '/home/Plant_Disease_DataSet/Citrus/Citrus'
    directory = extracting_directory(path)
    file = image_extraction(directory)
    
    Dataset, Plantname, imagetype, disease, imageid, location, path = [], [], [], [], [], [], []

    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))
        diseased = l.split('/')[-1]
        plantpart = l.split('/')[-2]
        plantname= l.split('/')[-3]
        dataset = l.split('/')[-3]
        path = l.split('/')[-4:]
        # path = os.path.join(dataset,plantpart,diseased)
        for k in range(len(file[i])):
            Dataset.append(dataset)
            Plantname.append(plantname)
            imagetype.append(plantpart)
            disease.append(diseased)
            location.append('/'.join(path))
        for j in file[i]:
            imageid.append(j)
        combine_details = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
    
    df = pd.DataFrame(combine_details)
    df.to_csv(csv_path + 'Citrus_meta_v1.csv', index = False)
    
def rice5932():
    print('Creating Rice5932 meta version_01')
    path = '/home/Plant_Disease_DataSet/Rice5932/Rice5932'
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    
    # Creating CSV
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-2])
            Plantname.append('Rice')
            imagetype.append('Leaves')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        combine_details = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
    df = pd.DataFrame(combine_details)
    df.to_csv(csv_path + 'rice5932_meta_v1.csv', index = False)
    

def rice1426():
    print('Creating Rice1426 meta version_01')
    path = '/home/Plant_Disease_DataSet/Rice1426/Rice1426'
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    
    # Creating CSV
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-2])
            Plantname.append('Rice')
            imagetype.append('Leaves')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        combine_details = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
    df = pd.DataFrame(combine_details)
    df.to_csv(csv_path + 'rice1426_meta_v1.csv', index = False)
    
def cgiarwheat():
    print('Creating CGIARWheat meta version_01')
    path = '/home/Plant_Disease_DataSet/CGIARWheat/CGIARWheat/train'
    directory = extracting_directory(path)
    file = image_extraction(directory)
    # Creating CSV
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        plant__part = l.split('/')[-1].split('_')[0]

        for k in range(len(file[i])):
            Dataset.append('CGIARWheat')
            Plantname.append('wheat')
            if plant__part == 'healthy':
                imagetype.append('no information')
            else:
                imagetype.append(plant__part)
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-5],l.split('/')[-4],l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        combine_details = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
    
    df = pd.DataFrame(combine_details)
    df.to_csv(csv_path + 'CGIARWheat_meta_v1.csv', index = False)

def pdd271():
    print('Creating PDD271 meta version_01')
    path = '/home/Plant_Disease_DataSet/PDD271/PDD271'
    name = pd.Series(PDD217_01)
    plantname = name.apply(extract_first_word)
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-2])
            Plantname.append(plantname[i])
            imagetype.append('Leaves')
            disease.append(PDD217_01[i])
            location.append(os.path.join(l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        dict = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
    df = pd.DataFrame(dict)
    df.to_csv(csv_path + 'PDD271_meta_v1.csv',  index = False)
    
def taiwantomato():
    print('Creating TaiwanTomato meta version_01')
    path = '/home/Plant_Disease_DataSet/TaiwanTomato/TaiwanTomato'
    directory = extracting_directory(path)
    file = image_extraction(directory)
    
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-3])
            Plantname.append('Tomato')
            imagetype.append('leaf')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-3],l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        dict = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
    }
    df = pd.DataFrame(dict)
    df.to_csv(csv_path + 'TaiwanTomato_meta_v1.csv', index= False)
    
def plant_disease_classification_merged_dataset():
    print('Creating Plant Disease Classification Merged Dataset meta version_01')
    path = '/home/Plant_Disease_DataSet/Plant Disease Classification Merged Dataset/Plant Disease Classification Merged dataset'
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    ## Extracting plant names
    plant_name = []
    for i in directory:
        plant_name.append(i.split('/')[-1].split('__')[0])
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-2])
            Plantname.append(plant_name[i])
            imagetype.append('leaf')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        combine_detail = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
    df = pd.DataFrame(combine_detail)
    df.to_csv(csv_path + 'Plant Disease Classification Merged dataset_meta_v1.csv', index = False)
    
def plant_leave_diseases_dataset_with_augmentation():
    print('Creating Plant Leaves Disease meta version_01')
    path = '/home/Plant_Disease_DataSet/Plant_leaf_diseases_dataset_with_augmentation/Plant_leave_diseases_dataset_with_augmentation'
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    # Directory processing
    joined_path = []
    for i in range(len(directory)):
            l = directory[i]
            # print(l.split('/')[2])
            dataset_name = l.split('/')[-2]
            diease_name = l.split('/')[-1]
            plant_name = diease_name.split('__')[0]
            processed_diease_name = diease_name.split('__')[-1].replace('_','',1)
            process_pah = os.path.join(dataset_name,plant_name,processed_diease_name)
            joined_path.append(process_pah)
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = joined_path[i]
        loc = directory[i]
        for k in range(len(file[i])):            
            Dataset.append(l.split('/')[0])
            Plantname.append(l.split('/')[1])
            imagetype.append('leaves')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(loc.split('/')[-3],loc.split('/')[-2],loc.split('/')[-1]))

        for j in file[i]:
            imageid.append(j)
        combine_detail = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
    df = pd.DataFrame(combine_detail)
    df.to_csv(csv_path + 'plant_leaf_diseases_dataset_augmentation_v1.csv', index = False)

def rocole_dataset():
    print('Creating Rocole Dataset meta version_01')
    path = '/home/Plant_Disease_DataSet/Rocole_dataset/RoCoLE-csv.csv'
    df = pd.read_csv(path)
    df = df.loc[:, ['Label', 'External ID']]
    #Extracting json data from label col
    label_class = []
    label_data = df['Label']
    for i in range(len(label_data)):
        label_class.append(pd.read_json(label_data[i])['classification'])
    # making list of status of the plant diseased or healthy
    label_class1 = []
    for i in range(len(label_class)):
        label_class1.append(label_class[i][0])
    # Creating dataframe
    df['Label'] = label_class1
    df['data_set'] = 'Rocole_dataset' 
    df['plant_name'] = 'Coffee'
    df['plant_part'] = 'leaf'
    df['disease'] = df['Label']
    df['file_name'] = df['External ID']
    df['file_location'] = 'Rocole_dataset/Photos'
    
    drop_col = ['Label', 'External ID']
    df = df.drop(columns= drop_col)
    
    df.to_csv(csv_path + 'Rocole_dataset_meta_v1.csv', index = False)
    
def rice_leaf_disease_dataset():
    print('Creating Rice Leaf Disease Dataset meta version_01')
    path = '/home/Plant_Disease_DataSet/Rice Leaf Diseases Dataset/rice_leaf_diseases'
    
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-2])
            Plantname.append('Rice')
            imagetype.append('leaf')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        dict = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
    }
    df = pd.DataFrame(dict)
    df.to_csv(csv_path + 'Rice_Leaf_Disease_meta_v1.csv', index= False)

def plant_leaves_image_classification():
    print('Creating Plant leaves Image Classification Dataset meta version_01')
    path = '/home/Plant_Disease_DataSet/Plant Leaves for image classification/Plant_Leaves_Image_Classification'
    directory = extracting_directory(path)
    file = image_extraction(directory)
    #EXtracting plant name
    plant_name = []
    for i in directory:
        plant_name.append(i.split('/')[-1].split()[0])
    
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-3])
            Plantname.append(plant_name[i])
            imagetype.append('leaf')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-4],l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        dict = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
    }
    df = pd.DataFrame(dict)
    df.to_csv(csv_path + 'Plant_Leaves_Image_Classification_meta_v1..csv', index = False)
   
def healthy_vs_unhealthy_leaf_image():
    print('Creating Healthy vs Unhealthy Leaf Image Dataset meta version_01')
    path = '/home/Plant_Disease_DataSet/Healthy vs Diseased leaf image dataset/healthy vs unhealthy leaf image dataset'
    directory = extracting_directory(path)
    file = image_extraction(directory)
    
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-3])
            Plantname.append(l.split('/')[-2])
            imagetype.append('Leaves or stem')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-4],l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        combine_detail = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location,
            
                }
    df = pd.DataFrame(combine_detail)
    df.to_csv(csv_path  + 'Healthy vs diseased leaf image dataset_meta_v1.csv', index = False)
    
def wheat_leaf_dataset():
    print('Creating Wheat Leaf Dataset meta version_01')
    path = '/home/Plant_Disease_DataSet/wheat_leaf_dataset/wheat_leaf'
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        # print(l.split('/'))

        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-3])
            Plantname.append('Wheat')
            imagetype.append('leaf')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        combine_detail = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
                }
        
    df = pd.DataFrame(combine_detail)
    df.to_csv(csv_path + 'wheat_Leaf_Disease_meta_v1.csv', index= False)
    
def dataset_detection_classification_guava_disease():
    print('Creating Dataset for Detection and Classification of Guava Diseases meta version_01')
    path = '/home/Plant_Disease_DataSet/Dataset for Detection and Classification of Guava Disease/Dataset for Detection and Classification of Guava Diseases'
    directory = sample_extracting_directory(path)
    file = image_extraction(directory)
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-2])
            Plantname.append('Guava')
            imagetype.append('No info')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        combine_detail = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
    }
    df= pd.DataFrame(combine_detail)
    df.to_csv(csv_path + 'Dataset for Detection and Classification of Guava Diseases_meta_v1.csv', index = False)
    
def grape_disease():
    print('Creating Dataset for Grapes Disease')
    path = '/home/Plant_Disease_DataSet/grape_disease/grape_dataset'
    directory = extracting_directory(path)
    file = image_extraction(directory)
    #EXtracting plant name
    plant_name = []
    for i in directory:
        plant_name.append(i.split('/')[-1].split("__")[0])
    ############### Creating csv ########
    Dataset, Plantname, imagetype, disease, imageid, location = [], [], [], [], [], []
    for i in range(len(directory)):
        l = directory[i]
        for k in range(len(file[i])):
            Dataset.append(l.split('/')[-3])
            Plantname.append(plant_name[i])
            imagetype.append('leaf')
            disease.append(l.split('/')[-1])
            location.append(os.path.join(l.split('/')[-4],l.split('/')[-3],l.split('/')[-2],l.split('/')[-1]))
        for j in file[i]:
            imageid.append(j)
        dict = {
                'data_set' : Dataset,
                'plant_name': Plantname,
                'plant_part' : imagetype,
                'disease' : disease,
                'file_name' :imageid,
                'file_location' : location
    }
    df = pd.DataFrame(dict)
    df.to_csv(csv_path + 'Grape_disease_meta_v1.csv', index= False)
    
def csv_version_01():
    print('Creating final CSV')
    path = '/home/Plant_Disease_DataSet/Data_Base/Meta_data_01/'
    dataset = os.listdir(path)
    final_dataset = []
    for i in dataset:
        if i == '.ipynb_checkpoints' or i == 'Untitled.ipynb':
            continue
        else:
            df = pd.read_csv(path + i)
        final_dataset.append(df)
    final_df = pd.concat(final_dataset, ignore_index = True)
    final_df.to_csv(csv_path + 'final_dataset_meta_v1.csv', index = False)
    
if __name__ == '__main__':
    try:
        plant_village()
        plant_doc()
        apple2020()
        apple2021()
        citrus()
        rice5932()
        rice1426()
        cgiarwheat()
        pdd271()
        taiwantomato()
        plant_disease_classification_merged_dataset()
        plant_leave_diseases_dataset_with_augmentation()
        rocole_dataset()
        rice_leaf_disease_dataset()
        plant_leaves_image_classification()
        healthy_vs_unhealthy_leaf_image()
        wheat_leaf_dataset()
        dataset_detection_classification_guava_disease()
        grape_disease()
        csv_version_01()
        print("CSV file saved at:", csv_path + 'plant_vilage_v1.csv')
    except Exception as e:
        print("An error occurred:", e)




