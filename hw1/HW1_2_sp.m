clc;
close all;
clf;
clear all;
img_path = '.\image\slipper.jpg';
img = imread(img_path);
img = rgb2gray(img);
[L,N] = superpixels(img,700);
figure
BW = boundarymask(L);
imshow(imoverlay(img,BW,'cyan'),'InitialMagnification',67)
outputImage = zeros(size(img),'like',img);
idx = label2idx(L);
numRows = size(img,1);
numCols = size(img,2);
for labelVal = 1:N
    redIdx = idx{labelVal};
    outputImage(redIdx) = mean(img(redIdx));
end    

figure
imshow(outputImage,'InitialMagnification',67)
mask = zeros(size(img));
mask(60:end-50,170:end-90) = 1;
figure
imshow(mask)
title('Initial Contour Location')
bw = activecontour(outputImage,mask,1000);