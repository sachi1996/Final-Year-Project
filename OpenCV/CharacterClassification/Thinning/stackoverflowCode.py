import cv2


BW = cv2.imread('s.png');
BWI = imcomplement(BW);
BW2D = im2bw(BWI,0.1);
BWT = bwmorph(BW2D,'thin',Inf),
BWFinal = imcomplement(BWT);
figure, imshow(BWFinal);