import cv2
import numpy as np
import os

def process_image(image_name, output_name="result.jpg"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    image_path = os.path.join(script_dir, image_name)
    output_path = os.path.join(script_dir, output_name)

    image = cv2.imread(image_path)
    if image is None:
        print(f"Ошибка: Не удалось загрузить изображение по пути: {image_path}")
        return

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 100:
            continue

        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

    cv2.imwrite(output_path, image)
    print(f"Обработка завершена. Результат сохранен в {output_path}")

process_image("test.jpg")