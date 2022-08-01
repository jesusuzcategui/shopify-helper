import npyscreen as nps

class Login(nps.ActionForm):
    def create(self):
        self.usuario = self.add(nps.TitleText, name='Usuario:')
        self.contrasena = self.add(nps.TitlePassword, name='Contraseña:',)
    def on_ok(self):
        self.parentApp.change_form('PERFIL')

class Perfil(nps.ActionForm):
    def create(self):
        self.add(nps.TitleFixedText, name="Usuario <nombre del usuario>\n", value="")
        self.add(nps.ButtonPress, name="Cerrar sesión", when_pressed_function=self.close_session)

    def close_session(self):
        self.parentApp.change_form('MAIN')

class ElBrutoApp(nps.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN',Login, name='El Bruto - Login')
        self.addForm('PERFIL',Perfil,name="El Bruto - Perfil")

    def change_form(self, name):
        self.switchForm(name)
        self.resetHistory()

if __name__ == "__main__":
    app = ElBrutoApp()
    app.run()