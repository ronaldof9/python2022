# Background
Rect(0, 0, 400, 400, fill=gradient('silver', 'black', start='left-top'))

# Cinta y tarjeta
Line(200, 95, 275, -15, fill='crimson', lineWidth=35)
Rect(25, 75, 350, 275, fill=gradient('red', 'orange', 'yellow', 'limeGreen',
                                     'blue', 'purple', start='bottom'))
Line(200, 95, 145, -15, fill='red', lineWidth=35)
Oval(200, 95, 85, 15, fill='grey')

# Sección blanca para escribir
Rect(50, 190, 300, 120, fill='white')
Rect(65, 175, 270, 150, fill='white')
Circle(65, 190, 15, fill='white')
Circle(65, 310, 15, fill='white')
Circle(335, 190, 15, fill='white')
Circle(335, 310, 15, fill='white')

# Label
Label('Hello, my name is', 200,140, fill='white', size=35, font='arial', bold=True)
Label('Python',200,250, fill=gradient('limeGreen', 'yellow', 'orange', start='top'), border='black', size=75, bold=True)
