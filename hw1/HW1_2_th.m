clc;
clf;
close all;
clear all;
img_path = '.\image\slipper.jpg';
img = imread(img_path);
img = rgb2gray(img);
BW = imbinarize(img,200/255);
img2 = img.*uint8(BW);
BW2 = imbinarize(img,150/255);
img3 = img.*uint8(~BW2);
imhist(img3+img2)
figure
imshow(img3+img2)
