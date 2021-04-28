import cv2

# Image resizing
    def Reformat_Image(self, img):
        # img_dot = cv2.imread("dot.jpg", cv2.IMREAD_COLOR)
        # gray = cv2.cv2tColor(img_dot, cv2.COLOR_BGR2GRAY)
        # ret, th1 = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)
        # Load the image
        img = Image.fromarray(cv2.cv2tColor(img, cv2.COLOR_BGR2RGB))
        img_w, img_h = img.size
        background = Image.new('RGB', (200, 200), (255, 255, 255, 255))
        bg_w, bg_h = background.size
        offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
        background.paste(img, offset)
        # Converting Image to the opencv2 format(BGR)
        open_cv2_image = np.array(background)
        # Convert RGB to BGR
        open_cv2_image = open_cv2_image[:, :, ::-1].copy()
        if self.no_of_contours(open_cv2_image) == 1:
            # Getting smallest square contour character
            cropped_img = self.char_contour(None, open_cv2_image)
        elif self.no_of_contours(open_cv2_image) > 1:
            teimg = self.morph(open_cv2_image)
            cropped_img = self.char_contour(teimg, open_cv2_image)
        else:
            cropped_img = self.char_contour(None, open_cv2_image)

        # Resizing image to 50*50 resolution
        width = 50
        height = 50
        dim = (width, height)

        # resize image
        if cropped_img is None:
            return -1
        else:
            resized = cv2.resize(cropped_img, dim, interpolation=cv2.INTER_AREA)

        return resized