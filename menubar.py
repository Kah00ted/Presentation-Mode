import rumps

#rumps.notification(title="gofer", subtitle="gofer is starting", message='', sound=False)

class goferApp(object):
    @rumps.clicked('Presentation Mode')

    def hello(sender):
        print(f"Hello from {sender.title}")

    def __init__(self):
        self.app = rumps.App("Presentation Mode", "🧨")

    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = goferApp()
    app.run()