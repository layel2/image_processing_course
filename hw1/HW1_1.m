clc;
clf;
clear all;
img_path = '.\tower.jpg';
img = imread(img_path);
img = rgb2gray(img);
%level = graythresh(img)
BW = imbinarize(img,0.6);
imshowpair(img,BW,'montage');
%figure;
%imshow(uint8(BW).*img);
