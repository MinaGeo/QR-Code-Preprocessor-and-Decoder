import cv2
import numpy as np
import matplotlib.pyplot as plt


def image_pre_processing(img_address):
    img = cv2.imread(img_address, cv2.IMREAD_GRAYSCALE)
    # cv2.imshow("img", img)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    fig = plt.figure(figsize=(5, 5))
    plt.xticks([], [])
    plt.yticks([], [])
    plt.title('Example QR code')
    plt.imshow(img, cmap='gray')
    detecting_area_of_qr(img)


def get_qr_without_quiet_zone(img, start_row, end_row, start_col, end_col):
    qr_no_quiet_zone = img[start_row:end_row, start_col:end_col]
    fig = plt.figure(figsize=(5, 5))
    plt.xticks([], [])
    plt.yticks([], [])
    fig.get_axes()[0].spines[:].set_color('red')
    fig.get_axes()[0].spines[:].set_linewidth(40)
    fig.get_axes()[0].spines[:].set_position(("outward", 20))
    plt.title('QR code without quiet zone', y=1.15, color='red')
    plt.imshow(qr_no_quiet_zone, cmap='gray')
    plt.show()


def detecting_area_of_qr(img):
    start_row = -1
    start_col = -1
    end_row = -1
    end_col = -1

    for row_index, row in enumerate(img):
        for pixel in row:
            if pixel != 255:
                start_row = row_index
                break
        if start_row != -1:
            break

    for row_index, row in enumerate(img[::-1]):
        for pixel in row:
            if pixel != 255:
                end_row = img.shape[0] - row_index
                break
        if end_row != -1:
            break

    for col_index, col in enumerate(cv2.transpose(img)):
        for pixel in col:
            if pixel != 255:
                start_col = col_index
                break
        if start_col != -1:
            break

    for col_index, col in enumerate(cv2.transpose(img)[::-1]):
        for pixel in col:
            if pixel != 255:
                end_col = img.shape[1] - col_index
                break
        if end_col != -1:
            break

    print(start_row, end_row, start_col, end_col)
    get_qr_without_quiet_zone(img, start_row, end_row, start_col, end_col)


img_address = "01-Getting-started.png"
image_pre_processing(img_address)
