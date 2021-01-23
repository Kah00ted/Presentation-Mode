import rumps

#rumps.notification(title="gofer", subtitle="gofer is starting", message='', sound=False)

class menuApp(object):

    def __init__(self):
        self.app = rumps.App("Presentation Mode", "🧨")

        self.branding = rumps.MenuItem(title="--Reid Metzger--", callback=None)

        self.presentation = rumps.MenuItem(title="Presentation Mode", callback=None)
        self.presentation.on = rumps.MenuItem(title="on", callback=self.presentationMode)
        self.presentation.off = rumps.MenuItem(title="off", callback=self.presentationMode)

        self.app.menu = [
            self.branding, 
            None, 
            [self.presentation,[self.presentation.on, self.presentation.off]]
        ]

    def presentationMode(self, sender):
        rumps.notification(title="Present", subtitle=f"Presentation Mode is {sender.title}", message='', sound=False)

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = menuApp()
    app.run()