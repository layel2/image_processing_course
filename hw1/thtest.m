clc;
close all;
clf;
clear all;
img_path = '.\slipper.jpg';
img = imread(img_path);
img = rgb2gray(img);
%level = graythresh(img)
BW = imbinarize(img,0.5);
imshowpair(img,BW,'montage');
figure;
imshow(uint8(BW).*img);
