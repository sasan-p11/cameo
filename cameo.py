import cv2
#import filters
from managers import WindowManager , CaptureManager

class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager("Cameo",self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture("rtsp://admin:Admin12345%21@192.168.1.108:554/live"),self._windowManager,True)
       # self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        ''' run the main loop'''
        self._windowManager.createWindow()
        while self._windowManager._isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            # if frame is not None:
            #     filters.strokeEdges(frame, frame)
            #     self._curveFilter.applay(frame,frame)

            self._captureManager.exitFrame()
            self._windowManager.processEvent()


    def onKeypress(self,keycode):
        '''
            handle a key press
            space -> take screenshot
            tab -> start/stop recording a screencats
            escape -> quit
        '''

        if keycode ==  32 :#space
            self._captureManager.writeImage("screenshot.png")
        elif keycode == 9 :#tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo("screencast.avi")
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27 :# escape
            self._windowManager.destroyWindow()
        


if __name__ == "__main__":
    Cameo().run()