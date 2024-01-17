#Meu primeiro projetinho, Minha Calculadora
#Com finalidade de aprendizado, como fonte do canal Programador Aventureiro

import flet as ft
from flet import colors
from decimal import Decimal



buttons = [
    {'operador': 'AC', 'fonte': colors.BLACK,'fundo': colors.GREY },
    {'operador': '±', 'fonte': colors.BLACK,'fundo': colors.GREY },
    {'operador': '%', 'fonte': colors.BLACK,'fundo': colors.GREY },
    {'operador': '/', 'fonte': colors.BLACK,'fundo': colors.YELLOW_100 },
    {'operador': '7', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '8', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '9', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '*', 'fonte': colors.BLACK,'fundo': colors.YELLOW_100 },
    {'operador': '4', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '5', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '6', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '-', 'fonte': colors.BLACK,'fundo': colors.YELLOW_100 },
    {'operador': '1', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '2', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '3', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '+', 'fonte': colors.BLACK,'fundo': colors.YELLOW_100 },
    {'operador': '0', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '.', 'fonte': colors.WHITE,'fundo': colors.GREY },
    {'operador': '=', 'fonte': colors.BLACK,'fundo': colors.YELLOW_100 },

]


def main(page: ft.Page):
    page.bgcolor = '#4a4a4a'
    page.window_resizable = False
    page.window_width = 350
    page.window_height = 500
    page.title = 'Calculadora'
    

    result = ft.Text(value= '0', color= colors.WHITE, size=20)

    def calculate(operator, value_at):
        try:
            value = eval(value_at)

            if operator == '%':
                value /= 100
            elif operator == '±':
                value = -value
        except:
            return 'Error'
        
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')


    def select(e):        
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value == 'AC':
            value= '0'
        else:
            if value_at and value_at[-1] in ('/','*','-','+','.'):
                value_at = value_at[:-1]
        
            value = value_at + value

        if value[-1] in ('=','%','±'):
            value = calculate(operator=value[-1], value_at=value_at)

        result.value = value
        result.update()



    display = ft.Row(
        width=350,
        controls=[result],
        alignment= 'end',

    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=70,
        height=70,
        bgcolor=btn['fundo'],
        border_radius=5,
        alignment=ft.alignment.center,
        on_click=select
    
    )   for btn in buttons]


    keyboad = ft.Row(
        width=350,
        wrap=True,
        controls=btn,
        alignment='end'
    )


    page.add(display, keyboad)



ft.app(target = main)