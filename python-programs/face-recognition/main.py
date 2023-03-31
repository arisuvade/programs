import cv2
import pathlib


def main():
    c_path = (
        pathlib.Path(cv2.__file__).parent.absolute()
        / "data/haarcascade_frontalface_default.xml"
    )
    clf = cv2.CascadeClassifier(str(c_path))
    camera = cv2.VideoCapture(0)

    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        for (x, y, width, height) in face:
            cv2.rectangle(
                frame,
                (x, y),
                (x + width, y + height),
                (0, 255, 255),
                2,
            )

        cv2.imshow("Faces", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
