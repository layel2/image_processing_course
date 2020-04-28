<<<<<<< HEAD
clc;
clf;
close all;
clear all;
img_path = '.\image\tower2.jpg';
img = imread(img_path);
img = rgb2gray(img);
hand_mask = load('.\tower_m.mat');
hand_mask = hand_mask.limg;
%level = graythresh(img)
BW1 = imbinarize(img,150/255);
BW2 = imbinarize(img,175/255);
BW3 = imbinarize(img,200/255);
subplot(221)
imshow(BW1)
title('Threshold = 150');
subplot(222)
imshow(BW2)
title('Threshold = 175');
subplot(223)
imshow(BW3)
title('Threshold = 200');
subplot(224)
imshow(hand_mask)
title('Manual Mask');
confusionmat(hand_mask(:),BW1(:))
confusionmat(hand_mask(:),BW2(:))
confusionmat(hand_mask(:),BW3(:))

%imshowpair(img,BW,'montage');
%figure;
%imshow(uint8(BW).*img);
=======
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
>>>>>>> 18619402270a206486e7d4637fff88e2d1e13d38
