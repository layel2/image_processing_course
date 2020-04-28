<<<<<<< HEAD
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
=======
clc;
clf;
clear all;
img_path = '';
img = imread('E:\film\tmax400-2-10\181205000250550011.jpg');
img = rgb2gray(img);
%level = graythresh(img)
BW = imbinarize(img,0.95);
BW = uint8(~BW);
img2 = BW.*img;
%imshow(BW.*img);
BW2 = imbinarize(img2,0.4);
BW2 = uint8(BW2);
>>>>>>> 18619402270a206486e7d4637fff88e2d1e13d38
imshowpair(img,BW2,'montage');