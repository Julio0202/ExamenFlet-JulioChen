import flet as ft


def main(page: ft.Page):
    page.title = "Examen Flet"
    #Ejercicio 6
    alerta = ft.AlertDialog(title=ft.Text("El usuario y contraseña es igual"))
    def aviso_usuario_contra(e):
        if tfnombre.value == tfpassword.value:
            alerta.open = True
            page.update()
    #Fin --- Ejercicio 6


    #Ejercicio 2
    img = ft.Image(src="/fotos/Logo.png")
    
    #Fin --- Ejercicio 2


    #Ejercicio 3
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #Fin --- Ejercicio 3

    page.window_height=500
    page.window_width= 250



    tfnombre = ft.TextField(label="Nombre")
    #Ejercicio 4
    tfpassword = ft.TextField(label="Contraseña",password=True,can_reveal_password=True)

    #Fin --- Ejercicio 4

    #Ejercicio 5
    btnEntrar = ft.ElevatedButton(text="Boton",icon="chair_outlined",on_click=aviso_usuario_contra)
    #Fin-- Ejercicio 5
    page.add(img,tfnombre,tfpassword,btnEntrar,alerta)



ft.app(target=main,assets_dir="fotos")