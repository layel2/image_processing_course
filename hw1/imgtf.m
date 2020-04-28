clc;
clf;
clear all;
img_path = '.\image\beach_m_b.jpg';
img = imread(img_path);
img = rgb2gray(img);
%img = logical(img);
simg = size(img);
img = img(:);
for i=1:size(img)
    if(img(i)<128)
        img(i) = 0;
    elseif(img(i)>=128)
        img(i) = 255;
    end
end
limg1 = reshape(logical(img),simg(1),simg(2));

img_path = '.\image\beach_m_tree.jpg';
img = imread(img_path);
img = rgb2gray(img);
%img = logical(img);
simg = size(img);
img = img(:);
for i=1:size(img)
    if(img(i)<128)
        img(i) = 0;
    elseif(img(i)>=128)
        img(i) = 255;
    end
end
limg2 = reshape(logical(img),simg(1),simg(2));

img_path = '.\image\beach_m_ss.jpg';
img = imread(img_path);
img = rgb2gray(img);
%img = logical(img);
simg = size(img);
img = img(:);
for i=1:size(img)
    if(img(i)<128)
        img(i) = 0;
    elseif(img(i)>=128)
        img(i) = 255;
    end
end
limg3 = reshape(logical(img),simg(1),simg(2));

limg1 = limg1(:);
limg2 = limg2(:);
limg3 = limg3(:);

gt = zeros(size(img));
for i=1:size(img)
    if(limg1(i)==0)
        gt(i)=0;
    elseif(limg2(i)==0)
        gt(i)=1;
    elseif(limg3(i)==0)
        gt(i)=2;
    end
end


