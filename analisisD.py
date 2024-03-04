cadenaLarga = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur sodales suscipit dolor id luctus. Integer sem urna, euismod a accumsan in, aliquet ac augue. Maecenas at justo tellus. Sed sem lorem, pharetra ac sodales mollis, euismod sed mauris. Vivamus nec tortor a nulla aliquam viverra mollis sed ipsum. Nulla et libero a ex dignissim ullamcorper at sed erat. Aliquam in nisi eget mi sodales interdum. Praesent fermentum erat id ante consequat, ac tincidunt nunc rutrum. Maecenas at sapien eleifend, condimentum elit vel, consequat quam. Praesent hendrerit purus nec velit eleifend tempus. Nam malesuada massa at felis sollicitudin, sed ultricies eros porttitor. Vestibulum sit amet odio id nibh iaculis dapibus. Vestibulum tempus posuere mollis. Sed purus lorem, vulputate vitae diam id, tempus suscipit dolor. Nam vulputate nec massa vitae malesuada.

Donec vel sem et nisi feugiat semper non eget turpis. Nulla facilisi. Nunc suscipit feugiat velit. Nulla tincidunt, eros ut imperdiet dapibus, eros orci placerat lacus, id porttitor neque lacus eu nisi. Praesent tempus elit ac leo scelerisque, et pellentesque dolor condimentum. Aliquam purus dolor, convallis eget nulla ac, sodales mollis magna. Pellentesque posuere orci lorem, non tristique eros venenatis in. Phasellus dignissim dapibus metus at dignissim.

Sed justo purus, consectetur ut magna vitae, dictum mattis tellus. Aenean ipsum mauris, ultrices id pharetra id, finibus laoreet massa. Pellentesque gravida tellus condimentum sodales cursus. Donec blandit ullamcorper ante, sit amet cursus mi varius at. Nulla laoreet maximus metus, vitae aliquam nisi rutrum ac. Donec eu suscipit magna. In hac habitasse platea dictumst. In ut leo rhoncus, bibendum turpis sit amet, viverra nisl. Integer consectetur ante in turpis egestas aliquet. Aenean facilisis nec justo ut aliquam. Quisque eu enim libero. Vivamus sed egestas enim, ut facilisis sem. Vestibulum nunc diam, condimentum in nunc tempus, lacinia molestie odio.

Nulla accumsan venenatis massa eu eleifend. Maecenas tristique tellus at turpis elementum laoreet. Vestibulum quis justo luctus elit luctus imperdiet sed eu neque. In metus orci, faucibus a viverra non, eleifend eget lacus. Nunc bibendum tortor nec erat ullamcorper, ut consequat nisi tempus. Suspendisse convallis ligula in lectus fermentum, id commodo nisl condimentum. Praesent placerat auctor orci feugiat consequat. Nulla faucibus sed justo et ullamcorper. Proin iaculis dolor vel suscipit ornare. Duis vel ex viverra, sollicitudin tellus sit amet, convallis tortor. Praesent laoreet at nibh nec tristique. Nam eget mauris dignissim, sagittis lorem in, ornare nulla.

Curabitur bibendum diam vel ex commodo interdum. Morbi id nisi eget enim elementum euismod. Nulla scelerisque posuere arcu, sed iaculis nisi efficitur nec. Vestibulum at eros maximus, tempus eros non, porta risus. Donec gravida neque ut nulla hendrerit porta. In semper sapien quis tortor scelerisque lacinia vitae ut nunc. Maecenas dapibus ligula nec molestie volutpat. In rutrum ligula nec finibus posuere. Vivamus accumsan dictum interdum. Nullam ornare interdum est eget sagittis. In hac habitasse platea dictumst. Donec ex neque, mattis vel sapien et, maximus volutpat erat. Suspendisse potenti. Donec vel urna mi. Sed porttitor convallis tincidunt. Nam tempus ante ac vulputate semper.
"""

letras = 'abcdefghijklmnñopqrstuvwxyz'
caracteres =['a','e','i', 'o','u', ' ', ',','.' ]
estadisticas = ['Total de caracteres:', 'Total de letras : ', 'Total de vocales a :', 'Total de vocales e :', 'Total de vocales i :', 'Total de vocales o :', 'Total de vocales u :', 'Total de espacios :', 'Total de comas:', 'Total de puntos:']
totales = [0] * len(estadisticas)

for char in cadenaLarga:
    totales[0] += 1  # Total de caracteres
    if char in letras:
        totales[1] += 1  # Total de letras
    if char in caracteres[0]:
        totales[2] += 1  # Total de vocales a
    elif char in caracteres[1]:
        totales[3] += 1  # Total de vocales e
    elif char in caracteres[2]:
        totales[4] += 1  # Total de vocales i
    elif char in caracteres[3]:
        totales[5] += 1  # Total de vocales o
    elif char in caracteres[4]:
        totales[6] += 1  # Total de vocales u
    elif char == ' ':
        totales[7] += 1  # Total de espacios
    elif char == ',':
        totales[8] += 1  # Total de comas
    elif char == '.':
        totales[9] += 1  # Total de puntos

print("Resumen de estadísticas:")
for i in range(len(estadisticas)):
    print(estadisticas[i], totales[i])