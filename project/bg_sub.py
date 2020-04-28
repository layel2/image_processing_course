import cv2
from utils import *

data_path = './data_fall/rgb/'
data_file = np.array(sorted(os.listdir(data_path)))
proj = getdata(data_path,'./data_fall/labels.csv')

#subtrac = cv2.createBackgroundSubtractorKNN(dist2Threshold=1000,detectShadows=True)
subtrac = cv2.createBackgroundSubtractorMOG2(history=500,varThreshold=50,detectShadows=False)
#subtrac.setShadowThreshold(50)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('./output/output_bg_MOG2.avi',fourcc, 60, (320,240))
for i in range(proj.n_index):
	frame = proj.get1img(i,mode='df')

	mask = subtrac.apply(frame)
	#fmask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
	#out.write(fmask)

	cv2.imshow('vid',frame)
	cv2.imshow('mask',mask)
	key = cv2.waitKey(30)
	if key==27:
		break
out.release()
