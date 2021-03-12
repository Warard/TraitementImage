import cv2
import time

# Paramètre de l'image
S = {
    "path": "assets/",
    "image": "feu.jpg"
}

# Charger l'image
img = cv2.imread(S['path'] + S['image'], flags=1)

def imgToGrey(img, save=False, show=True, perf=True):
    '''
        Converts a colored image to a grey one
        ARGS : 
            img : image from cv2.imread()
            save : boolean : should image be saved at the end ?
            show : boolean : should image be shown at the end ?
            perf : boolean : should running time and operation number be shown at the end ?
        RETURN : Greyscale img, type : cv2 image
    '''
    
    d, operations = time.time(), 0

    # Pour chaque ligne, 
    for i in range(img.shape[0]):
        # Pour chaque colonne
        for j in range(img.shape[1]):
            # conversion en int pour ne plus être sous 8 bits (car R G B de type u_byts scalars)
            R = int(img[i][j][2])
            G = int(img[i][j][1])
            B = int(img[i][j][0])
    
            mean = (R + G + B) // 3

            img[i][j] = mean

            operations += 1

    e = time.time()

    if save: cv2.imwrite('coloredToGrey.jpg', img)
    if perf: print(f'Color --> grey conversion executed in : {round(e - d, 2)} seconds with {operations} operations')
    if show: 
        img = cv2.resize(img, (0, 0), fx= 0.4, fy=0.4)
        cv2.imshow('test', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
    return img

imgToGrey(img, save=False, show=True, perf=True)