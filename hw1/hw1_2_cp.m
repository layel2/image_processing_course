basem = load('slipper_m.mat');
basem = basem.limg;
bwsf3 = load('edgeI10SF3.mat');
bwsf3 = bwsf3.bw;
bwsf35 = load('edgeI15SF35.mat');
bwsf35 = bwsf35.bw;
bwsf4 = load('edgeI20SF40.mat');
bwsf4 = bwsf4.bw;

confusionmat(~basem(:),~bwsf3(:))
confusionmat(~basem(:),~bwsf35(:))
confusionmat(~basem(:),~bwsf4(:))