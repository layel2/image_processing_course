clc;
clf;
close all;
clear all;
img_path = '.\image\slipper.jpg';
img = imread(img_path);
img = rgb2gray(img);
%img = imresize(img,0.5);
%img = 255-img;
imshow(img);
mask = zeros(size(img));
mask(60:end-50,170:end-90) = 1;
figure
imshow(mask)
title('Initial Contour Location')
bw = activecontour(img,mask,1000);
figure
imshow(bw)
title('Segmented Image')
figure
imshow(uint8(bw).*img)