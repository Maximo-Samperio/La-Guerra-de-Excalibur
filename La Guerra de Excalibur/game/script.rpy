# ↓ Fade in y fade out de la barra de decisiones
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0
    

init:
    # Definicion de personajes
    $ a = Character ("Arthur", color="#ffee00ff")
    $ m = Character ("Merlín", color="#820992ff")

    # Planos de Merlin
    image merlinFeliz = im.Scale("MerlinFeliz.png", 1280, 720)
    image merlinEnojado = im.Scale("MerlinEnojado.png", 1280, 720)
    image merlinPensativo = im.Scale("MerlinPensativo.png", 1280, 720)
    image merlinPreocupado = im.Scale("MerlinPreocupado.png", 1280, 720)
    image merlinSorprendido = im.Scale("MerlinSorprendido.png", 1280, 720)


    #Planos de Arthur
    image arthurLlorando = im.Scale("ArthurLlorando.png", 820, 720)
    image arthurEmocionado = im.Scale("ArthurEmocionado.png", 820, 720)
    image arthurEnojado = im.Scale("ArthurEnojado.png", 820, 720)
    image arthurFeliz = im.Scale("ArthurFeliz.png", 820, 720)
    image arthurEmocionado = im.Scale("ArthurEmocionado.png", 820, 720)
    image arthurPreocupado = im.Scale("ArthurPreocupado.png", 820, 720)
    image arthurPensativo = im.Scale("ArthurPensativo.png", 820, 720)



    # Definicion de imagenes de fondos
    image bolaDeCristal = im.Scale("BolaCristal.jpg", 1920, 1080)
    image camelot = im.Scale("Camelot.jpeg", 1920, 1080)
    image casaDia = im.Scale("CasaDia.jpeg", 1920, 1080)
    image casaNoche = im.Scale("CasaNoche.jpeg", 1920, 1080)
    image cuarto = im.Scale("Cuarto.jpg", 1920, 1080)
    image desierto = im.Scale("Desierto.jpeg", 1920, 1080)
    image ejercito = im.Scale("Ejercito.jpeg", 1920, 1080)
    image genteCaminando = im.Scale("GenteCaminando.jpeg", 1920, 1080)
    image lunaRoja = im.Scale("LunaRoja.jpeg", 1920, 1080)
    image tumba = im.Scale("Tumba.jpg", 1920, 1080)
    image ninojugando = im.Scale("NiñoJugando.jpeg", 1920, 1080)

    


    # image imageName = "imageFileName.jpg"

    #Definicion de variables 
    default dedicacion = 0      # Sistema de honor

    $ time = 0                  # Tiempo a contar
    $ timer_range = 0           # Tiempo a contar pero para la barra de animacion
    $ timer_jump = 0            # lugar al que saltar si se acaba el tiempo

screen countdown:
    # ↓ Dismuinuye la var time por 0.01 hasta llegar a 0, en cuyo punto, el juego salta a la label timer_jump
    timer 0.001 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

    # ↓ La barra del timer en la UI
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve


label start:
    # Para mostrar una imagen
    # show imageName

    # Para dejar de mostrar una imagen
    # hide imageName

    show lunaRoja
    play music "MusicaEpica.mp3" volume 0.1
    "La isla de Avalon (la isla de las hadas)"

    play sound "LaProfecia1.mp3" volume 1.0
    queue sound "BebeLlorando.mp3" volume 0.3
    "El elegido que fue prometido, nacido bajo la luna roja, despertara." 

    play sound "LaProfecia2.mp3" volume 1.0
    queue sound "BebeLlorando.mp3" volume 0.3
    "Concebido por el poder de la magia e hijo de un rey, él será..."

    play sound "LaProfecia3.mp3" volume 1.0
    queue sound "BebeLlorando.mp3" volume 0.3
    "Cuando el equilibrio se tambalee, el pasado y el futuro deberán fluir y combinarse."

    play sound "LaProfecia4.mp3" volume 1.0
    queue sound "BebeLlorando.mp3" volume 0.3
    "Un elegido surgirá, cuando le ponga fin a Excalibur, y a través de él, el equilibrio final de las energías se restablecerá"

    hide lunaRoja

    show camelot
    "La Guerra de Excalibur"
    hide camelot
    stop music fadeout 1.0
    
    show casaDia
    show merlinPensativo at left
    show arthurPensativo at right
    play music "RuidoDePajaros.mp3" volume 0.2
    play sound "EspadasChocando.mp3" volume 0.4

    m "Arthur, ¿qué te parece si realizamos una sesión extra de entrenamiento? Te vendría bien reforzar tu técnica con la espada."


    label trainingChoiceLoop:
        $ time = 6                          # Seteo de la variable de tiempo
        $ timer_range = 6                   # Setear el rango de la barra
        $ timer_jump = 'training_slow'      # Setear a donde saltar en fallo
        show screen countdown
        menu:
            "Aceptar la sesión extra":
                hide screen countdown       # Detiene el timer
                $ dedicacion += 1
                #a "dedicacion actual es total a: [dedicacion]."
                hide merlinPensativo
                show arthurEmocionado at right
                show merlinFeliz at left

                a "Está bien, no veo por qué no. Un poco más de práctica no le hace mal a nadie."
                m "¡Buena decisión!"
                hide casaDia
                hide arthurEmocionado
                hide merlinFeliz
                stop sound
                show casaNoche
                show arthurEmocionado at right
                show merlinFeliz at left
                "*Un rato después*"
                m "¡Buen trabajo Arthur! Estoy orgulloso de ti. Es increíble todo lo que has avanzado en los meses que hemos estado juntos. No dejas de sorprenderme."
                hide arthurEmocionado
                show arthurFeliz at right
                a "Gracias Merlín, estoy dando lo mejor de mí y es bueno ver que eso da frutos."
                m "Pues claro que da frutos. Y me parece muy bien que des lo mejor de ti. Eso es lo que se espera de alguien que se convertirá en el guía de este reino. Serás un gran líder si te mantienes en este camino."
                m "Por no hablar de toda la gente que cree en ti, Arthur. No hablo solo de La Mesa Redonda, sino de todo el pueblo. Todos cuentan contigo."
                hide arthurFeliz
                hide merlinFeliz
                hide casaNoche
                stop music fadeout 1.0

            "Negarse a la sesion extra":
                $ dedicacion -= 1
                hide screen countdown       # Detiene el timer
                hide merlinPensativo
                stop sound
                show arthurPensativo at right
                show merlinPreocupado at left

                a "Eh, la verdad que no tengo muchas ganas, ya estuve entrenando un poco hoy y prefiero descansar ahora"
                m "Que... decepcionante de tu parte, Arthur. Esperaba más dedicación de tu parte a la causa, más aun sabiendo a lo que nos enfrentamos."
                m "La Orden... está arrasando con todo a su paso y la gente cree en ti, Arthur. Sus esperanzas están depositadas en ti."
                hide arthurPensativo
                hide arthurPensativo
                hide merlinPreocupado
                hide casaDia
                stop music fadeout 1.0

    "El tiempo pasa y Arthur se dirige hacia su cuarto"
    
    "*Arthur agacha la cabeza un poco avergonzado y piensa para sí mismo...*"
    show cuarto
    play music "SonidoDeGranja.mp3" volume 0.1

    show arthurPensativo


    a " Pero... ¿realmente quiero ser rey?"
    a "La responsabilidad es tan grande..."

    hide cuarto
    hide arthurPensativo

    show genteCaminando
    a "Las personas del reino"
    hide genteCaminando

    show ejercito
    a "La Orden"
    hide ejercito

    show ninojugando
    a "La vida"
    hide ninojugando

    show tumba
    a "La muerte"
    hide tumba 

    show cuarto
    show arthurPensativo
    a "Todo depende de mi..."
    a "¿Realmente quiero ser rey?"


    menu:
        "Si. Quiero ser rey.":
            hide arthurPensativo
            show arthurFeliz
            a "Sí, tengo que ser rey. La gente me necesita y ahí estaré para protegerlos"
            hide arthurFeliz
            $ dedicacion += 1

        "No. No quiero ser rey":
            hide arthurPensativo
            jump huida

    show arthurPensativo
    a "Sin embargo... ¿Qué tipo de rey quiero ser?"
    menu:
        "Un rey que se concentre en proteger a sus seres queridos":
            $ dedicacion += 1
            a "Seré un rey bondadoso, que se esforzará por proteger aquello más preciado para uno... su gente. Un rey no es nada sin un reino que gobernar. Tengo que continuar mi entrenamiento, ese es el camino que Merlín también elegiría para mi."
        
        "Un rey que se concentre en destruir a sus enemigos":
            $ dedicacion -= 1
            a "Si... La Orden debe ser aniquilada. He visto lo que hacen. Asesinan hombres, mujeres y niños por igual. Queman aldeas, encerrando a los habitantes dentro de sus casas para oír sus gritos mientras se queman vivos."
            a "Son unos monstruos y serán tratados acorde. Merlín me ha advertido sobre estos pensamientos oscuros, pero es la cruda realidad."
            a "Se que Merlín no piensa igual."
            menu:
                "Eso se debe a que es misericordioso":
                    $ dedicacion += 1
                    
                "Eso se debe a que es un cobarde":
                    $ dedicacion -= 1
    hide arthurPensativo
    hide cuarto

    show casaDia
    show arthurFeliz at right
    "A la madrugada del día siguiente, Arthur se levanta con renovadas energías y voluntad para entrenar."

    show merlinFeliz at left
    "Al levantarse y encontrarlo ya entrenando, Merlín felicita su perseverancia."
    hide merlinFeliz
    show merlinPensativo at left


    m "Arthur, la perseverancia es una de las cualidades de un líder. Me gustaría que hablemos un rato sobre eso, ¿Qué te parece?"

    menu:
        "Reflexionar sobre las cualidades de un líder, así seré mejor rey.":
            
            $ dedicacion += 1
            a "Claro, Merlín. Cuéntame sobre las cualidades de un líder."
            hide merlinPensativo
            show merlinFeliz at left

            m "Bien. Algunas de las cualidades distintivas de los lideres son: la proactividad, la habilidad para coordinar con otras personas, saber elegir prioridades, ser una persona integra y moral, entre otras."
            m "¿Y sabes que es lo sorprendente, Arthur? Tu las posees todas y cada una de ellas."
            hide merlinFeliz
            show merlinPreocupado at left
            m "Y con esto en mente y sabiendo el orgullo que me generas, me gustaría que sepas algo."
            hide arthurFeliz
            show arthurPreocupado at right
            a "¿Qué Merlín?"
            m "Tú... no eres el elegido que creíamos que eras, Arthur."
            "Se realiza una breve pausa."
            hide arthurPreocupado
            show arthurEnojado at right
            a "¡¿Qué?!"
            m "Lo- Lo siento, Arthur. Sin embargo... a pesar de no ser el elegido de la profecía has sido elegido en cierta forma."
            a "No entiendo muy bien a que te refieres."
            m "Arthur, has sido elegido por la mesa redonda, pero no por una profecía de tiempos antiguos, sino por hechos fácticos."
            m "Eres una persona con dones inconmensurables."
            hide merlinPreocupado
            show merlinFeliz at left
            m "La gente levanta la cabeza cuando te ve, tienes un aura digna de un rey e igualmente queremos seguir llevando a cabo nuestro plan. Sin embargo, quería ser honesto sobre la naturaleza de la profecía."
            "Arthur piensa para sí mismo..."
            if dedicacion <= -1:
                menu:
                    "Pero qué carajos me está diciendo el viejo... maldito traicionero.":
                        jump angry
                        $ dedicacion -= 1
                
            else:
                menu:
                    "Merlín... no estoy enojado. Simplemente decepcionado. De todas formas quiero seguir por este camino.":
                        jump good_ending
                        $ dedicacion += 1
                        
                    "Pero qué carajos me está diciendo el viejo... maldito traicionero.":
                        jump angry
                        $ dedicacion -= 1
                        
        
        "¿Qué me importa eso?, yo solo quiero entrenar y hacerme fuerte":
            $ dedicacion -= 1
            hide casaDia
            hide merlinPensativo
            hide arthurFeliz
            "Dada la aparente falta de interés de Arthur, Merlín decide dejarlo entrenando solo."
            "Un par de horas mas tarde, cuando el joven regresa a la cabaña, este logra escuchar a Merlín hablando por su bola de cristal, y oye algo que no debió de haber escuchado..."
            show casaDia
            m "'Él no es el elegido del cual habla la profecía'."
            show arthurPreocupado at right
            "Arthur se detiene súbitamente, en shock."

            # Esta ausencia de eleccion solo sucede si el jugador eligio todas y cada una de las elecciones deshonorables, es decir, es irredimible
            if dedicacion <= -2:
                menu:
                    "Abandonar a Merlín y escapar del reino.":
                        jump huida

            # Si el jugador es honorable, tiene poder de eleccion
            else:
                menu:
                    "Enfrentar a Merlín y discutir con el.":
                        jump angry

                    "Abandonar a Merlín y escapar del reino.":
                        jump huida
    #End
    return

label training_slow:
    hide merlinPensativo
    show merlinEnojado at left
    m "¿Arthur? ¿Estás ahí?"
    hide arthurPensativo
    show arthurEmocionado at right
    a "Lo- Lo siento Merlin, ¿Qué dijiste?"
    "*Merlín suspira de cansancio*"
    m "Te pregunte si te gustaría realizar una sesión extra de entrenamiento, ya que te vendría bien reforzar tu técnica con la espada."
    hide arthurEmocionado
    hide merlinEnojado
    show merlinPensativo at left
    show arthurPensativo at right
    jump trainingChoiceLoop




label angry:
    "Arthur estalla de furia contra Merlín ante este hecho."
    hide merlinFeliz
    show merlinPreocupado at left
    show arthurEnojado at right
    a "¡Merlín! De todas las personas en el mundo... jamás pensé que ibas a ser tú, la misma persona que me rescato quien me iba a mentir de esta forma... Me siento traicionado."
    m "Perdón Arthur. Mis más sinceras disculpas. Pero... una cosa no quita la otra. No necesitas ninguna profecía antigua para convertirte en el rey y salvador de estas tierras ¡Ya eres un líder y te estás convirtiendo en el salvador! Que importa lo que una profecía diga."
    
    if dedicacion <= -1:
        menu:
            "Explotar de rabia e intentar asesinar a Merlín.":
                jump bad_ending

            "Dejarlo atrás, ya no te interesa ser ni el rey salvador ni un villano. Alejarte. Escapar.":
                jump huida

    else:
        menu:
            "Entrar en razón, relajarse y darle una oportunidad.":
                jump good_ending
            
            "Explotar de rabia e intentar asesinar a Merlín.":
                jump bad_ending

            "Dejarlo atrás, ya no te interesa ser ni el rey salvador ni un villano. Alejarte. Escapar.":
                jump huida


#End
    return



label good_ending:
    hide arthurEnojado
    show arthurPensativo at right
    a "Merlín... me decepciona saber que no soy 'El Elegido' de la profecía, no te voy a mentir. Creía que tenía un derecho divino."
    a "Sin embargo, ahora comprendo a lo que te referías. Es mas importante ganarse el derecho mediante las cualidades entrenadas por uno mismo a aquellas que se le achacan a uno mediante fuentes desconocidas."
    a "No necesito una profecía para desear ayudar a mi pueblo. Nunca la necesité."
    hide merlinPreocupado
    show merlinFeliz
    hide arthurPensativo
    show arthurFeliz at right
    a "¡Vamos a continuar el camino que empezamos, detener a La Orden y restaurar el reino en su gloria total!"
    a "¡Vamos a convertirnos en el escudo de las personas y traer justicia al reino!"

    "Aquí comienza el viaje...\nContinuará..."

#End
    return


label bad_ending:
    "Arthur se deja llevar por la furia... una furia potenciada por el combustible más  potente de todos. La traición."
    "En un arrebato de fuerza y sorpresa para el mago, Arthur agarra la cabeza del mago y la estampa contra la pared, pulverizándole el miembro superior y dejándolo sin vida."
    hide merlinPreocupado
    hide arthurEnojado
    show arthurEnojado
    a "Aquí le declaro la guerra a La Mesa Redonda. Una organización fundada por una rata traidora como esta no puede ser redimida."
    a "Al parecer La Orden tenía razón."
    "Y así, Arthur, decide emprender un nuevo camino. Un camino lleno de dolor y sufrimiento, pero tal es el odio y el resentimiento que le genera la traición de la mesa redonda que es capaz de apaciguar todo ese dolor para ver su fin realizado..."
    "Ver a la mesa redonda arder.\nContinuará..."

#End
    return



label huida:
    hide arthurPreocupado
    show arthurEnojado
    a "No. No puedo ser rey. No estoy capacitado, nunca lo estaré. No soy ningún elegido de nada."
    "Sumido completamente en la ansiedad, la presión y la desesperación, Arthur, decide escapar esa misma noche."
    "Dejando atrás toda su vida, con la esperanza de encontrar una... más simple."
    "Una vida sin tanta preocupación."
    hide casaDia
    show desierto
    play music "SonidoDeAguila.mp3" volume 0.3
    play sound "SonidoDeCaballo.mp3" volume 0.5

    "Un par de horas después, Arthur, llega a 'La frontera del mundo', la división de los reinos."
    "Sin embargo, al estar a punto de cruzar la frontera, unas siluetas sigilosas se asoman de las esquinas y encierran a Arthur." 
    "La Orden lo había encontrado."

    hide arthurEnojado
    show arthurLlorando

    menu:
        "Tengo que defenderme.":
            "Pero claro... Arthur abandonó de forma temprana su entrenamiento. No tiene defensa ni escapatoria."

    a "*Comienza a temblar de miedo y ansiedad*"
    a "No puedo volver otra vez con La Orden."
    "Y todos los recuerdos dolorosos, marcados en su alma como una cicatriz, empezaron a fluir como un rio."
    "El trabajo forzado."
    "El cansancio físico."
    "La tortura mental."
    "Arthur posó su mano sobre las cicatrices en toda su espalda causadas por los latigazos, sintiendo su relieve irregular y se decidió."
    hide arthurLlorando
    show arthurEnojado
    a "No puedo volver a ese infierno."
    a "No puedo."

    menu:
        "Acabar con todo":
            "Y así, Arthur en un fluido movimiento se corta las venas."

    
    "Y asi, Arthur en un fluido movimiento se corta las venas. Una solución mejor que volver al sufrimiento generado por La Orden, mejor que ser usado como un arma contra las personas."
    hide arthurEnojado
    "Fin."
    #End
    return