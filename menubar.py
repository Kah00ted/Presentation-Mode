import rumps
from presentationMode import *

class menuApp(object):

    def __init__(self):
        self.app = rumps.App("Presentation Mode", "👀")

        self.branding = rumps.MenuItem(title="--Reid Metzger--", callback=None)

        self.presentation = rumps.MenuItem(
            title="Presentation Mode", callback=None)
        self.presentation.on = rumps.MenuItem(
            title="on", callback=self.presentationMode)
        self.presentation.off = rumps.MenuItem(title="off", callback=None)

        self.app.menu = [
            #self.branding,
            #None,
            [self.presentation, [self.presentation.on, self.presentation.off]]
        ]

    def presentationMode(self, sender):
        if (sender.title == "on"):
            self.presentation.on.set_callback(None)
            self.presentation.off.set_callback(self.presentationMode)

            setPresentationMode(True)

            rumps.notification(title="Presentation Mode: Enabled", subtitle=f"", message='', sound=False)

        else:
            self.presentation.off.set_callback(None)
            self.presentation.on.set_callback(self.presentationMode)

            setPresentationMode(False)

            rumps.notification(title="Presentation Mode: Disabled", subtitle=f"", message='', sound=False)

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = menuApp()
    app.run()
