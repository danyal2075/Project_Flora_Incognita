import sys
import argparse
import numpy as np
import torch
import os
from torch.utils.data import DataLoader, SubsetRandomSampler
import pandas as pd
import matplotlib.pyplot as plt
import PIL
import torchvision.transforms as transform
from torchvision.datasets import ImageFolder
import time
from tqdm import tqdm
from sklearn.model_selection import StratifiedKFold, KFold
import torch.optim as optim
from torchvision import models
import torch.nn as nn

class EarlyStopping:
    def __init__(self, patience):
        self.pateince  = patience
        self.best_score = None
        self.counter = 0
        self.stop  = False
    def _stopping(self,val_loss):
        if self.best_score is None:
            self.best_score = val_loss
        elif val_loss > self.best_score:
            self.counter += 1
            if self.counter == self.pateince:
                self.stop = True
        else:
            self.best_score = val_loss
            # print(self.best_score)
            counter = 0

def model(batch_size, learning_rate, model):
    # NewPlantDiease/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)/train
    path = '/home/NewPlantDiease/new plant diseases dataset(augmented)/New Plant Diseases Dataset(Augmented)'
    train_data_path = path + '/train'
    val_data1 = path + '/valid'
    # diease = os.listdir(train_data1)
    mean = [0.4757, 0.5001, 0.4264]
    std = [0.2165, 0.1957, 0.2320]
    Batch_size = batch_size
    Learning_rate = learning_rate
    Model = model
    print(Model,'having Batch_Size of', Batch_size, 'and Learning_Rate', Learning_rate)

    transforms = transform.Compose([transform.Resize((256,256)), transform.ToTensor(), transform.Normalize(mean = mean, std= std)])
    val_datasets = ImageFolder(root = train_data_path, transform=transforms)
    train_data1 = int(0.25 * len(val_datasets))
    testing_data1 = len(val_datasets) - train_data1
    train_set1, val_set1 = torch.utils.data.random_split(val_datasets, [train_data1, testing_data1])
    kfold = KFold(n_splits=4)
    avg_train_acc = []
    avg_test_acc = []
    avg_train_loss = []
    avg_test_loss = []
    for fold, (train_ids, test_ids) in enumerate(kfold.split(train_set1)):
        print('*********************',fold)
        train_sampler = SubsetRandomSampler(train_ids)
        test_sampler = SubsetRandomSampler(test_ids)
        Train_dataloader = DataLoader(train_set1, batch_size = Batch_size, sampler = train_sampler)
        Val_dataloader = DataLoader(train_set1, batch_size = Batch_size, sampler = test_sampler)

        # Creating model
        model = models.resnet18(pretrained=True).cuda()
        # Freeze all parameters in the pre-trained model
        for param in model.parameters():
            param.requires_grad = True
        # Extracting features from last CNN layer
        num_features = model.fc.in_features
        model.fc = nn.Linear(num_features , 38).cuda()
        # optimizer and loss function
        optimizer = optim.Adam(model.parameters(), lr = learning_rate)
        loss_function = nn.CrossEntropyLoss()
        earlystopping = EarlyStopping(patience=5)

        for epoch in range(10):
            start = time.time()

            tr_acc = 0
            val_acc = 0

            # Train
            model.train()
            with tqdm(total=len(Train_dataloader)) as pbar:
                for xtrain, ytrain in Train_dataloader:
                    xtrain, ytrain = xtrain.cuda(), ytrain.cuda() 
                    train_prob = model(xtrain)
                    train_loss = loss_function(train_prob, ytrain)
                    train_loss.backward() # backpropagation
                    optimizer.step() # update the model parameters
                    optimizer.zero_grad()
                    train_pred = torch.max(train_prob, 1).indices
                    tr_acc += int(torch.sum(train_pred == ytrain))
                    pbar.set_postfix(tr_acc = tr_acc, train_loss = train_loss)
                    pbar.update(n=1)
                ep_tr_acc = tr_acc / len(train_ids)

            end = time.time()
            duration = (end - start) / 60

            model.eval()
            with torch.no_grad():
                for xval, yval in Val_dataloader:
                    xval, yval = xval.cuda(), yval.cuda()
                    val_prob = model(xval)
                    val_loss = loss_function(val_prob , yval)
                    val_pred = torch.max(val_prob,1).indices
                    val_acc += int(torch.sum(val_pred == yval))
                ep_val_acc = val_acc / len(test_ids)

            earlystopping._stopping(val_loss)
            if earlystopping.stop:
                print('Early Stopping Executed')
                break

            end = time.time()
            duration = (end - start) / 60

            print(f"Epoch: {epoch}, Test_Loss: {train_loss}, Validation_loss: {val_loss}, Train_acc: {ep_tr_acc}, Val_acc: {ep_val_acc}")

        avg_train_acc.append(ep_tr_acc)
        avg_test_acc.append(ep_val_acc)
        avg_train_loss.append(train_loss.detach().item())
        avg_test_loss.append(float(val_loss.item()))
        print('Append list is printing')
        print(avg_train_acc, avg_test_acc, avg_test_loss, avg_train_loss)

    return avg_train_acc, avg_test_acc, avg_train_loss, avg_test_loss

# arg1 = int(sys.argv[1])
# arg2 = float(sys.argv[2])
# arg3 = sys.argv[3]

# avg_train_acc, avg_test_acc, avg_train_loss, avg_test_loss = model(arg1, arg2, arg3)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('Batch_Size', type = int)
    parser.add_argument('Learning_Rate', type = float)
    parser.add_argument('Model_Name', type = str)
    
    args = parser.parse_args()
    avg_train_acc, avg_test_acc, avg_train_loss, avg_test_loss = model(args.Batch_Size, args.Learning_Rate, args.Model_Name)
