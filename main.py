import cv2

path =cv2.imread('/Users/yarenkarabacak/Desktop/cicek2.jpg')
cv2.imshow('image', path)

b, g, r =cv2.split(path)
cv2.imshow("Model blue image", b)
cv2.imshow("Model green image", g)
cv2.imshow("Model red image", r)
print(r)


print(path.shape)
for i in range(0,1024):
    for a in range(0,768):
        if r[i,a] > 100:
            r[i,a] = 10

merged = cv2.merge([b,g,r])
cv2.imshow("Merged", merged)

cv2.waitKey(0)




