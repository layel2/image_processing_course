clc;
clf;
close all;
clear all;
img_path = '';
img = imread('.\image\gundum.jpg');
img = rgb2gray(img);
%level = graythresh(img)
BW = imbinarize(img,0.9);
BW = uint8(~BW);
img2 = BW.*img;
imshow(img2)
figure
%imshow(BW.*img);
BW2 = imbinarize(img2,0.2);
BW2 = uint8(BW2);
imshowpair(img,BW2,'montage');