clc;
close all;
clf;
clear all;
img_path = '.\mk.jpg';
img = imread(img_path);
img = rgb2gray(img);
imshow(img);
figure
imhist(img);
simg = size(img);
img = img(:);
k = 2;
km = kmeans(img,k);
km = reshape(km,simg(1),simg(2));
km = uint8(km);
figure
imshow((km-1)*(255/(k-1)));