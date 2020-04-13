import sys
import ac
import acsys

def acMain(ac_version):
        global shadow, label, appWindow
        appWindow = ac.newApp("SimpleSpeedo")
        ac.setSize(appWindow, 120, 60)
        ac.setBackgroundOpacity(appWindow,0)
        ac.drawBorder(appWindow,0)
        ac.setIconPosition(appWindow, 0, -9000)
        -ac.setTitlePosition(appWindow,0, -9000)

        shadow = ac.addLabel(appWindow, "?")
        ac.setFontSize(shadow, 44)
        ac.setPosition(shadow, 61, 1)
        ac.setFontColor(shadow, 0.2, 0.2, 0.2, 0.2)
        ac.setFontAlignment(shadow, "center")

        label = ac.addLabel(appWindow, "?")
        ac.setFontSize(label, 44)
        ac.setPosition(label, 60, 0)
        ac.setFontColor(label, 1, 1, 1, 0.4)
        ac.setFontAlignment(label, "center")

        return "SimpleSpeedo"

def acUpdate(deltaT):
        global speed, appWindow
        ac.setBackgroundOpacity(appWindow,0)
        speed = ac.getCarState(0, acsys.CS.SpeedKMH)
        ac.setText(label, "{}".format(int(speed)))
        ac.setText(shadow, "{}".format(int(speed)))
