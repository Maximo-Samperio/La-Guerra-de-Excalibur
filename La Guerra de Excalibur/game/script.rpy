
init:
    # Definicion de personajes
    $ a = Character ("Arthur", color="#ffee00ff")
    $ m = Character ("Merlin", color="#085bc7ff")

    # Definicion de imagenes
    # image imageName = "imageFileName.jpg"




label start:

    #Lista de variables
    default dedicacion = 0

    # Para mostrar una imagen
    # show imageName

    # Para dejar de mostrar una imagen
    # hide imageName

    # Si quiero solo texto (estilo narracion), se pone el texto pelado entre ""
    "El elegido que fue prometido, nacido bajo la luna roja, despertara."
    "El elegido que fue prometido, nacido bajo la luna roja, despertara.\nConcebido por el poder de la magia y hijo de un rey, él será..."
    "El elegido que fue prometido, nacido bajo la luna roja, despertara.\nConcebido por el poder de la magia y hijo de un rey, él será...\nCuando el equilibrio se tambalee, el pasado y el futuro deberán fluir y combinarse"
    "El elegido que fue prometido, nacido bajo la luna roja, despertara.\nConcebido por el poder de la magia y hijo de un rey, él será...\nCuando el equilibrio se tambalee, el pasado y el futuro deberán fluir y combinarse.\nUn elegido surgirá, cuando le ponga fin a Excalibur, y a través de él, el equilibrio final de las energías se restablecerá"

    "La Guerra de Excalibur"

    "Arthur estaba entrenando con Merlín, su mentor y quien lo ha rescatado de las garras de 'La Orden', una organización temeraria que guerrea sobre el reino de Arthur y retuvo a este cautivo durante años con la promesa de que él sea 'El Elegido'"
    
    
    # Si quiero que arriba de eso aparezca quien lo dice (estilo coment.), se pone el char con el que se declara el pj y el texto entre ""
    m "Arthur, ¿qué te parece si realizas una sesión extra de entrenamiento? Te vendría bien reforzar tu técnica con la espada."
    menu:
        "*Aceptar la sesión extra*":
            #dedicacion++
            a "Está bien, no veo por qué no. Un poco más de práctica no le hace mal a nadie."
            m "¡Buena decisión!"
            "*Un rato después*"
            m "¡Buen trabajo Arthur! Estoy orgulloso de ti. Es increíble todo lo que has avanzado en los meses que hemos estado juntos. No dejas de sorprenderme."
            a "Gracias Merlín, estoy dando lo mejor de mí y es bueno ver que eso da frutos."
            m "Pues claro que da frutos. Y me parece muy bien que des lo mejor de ti. Eso es lo que se espera de alguien que se convertirá en el guía de este reino. Serás un gran líder si te mantienes en este camino."
            m "Por no hablar de toda la gente que cree en ti, Arthur. No hablo solo de La Mesa Redonda, sino de todo el pueblo. Todos cuentan contigo."

        "*Negarse a la sesion extra":
            #dedicacion--
            a "Eh, la verdad que no tengo muchas ganas, ya estuve entrenando un poco hoy y prefiero descansar ahora"
            m "Que... decepcionante de tu parte, Arthur. Esperaba más dedicación de tu parte a la causa, más aun sabiendo a lo que nos enfrentamos."
            m "La Orden está arrasando con todo a su paso y la gente cree en ti, Arthur. Sus esperanzas están depositadas en ti."

    "*Arthur agacha la cabeza un poco avergonzado y piensa para sí mismo...*"

    a " Pero... ¿realmente quiero ser rey?"
    a "La responsabilidad es tan grande..."
    a "Las personas del reino"
    a "La Orden"
    a "La Mesa Redonda"
    a "La vida"
    a "La muerte"
    a "Todo depende de mi..."
    a "¿Realmente quiero ser rey?"

    menu:
        "Si. Quiero ser rey.":
            a "Sí, tengo que ser rey. La gente me necesita y ahí estaré para protegerlos"

        "No. No quiero ser rey":
            jump huida

    a "Sin embargo... ¿Qué tipo de rey quiero ser?"
    menu:
        "Un rey que se concentre en proteger a sus seres queridos":
            #Dedicacion++
            a "Seré un rey bondadoso, que se esforzara por proteger aquello más preciado para uno... su gente. Un rey no es nada sin un reino que gobernar. Tengo que continuar mi entrenamiento, ese es el camino que Merlín también elegiría para mi"
        
        "Un rey que se concentre en destruir a sus enemigos":
            #Dedicacion--
            a "Si... La Orden debe ser aniquilada. He visto lo que hacen. Asesinan hombres, mujeres y niños por igual. Queman aldeas, encerrando a los habitantes dentro de sus casas para oír sus gritos mientras se queman vivos. Son unos monstruos y serán tratados acorde. Merlín me ha advertido sobre estos pensamientos oscuros, pero es la cruda realidad."
    
    "A la madrugada del día siguiente, Arthur se levanta con renovadas energías y voluntad para entrenar. "
    "Al levantarse y encontrarlo ya entrenando, Merlín felicita su perseverancia."

    m "Arthur, la perseverancia es una de las cualidades de un líder. Me gustaría que hablemos un rato sobre eso, ¿qué te parece?"
    menu:
        "Reflexionar sobre las cualidades de un lider, asi seré mejor rey":
            #Dedicacion++
            a "Claro, Merlín. Cuéntame sobre las cualidades de un líder"
            m "Bien. Algunas de las cualidades distintivas de los lideres son: la proactividad, la habilidad para coordinar con otras personas, saber elegir prioridades, ser una persona integra y moral, entre otras."
            m "¿Y sabes que es lo sorprendente Arthur? Tu las posees todas y cada una de ellas."
            m "Y con esto en mente y sabiendo el orgullo que me generas, me gustaria que sepas algo."
            a "¿Qué Merlin?"
            m "Tu... no eres el elegido que creiamos que eras Arthur."
            "Se realiza una breve pausa."
            a "¿Qué?"
            m "Lo- Lo siento Arthur. Sin embargo... a pesar de no ser el elegido de la profecia has sido elegido en cierta forma."
            a "No entiendo muy bien a que te refieres."
            m "Arthur, has sido elegido por la mesa redonda, pero no por una profecía de tiempos antiguos, sino por hechos factuales."
            m "Eres una persona con dones inconmensurables."
            m "La gente levanta la cabeza cuando te ve, tienes un aura digna de un rey e igualmente queremos seguir llevando a cabo nuestro plan. Sin embatgo, quería ser honesto igualmente sobre la naturaleza de la profecía."
            "Arthur piensa para si mismo..."
            menu:
                "*Merlin... no estoy enojado. Simplemente decepcionado. De todas formas ya esta. Quiero seguir por este camino*":
                    jump good_ending
                    #Dedicacion++


                "*Pero qué carajos me está diciendo el viejo... maldito traicionero*":
                    jump angry
                    #Dedicacion--
        
        "Que importa eso, yo solo quiero entrenar y hacerme fuerte":
            #Dedicacion--
            "Dada la aparente falta de interes de Arthur, Merlin decide dejarlo entrenando solo."
            "Un par de horas mas tarde, cuando el joven regresa a la cabaña, este logra escuchar a Merlin hablando por su bola de cristal, y oye algo que no debio de haber escuchado..."
            m "El no es el elegido del cual hablaba la profecía"
            "Arthur se detiene subitamente, en shock"
            menu:
                "Enfrentar a Merlin y discutir con el":
                    jump angry
                
                "Abandonar a Merlin y escapar del reino":
                    jump huida




    #End
    return



label angry:
    "Arthur estalla de furia contra Merlin ante este hecho"
    a "¡Merlín! De todas las personas en el mundo... jamás pensé que ibas a ser tú, la misma persona que me rescato quien me iba a mentir de esta forma... Me siento traicionado."
    m "Perdón Arthur. Mis más sinceras disculpas. Pero... una cosa no quita la otra. No necesitas ninguna profecía antigua para convertirte en el rey y salvador de estas tierras ¡Ya eres un líder y te estás convirtiendo en el salvador! Que importa lo que una profecía diga."
    menu:
        "Entrar en razón, relajarse y darle una oportunidad":
            jump good_ending
        
        "Explotar de rabia e intentar asesinar a Merlín":
            jump bad_ending

        "Dejarlo atrás, ya no te interesa ser ni el rey salvador ni un villano. Alejarte. Escapar":
            jump huida


#End
    return



label good_ending:
    a "Merlín... me decepciona saber que no soy 'El Elegido' de la profecía, no te voy a mentir. Creia que tenía un derecho divino."
    a "Sin embargo, ahora comprendo a lo que te referias. Es mas importante ganarse el derecho mediante las cualidades entrenadas por uno mismo a aquellas que se le achacan a uno mediante fuentes desconocidas."
    a "No necesito una profecía para desear ayudar a mi pueblo. Nunca la necesite."
    a "¡Vamos a continuar el camino que empezamos, detener a La Orden y restaurar el reino en su gloria total!"
    a "¡Vamos a convertirnos en el escudo de las personas y traer justicia al reino!"

    "Aqui comienza el viaje...\nContinuara..."

#End
    return



label bad_ending:
    "Arthur se deja llevar por la furia... una furia potenciada por el combustible más  potente de todos. La traición."
    "En un arrebato de fuerza y sorpresa para el mago, Arthur agarra la cabeza del mago y la estampa contra la pared, pulverizándole  el miembro superior y dejándolo  sin vida"
    a "Aquí le declaro la guerra a La Mesa Redonda. Una organización fundada por una rata traidora como esta no puede ser redimida"
    a "Al parecer La Orden tenía razón."
    "Y así, Arthur decide emprender un nuevo camino. Un camino lleno de dolor y sufrimiento, pero tal es el odio y el resentimiento que le genera la traición  de la mesa redonda que es capaz de apaciguar todo ese dolor para ver su fin realizado..."
    "Ver la mesa redonda arder\nContinuara..."

#End
    return



label huida:
    a "No. No puedo ser rey. No estoy capacitado, nunca lo estaré. No soy ningún  elegido de nada."
    "Sumido completamente en la ansiedad, la presión  y la desesperación, Arthur decide escapar esa misma noche."
    "Dejando atrás  toda su vida, con la esperanza de encontrar una... más  simple."
    "Una vida sin tanta preocupación"
    "Un par de horas despues, Arthur llega a 'La frontera del mundo', la division de los reinos"
    "Sin embargo, al estar a punto de cruzar la frontera, unas siluetas sigilosas se asoman  de las esquinas y encierran a Arthur." 
    "La Orden lo había  encontrado"

    menu:
        "Tengo que defenderme":
            "Pero claro... Arthur abandono de forma temprana su entrenamiento. No tiene defensa ni escapatoria"


    a "*Comienza a temblar de miedo y ansiedad.*"
    a "No puedo volver otra vez con La Orden"
    "Y todos los recuerdos dolorosos, marcados en su alma como una cicatriz, empezaron a fluir como un rio"
    "El trabajo forzado"
    "El cansancio fisico"
    "La tortura mental"
    "Arthur poso su mano sobre las cicatrices en toda su espalda causadas por los latigazos, sintiendo su relieve irregular y se decidió"
    a "No puedo volver a ese infierno"
    a "No puedo."

    menu:
        "*Acabar con todo*":
            "Y asi, Arthur en un fluido movimiento se corta las venas."

    
    "Y asi, Arthur en un fluido movimiento se corta las venas. Una solución mejor que volver al sufrimiento generado por La Orden, mejor que ser usado como un arma contra las personas."
    "Fin."
    #End
    return