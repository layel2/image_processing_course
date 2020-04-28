import numpy as np
import cv2
from skimage import feature
import os
from mahotas.features import zernike_moments

class getdata():
	def __init__(self,data_path,label_path):
		self.dataPath = data_path
		self.labelPath = label_path
		data_file = np.array(sorted(os.listdir(data_path)))
		if(data_file[0] =='.DS_Store'):
			data_file = data_file[1:]
		self.dataFile = data_file
		self.label = np.genfromtxt('./data_fall/labels.csv',delimiter=',')[1:][:,1]
		class_45 = np.concatenate([np.where(self.label == 4)[0],np.where(self.label==5)[0]])
		self.dataFile = np.delete(self.dataFile,class_45,axis=0)
		self.label = np.delete(self.label,class_45,axis=0)
		self.n_index = len(self.dataFile)
		
		if len(self.label) != len(self.dataFile):
			print("Error Length data != label")
	
	def get1img(self,img_index,mode='rgb'):
		img = cv2.imread( os.path.join(self.dataPath,self.dataFile[img_index]) )
		if mode == 'rgb':
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		elif mode == 'gray':
			img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		return img

	def feature_7HU(self,mode = 'all',index=None,outimg=None):
		if mode=='all':
			output = []
			for i in range(self.n_index):
				temp_img = self.get1img(i,'gray')
				output.append( cv2.HuMoments(cv2.moments(temp_img)).flatten() )

			return np.array(output)
		elif mode=='single':
			if index == None and outimg is None:
				print("please input index")
				return
			if outimg is None:
				temp_img  = self.get1img(index,'gray')
			else :
				temp_img = outimg
			return cv2.HuMoments(cv2.moments(temp_img)).flatten()

	def feature_lbp(self,mode = 'all',index=None,outimg=None):
		radius = 8
		n_point = 8*radius
		if mode=='all':
			out_ben = []
			for i in range(self.n_index):
				temp_img = self.get1img(i,'gray')
				temp_lbp = feature.local_binary_pattern(temp_img,n_point,radius,'uniform')
				out_ben.append(np.histogram(temp_lbp.ravel(),bins=n_point+1)[0])
			return np.array(out_ben)
		elif mode=='single':
			if index == None and outimg is None:
				print("please input index")
			if outimg is None:
				temp_img = self.get1img(index,'gray')
			else :
				temp_img = outimg
			temp_lbp = feature.local_binary_pattern(temp_img,n_point,radius,'uniform')
			return np.histogram(temp_lbp.ravel(),bins=n_point+1)[0]
		
	def feature_hog(self,mode = 'all',index=None):
		if mode=='all':
			out_ben = []
			for i in range(self.n_index):
				temp_img = self.get1img(i,'rgb')
				temp_hog = feature.hog(temp_img,orientations=4,pixels_per_cell=(8, 8),cells_per_block=(1,1))
				out_ben.append(temp_hog)
			return np.array(out_ben)
		elif mode=='single':
			if index == None:
				print("please input index")
			temp_img = self.get1img(index,'rgb')
			temp_hog,hog_img = feature.hog(temp_img,orientations=4,pixels_per_cell=(8, 8),cells_per_block=(1,1),visualize=True)
			return temp_hog,hog_img

	def feature_zernike(self,mode = 'all',index=None,outimg=None):
		if mode=='all':
			output = []
			for i in range(self.n_index):
				temp_img = self.get1img(i,'gray')
				output.append( zernike_moments(temp_img,1) )

			return np.array(output)
		elif mode=='single':
			if index == None and outimg is None:
				print("please input index")
				return
			if outimg is None:
				temp_img  = self.get1img(index,'gray')
			else :
				temp_img = outimg
			return zernike_moments(temp_img,1)

	def feature_coMat(self,mode = 'all',index=None,distances=[10],angles=[0, np.pi/4, np.pi/2, 3*np.pi/4]):
		if mode=='all':
			output = []
			for i in range(self.n_index):
				temp_img = self.get1img(i,'gray')
				temp_comat = feature.greycomatrix(temp_img,distances, angles)
				en = feature.greycoprops(temp_comat,'energy')
				const = feature.greycoprops(temp_comat,'contrast')
				coore = feature.greycoprops(temp_comat,'correlation')
				output.append( np.concatenate([en,const,coore]).reshape((-1)) )

			return np.array(output)
		elif mode=='single':
			if index == None:
				print("please input index")
				return
			temp_img  = self.get1img(index,'gray')
			temp_comat = feature.greycomatrix(temp_img,distances, angles)
			en = feature.greycoprops(temp_comat,'energy')
			const = feature.greycoprops(temp_comat,'contrast')
			coore = feature.greycoprops(temp_comat,'correlation')
			return np.concatenate([en,const,coore]).reshape((-1)) 


def data_div(data,label):
	n_label = np.unique(label)
	f_data = []
	for i,lab in enumerate(n_label):
		f_data.append(data[np.where(label==lab)[0]])
	f_data = np.array(f_data)

	n_feature = data.shape[1]
	feature_min_max = []
	for i in range(n_feature):
		feature_min_max.append((data[:,i].min(),data[:,i].max()))
	feature_min_max = np.array(feature_min_max)
	D = 0

	for i,_ in enumerate(n_label):
		for j,_ in enumerate(n_label):
			if(i!=j):
				temp_d = diver(f_data[i],f_data[j],n_feature,feature_min_max)
				D += temp_d
				print(f"D{i}{j} = {temp_d}")


	return D

def diver(a,b,n_feature,feature_min_max):
	D = 0
	for i in range(n_feature):
		d1 = a[:,i]
		d2 = b[:,i]
		bins = np.linspace(feature_min_max[i][0],feature_min_max[i][1],30)
		p1 = np.histogram(d1,bins=bins)[0]/len(d1)
		p2 = np.histogram(d2,bins=bins)[0]/len(d2)
		D += np.sum(np.where(np.logical_and(p1 != 0,p2!=0), p1 * np.log(p1/p2),0))
	return D

def J3scatterMat(data,label):
	n_label = np.unique(label)
	n_feature = data.shape[1]
	f_data = []
	m = []
	prob = []
	for i,lab in enumerate(n_label):
		f_data.append(data[np.where(label==lab)[0]])
		m.append(data[np.where(label==lab)[0]].mean(axis=0))
		prob.append( len(f_data[i])/len(data) )
	f_data = np.array(f_data)
	m = np.array(m)
	prob = np.array(prob)

	in_class = np.zeros((n_feature,n_feature))
	for i,_ in enumerate(n_label):
		for j in range(len(f_data[i])):
			temp_mat = (f_data[i][j,:] - m[i]).reshape(-1,1)      
			in_class += prob[i]*temp_mat.dot(temp_mat.T)

	bet_class = np.zeros((n_feature,n_feature))
	m_0 = np.sum(prob.reshape(-1,1)*m,axis=0)
	for i,_ in enumerate(n_label):
		temp_mat = (m[i]-m_0).reshape(-1,1)
		bet_class += prob[i]*(temp_mat.dot(temp_mat.T))
	return np.trace(np.linalg.inv(in_class)@(in_class+bet_class))

def fdr(data,label):
	n_label = np.unique(label)
	n_feature = data.shape[1]
	f_data = []
	m = []
	var = []
	for i,lab in enumerate(n_label):
		f_data.append(data[np.where(label==lab)[0]])
		m.append(data[np.where(label==lab)[0]].mean(axis=0))
		var.append( data[np.where(label==lab)[0]].std(axis=0) )
	f_data = np.array(f_data)
	n_class = len(f_data)
	fisher_sum = 0
	fisher_c = []
	for i in range(n_class-1):
		for j in range(i+1,n_class):
			fisher_temp = ((m[i]-m[j])**2/(var[0]**2 + var[1]**2))
			fisher_c.append(fisher_temp.sum())
			fisher_sum += fisher_temp.sum()

	return fisher_sum,fisher_c

def train_test_split(data,ratio=0.7,idx=None):
	if (idx != None).all:
		data = data[idx]
	n_split = int(len(data)*ratio)
	train_data = data[:n_split]
	test_data = data[n_split:]

	return train_data,test_data

def print_class_sep(data,label):
	print("--Divergence--")
	print(f"Divergence = {data_div(data,label)}")
	print(f"Scatter Matrix J3 = {J3scatterMat(data,label)}")
	fisher = fdr(data,label)
	print(f"Fisher discriminant ratio = {fisher[0]}")
	print(f"(fisher class1,2 = {fisher[1][0]}),class1,3 = {fisher[1][1]}),class2,3 = {fisher[1][2]})")



