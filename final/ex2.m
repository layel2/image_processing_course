clc;
close all;
clf;
clear all;
img_path = '.\Problem2_1.bmp';
img = imread(img_path);
img = rgb2gray(img);
imshow(img);
mask = zeros(size(img));
mask(end/2:end-20,50:end-30) = 1;
figure
imshow(mask)
title('Initial Contour Location')
bw = activecontour(img,mask,15000,'edge','SmoothFactor',3);
figure
imshow(bw)
title('Segmented Image')
figure
imshow(uint8(bw).*img)
bw = bw*255;