import ocr
import cv2


def parse_img(path, draw):
    cropped = cv2.imread(path)

    h, w, _ = cropped.shape

    cropped = cv2.resize(cropped, (w * 2, h * 2))
    cropped = cv2.detailEnhance(cropped, sigma_s=60, sigma_r=1.2)
    cropped = cv2.resize(cropped, (600, 1200))

    text = ocr.recog(cropped)

    # parse output
    lines = text.split("\n")

    parsed = {}
    for line in lines:

        # use no spaces for logic
        no_spaces = line.replace(" ", "")
        if no_spaces != "":  # checks for empty strinmgs or empty strings with spaces
            if "=" in no_spaces or "-" in no_spaces or ":" in no_spaces:
                sides = []
                if "=" in line:
                    sides = line.split("=")
                elif "-" in line:
                    sides = line.split("-")
                elif ":" in line:
                    sides = line.split(":")

                if not ("" in sides):

                    # print(sides)
                    stripped = []
                    for side in sides:
                        stripped.append(side.strip())
                    parsed[stripped[0]] = stripped[1]

                # parsed.append(line)
    if draw:
        display(cropped)
    return parsed


def display(img):
    cv2.imshow("Screen", img)

    if cv2.waitKey(0) == ord("q"):
        cv2.destroyAllWindows()
