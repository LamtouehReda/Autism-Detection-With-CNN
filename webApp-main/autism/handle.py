# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.transform import resize
#
# def rgb2gray(I):
#     r, g, b = I[:,:,0], I[:,:,1], I[:,:,2]
#     gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
#     return gray
#
# def stocker_images(nbr_im):
#     mat_image=np.zeros((500,500,nbr_im*2))
#     k=0
#     for j in ["Autistic","Non_Autistic"]:
#         for i in range(nbr_im):
#             filename2 = './AutismDataset/testSmall/'+j+'.'+str(i)+'.jpg'
#             mat_image[:,:,k] = resize(rgb2gray(plt.imread(filename2)), (500,500),anti_aliasing=True)
#             k+=1
#     return mat_image
#
#
# def variance(I):
#     nl,nc=I.shape
#     m=np.mean(I)
#     va=np.sum((I-m)**2)/(nl*nc)
#     return va
#
# def energie(I):
#     nl,nc=I.shape
#     en= np.sum(I**2)
#     return en
#
# def entropie(I):
#     ent=np.sum(I*np.log2(I+1e-10))
#     return -ent
#
# def contraste(I):
#     nl,nc=I.shape
#     co=0
#     for i in range(nl):
#         for j in range(nc):
#             co+=np.power((i-j),2)*I[i,j]
#     return co
#
# def homogenite(I):
#     nl,nc=I.shape
#     mo=0
#     for i in range(nl):
#         for j in range(nc):
#             mo+=I[i,j]*(1/(1+np.abs(i-j)))
#     return mo
#
# def histo(I):
#     [nl,nc]=np.shape(I)
#     h=np.zeros(256)
#     I_m=np.round(I)
#     for i in range(0,nl):
#         for j in range(0,nc):
#             val=int(I_m[i][j])
#             h[val]+=1
#     return h
#
# def histoN(I):
#     [nl,nc]=np.shape(I)
#     h=histo(I)
#     return h/(nl*nc)
#
# def histc(I):
#     a=histo(I)
#     b=np.zeros(256)
#     b[0]=a[0]
#     for i in range(1,len(a)):
#         b[i]=b[i-1]+a[i]
#     return b
#
# def colorMoy(rgb):
#     nr,nc=rgb2gray(rgb).shape
#     r,g,b=rgb[:,:,0],rgb[:,:,1],rgb[:,:,2]
#     return np.array([np.mean(r),np.mean(g),np.mean(b)])
#
#
# # def co_occurence(I):
# #     (l, c) = I.shape
# #     m = int(np.max(I))
# #     C = np.zeros((m + 1, m + 1))
# #
# #     for i in range(m + 1):
# #         for j in range(m + 1):
# #             cmp = 0
# #             # this loop will calculate each pair occurence
# #             for k in range(l):
# #                 for h in range(c - 1):
# #                     if I[k, h] == i and I[k, h + 1] == j:
# #                         cmp += 1
# #             C[i, j] = cmp
# #     return C
#
# def co_occurence(m):
#     M = m.astype(int)
#     co = np.zeros((256,256))
#     for i in range(M.shape[0]):
#         for j in range(M.shape[1]-1):
#             co[M[i,j],M[i,j+1]] +=1
#     return co/np.max(co)
#
# def stocker_desc(mat_image,descripteur):
#     nl,nc,nbr_img=mat_image.shape
#     if descripteur in ['histo','histoN','histc']:
#         columns=256
#     if descripteur=='texture':
#         columns=5
#     if descripteur=='colorMoy':
#         columns=3
#
#     desc=np.zeros((nbr_img,columns))
#     for i in range(nbr_img):
#         if descripteur=='histo':
#             desc[i,:]=histo(mat_image[:,:,i])
#         if descripteur=='histoN':
#             desc[i,:]=histoN(mat_image[:,:,i])
#         if descripteur=='histc':
#             desc[i,:]=histc(mat_image[:,:,i])
#         if descripteur=='texture':
#             desc[i,:]=np.array([variance(mat_image[:,:,i]),energie(mat_image[:,:,i]),
#                     entropie(mat_image[:,:,i]),contraste(mat_image[:,:,i]),
#                     homogenite(mat_image[:,:,i])])
#         if descripteur=='colorMoy':
#             if i<=32:
#                 I=plt.imread('./AutismDataset/testSmall/Autistic.'+str(i)+'.jpg')
#             else:
#                 I = plt.imread('./AutismDataset/testSmall/Non_Autistic.' + str(i-33) + '.jpg')
#             desc[i,:]=colorMoy(I)
#
#     return desc
#
# def distanceE(x,y):
#     return np.sqrt(np.sum(np.power(x-y,2)))
# def distancem(x,y):
#     return np.sqrt(np.sum(np.abs(x-y)))
#
# def proch(img_path, mat_image, distance, descripteur,stocked_desc):
#     nr, nc, nbr_img = mat_image.shape
#     I = plt.imread(img_path)
#     gray = resize(rgb2gray(plt.imread(img_path)), (500, 500), anti_aliasing=True)
#
#     if descripteur == 'histo':
#         h = histo(gray)
#
#     elif descripteur == 'histoN':
#         h = histoN(gray)
#
#     elif descripteur == 'histc':
#         h = histc(gray)
#
#     elif descripteur == 'texture':
#         h = np.array([variance(gray), energie(gray),
#                       entropie(gray), contraste(gray),
#                       homogenite(gray)])
#
#     elif descripteur == 'colorMoy':
#         h = colorMoy(I)
#
#
#     desc = stocked_desc[descripteur]
#     D = []
#     for i in range(nbr_img):
#         if distance == 'euclidienne':
#             d = distanceE(h, desc[i, :])
#
#         if distance == 'manhattan':
#             d = distancem(h, desc[i, :])
#
#         D.append([d, i + 1])
#
#     return sorted(D)
#
#
# def classe(D):
#     if D[1][1]>=1 and D[1][1]<33:
#         return 'Autiste'
#     else:
#         return 'Non Autiste'
#
#
# def test(img_path,mat_image,distance,descripteur):
#     D=proch(img_path,mat_image,distance,descripteur,stocked_desc)
#     return classe(D)
#
# mat_image = stocker_images(10)
# descripteurs = ['histo', 'histoN', 'texture', 'colorMoy', 'co_occurence']
# stocked_desc = {}
# for desc in descripteurs:
#     stocked_desc[desc] = stocker_desc(mat_image, desc)