# Michelle Cui
# This program calculates the rectangular prism's surface area
# 0ctober 15

def printInstructions():
    '''
    This is for the instructions of this program.
    '''
    print("This program can help you to calculate the surface area of a rectangular prism.")
    print("Please enter the Length, Width and the Height.")

def printLength():
    '''
    This is the step to get the number of length and return it
    :return: length
    '''
    length = input("Enter length: ")
    return float(length)


def printwidth():
    '''
    This is the step to get the number of width and return it
    :return: width
    '''
    width = input("Enter width: ")
    return float(width)


def printheight():
    '''
    This is the step to get the number of height and return it
    :return: height
    '''
    height = input("Enter height: ")
    return float(height)

def surfacearea(L, W, H):
    '''
    This is the step to calculate the surface area out.
    :param L: length
    :param W: width
    :param H: height
    :return: main surface area
    '''
    area = 2 * L * W + 2 * L * H + 2 * W * H
    return area

def printresult(result):
    '''
    This is the step to print the result out.
    :param result: the final surface area
    '''
    print("The rectangular prism's surface area is", result)

def main():
    printInstructions()
    L = printLength()
    W = printwidth()
    H = printheight()
    result = surfacearea(L, W, H)
    printresult(result)

main()

