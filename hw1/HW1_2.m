<<<<<<< HEAD
clc;
close all;
clf;
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
bw = activecontour(img,mask,10000,'edge','SmoothFactor',3);
figure
imshow(bw)
title('Segmented Image')
figure
=======
clc;
close all;
clf;
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
bw = activecontour(img,mask,10000,'edge','SmoothFactor',3);
figure
imshow(bw)
title('Segmented Image')
figure
>>>>>>> 18619402270a206486e7d4637fff88e2d1e13d38
imshow(uint8(bw).*img)