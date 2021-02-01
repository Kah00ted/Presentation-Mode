import rumps
from presentationMode import *
import webbrowser

class menuApp(object):

    def __init__(self):
        self.app = rumps.App("Presentation Mode", "👀", quit_button=None)

        self.about = rumps.MenuItem(title="About", callback=None)
        self.about.by = rumps.MenuItem(title="Author: Reid Metzger", callback=self.openLink)
        self.about.git = rumps.MenuItem(title="Github", callback=self.openLink)
        self.about.quit = rumps.MenuItem(title="Quit App", callback=rumps.quit_application)

        self.presentation = rumps.MenuItem(
            title="Presentation Mode", callback=None)
        self.presentation.on = rumps.MenuItem(
            title="on", callback=self.presentationMode)
        self.presentation.off = rumps.MenuItem(title="off", callback=None)

        self.app.menu = [
            #self.branding,
            #None,
            [self.presentation, [self.presentation.on, self.presentation.off]],
            None,
            [self.about, [self.about.by, self.about.git, None, self.about.quit]]
        ]

    def openLink(self, sender):
        if (sender.title == "Author: Reid Metzger"):
            webbrowser.open("https://reidmetzger.com", new=0, autoraise=True)
        if (sender.title == "Github"):
            webbrowser.open("https://github.com/Kah00ted", new=0, autoraise=True)

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
