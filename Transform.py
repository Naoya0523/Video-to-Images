try:
    import cv2
except ImportError:
    print("'Import Error': Please install openCV library -> !pip install opencv-python")


#video name
videoname = "sample.mp4" #please write your video name

video_path = "videos/" + videoname


def video_to_images(video_path):

    print('processing...')

    cap = cv2.VideoCapture(video_path)
    num = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            filepath = "Images/img_" + str(num) + ".jpg"
            cv2.imwrite(filepath, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("canceled")
                break
        else:
            break

        num += 1

    cap.release()
    cv2.destroyAllWindows()

    print('completed!')

if __name__ == '__main__':
    video_to_images(video_path)