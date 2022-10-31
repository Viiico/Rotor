import socket
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

class Rotororororo(Widget):
    def __init__(self, **kwargs):
        super(Rotororororo, self).__init__(**kwargs)
        self.present()


    def rotateLeft(self): 
        self.degrees = self.degrees-1 if self.degrees > 0 else 359
        self.present()
        self.s = socket.socket()
        self.s.connect(('127.0.0.1', 5050))
        self.s.send("Lewo".encode())
        sResponse = self.s.recv(1024)
        print(sResponse.decode())

    def rotateRight(self):
        self.degrees = self.degrees+1 if self.degrees < 359 else 0
        self.present()
        self.s = socket.socket()
        self.s.connect(('127.0.0.1', 5050))
        self.s.send("Prawo".encode())
        sResponse = self.s.recv(1024)
        print(sResponse.decode())

    def present(self):
        self.degreeLabel.text = str(self.degrees)

Builder.load_string('''
<Rotororororo>:
    degrees: 0
    degreeLabel: degreeLabel
    BoxLayout:
        size: root.size
        orientation: 'vertical'
        Image:
            source: "arrow.png"
            size: self.texture_size
            canvas.before:
                PushMatrix
                Rotate:
                    angle: -root.degrees
                    origin: self.center
            canvas.after:
                PopMatrix
        Label:
            id: degreeLabel
            text: "Degress"
        GridLayout:
            cols: 2
            Button:
                id: arrowLeft
                text: "turn left"
                on_release: root.rotateLeft()            
            Button:
                id: arrowRight
                text: "turn right"
                on_release: root.rotateRight()
''')

class testApp(App):
    def build(self):
        return Rotororororo()

if __name__ == "__main__":
    testApp().run()