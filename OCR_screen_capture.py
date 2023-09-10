from pynput import mouse
import pyautogui
import time
import cv2
import pytesseract

click_count = 0
print("WELCOME TO OCR SCREEN CAPTURE !!! (Convert text from image)")
time.sleep(1)

while True:
    cap = input("Do you want to start capture screen to OCR? (Y/N): ")
    if cap == "Y" or cap == "y":
        def on_click(x, y, button, pressed):
            global click_count,x1,y1,x2,y2
            if pressed:
                if click_count == 0:
                    click_count += 1
                    print(f"Mouse clicked at ({x}, {y})")
                    x1 = x
                    y1 = y
                    print("Please select second coordinates that capture screen: ")
                else:
                    print(f"Mouse clicked at ({x}, {y})")
                    x2 = x
                    y2 = y
                    return False

        # Create a listener instance
        listener = mouse.Listener(on_click=on_click)

        # Start the listener
        listener.start()

        print("Please select first coordinates that capture screen: ")
        listener.join() # loop for count click mouse
        print(f"Coordinates start at ({x1}, {y1}) and end at ({x2}, {y2})")

        time.sleep(1)
        print("Start screen short !!")
        print("\n ------- Extracted text from image show below ------- \n")
        screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        timestamp = time.strftime("%Y%m%d%H%M%S")

        # Save the captured screenshot with the timestamp
        file_path = f"screenshot_{timestamp}.png"

        # Save the captured screenshot
        screenshot.save(file_path)

        print("Screenshot saved successfully !!!")

        # refer exe file
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\samaphon.phrom\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
        # sample path--->E:\\Tesseract-OCR\\tesseract.exe

        img = cv2.imread(file_path)

        # pytessaract accepts only RGB value but cv2 accepts only BGR. So convert it before we send into pytesseract library
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


        #for raw imformation
        text = pytesseract.image_to_string(img)
        print(text)

        print("\n ------- Extracted text finished here ------- \n")

        file_name = f"{timestamp}.txt"
        file = open(file_name, "w")
        file.write(text)
        file.close()
        time.sleep(1)
        print("Save extracted text to txt file complete (^_^) ")

        # ONLY for location of character and box making---> Gives each character (x,y,w,h) coordinate values
        #print(pytesseract.image_to_boxes(img))

        #output will occur on console

        #cv2.imshow('result',img)
        #cv2.waitKey(0)

    elif cap == "N" or cap == "n":
        exits = input("Are you sure that exit screen capture OCR? (Y/N): ")
        if exits == "Y" or exits == "y":
            print("Exit screen capture OCR !!!")
            time.sleep(1)
            quit()
        elif exits == "N" or exits == "n":
            pass
        else:
            print("Please try again !!!")
    else:
        print("Please try again !!!")
