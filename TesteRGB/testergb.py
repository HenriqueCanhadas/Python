import cv2
import numpy as np

def create_bar(height, width, color):
    bar = np.zeros ((height,width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)


img = cv2.imread('black.jpg')

height, width, _  = np.shape(img)

print(height,width)

data = np.reshape(img, (height * width, 3))

data = np.float32(data)

number_cluster = 1
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
flags = cv2.KMEANS_RANDOM_CENTERS

compactness, labels, centers = cv2.kmeans(data, number_cluster, None, criteria, 10, flags)

print(centers)
font = cv2.FONT_HERSHEY_SIMPLEX
bars = []
rgb_values = []

for index, row in enumerate(centers):
    bar, rgb = create_bar(200, 200, row)
    bars.append(bar)
    rgb_values.append(rgb)
    
img_bar = np.hstack(bars)

for index, row in enumerate(rgb_values):
    image = cv2.putText(img_bar, f'{index + 1}. rgb:{row}', (5+200*index,200-10), 
                        font, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
    print(f'{index+1}. rgb{row}')

cv2.imshow('Image', img)
cv2.imshow("dominat colors", img_bar)

cv2.waitKey(0)




        gl.glColor3f(1.0f, 1.0f, 0.0f); // Definindo a cor amarela
        gl.glBegin(GL2.GL_TRIANGLE_FAN);
        gl.glVertex2f(0.0f, 0.0f); // Vértice central
        
        float outerRadius = 0.5f; // Raio externo
        float innerRadius = 0.2f; // Raio interno
        
        for (int i = 0; i <= 5; i++) {
            float angle = (float) (i * 2 * Math.PI / 5); // Ângulo para cada vértice
        
            // Calculando coordenadas dos vértices externos e internos
            float outerX = (float) (Math.cos(angle) * outerRadius);
            float outerY = (float) (Math.sin(angle) * outerRadius);
            float innerX = (float) (Math.cos(angle + Math.PI / 5) * innerRadius);
            float innerY = (float) (Math.sin(angle + Math.PI / 5) * innerRadius);
        
            // Desenhando os vértices
            if (i % 2 == 0) {
                gl.glVertex2f(outerX, outerY);
                gl.glVertex2f(innerX, innerY);
            } else {
                gl.glVertex2f(innerX, innerY);
                gl.glVertex2f(outerX, outerY);
            }
        }
        gl.glEnd();