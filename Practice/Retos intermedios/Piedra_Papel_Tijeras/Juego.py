import random

user_score = 0
machine_score = 0

options = ['piedra', 'papel', 'tijeras']



while True: 
    try:
        rounds = int(input('Cantidad de rondas a jugar: '))
        for i in range(1, rounds + 1):
            machine_opcion = random.choice(options)
            print(f'Ronda numero {i}...')

            while True: 
                try: 
                    user_opcion = input('Digite "Piedra", "Papel" o "Tijeras": ')
                    user_opcion = user_opcion.lower().strip()

                    if user_opcion not in ('piedra', 'papel', 'tijeras', 'salir'):
                        raise ValueError("Opción no válida, ronda cancelada...")
                        
                        
                    if user_opcion != 'salir':

                        if user_opcion == 'piedra':

                            if machine_opcion == 'piedra':
                                print('La maquina ha elegido piedra...')
                                print('¡Empate!')

                            elif machine_opcion == 'papel':
                                print('La maquina ha elegido papel...')
                                print('Pierdes!')
                                machine_score += 1

                            elif machine_opcion == 'tijeras':
                                print('La maquina ha elegido tijeras...')
                                print('Ganas!')
                                user_score += 1


                        elif user_opcion == 'papel':

                            if machine_opcion == 'piedra':
                                print('La maquina ha elegido piedra...')
                                print('Ganas!')
                                user_score += 1

                            elif machine_opcion == 'papel':
                                print('La maquina ha elegido papel...')
                                print('¡Empate!')


                            elif machine_opcion == 'tijeras':
                                print('La maquina ha elegido tijeras...')
                                print('pierdes!')
                                machine_score += 1


                        elif user_opcion == 'tijeras': 

                            if machine_opcion == 'piedra':
                                print('La maquina ha elegido piedra...')
                                print('Pierdes!')
                                machine_score += 1

                            elif machine_opcion == 'papel':
                                print('La maquina ha elegido papel...')
                                print('Ganas!')
                                user_score += 1

                            elif machine_opcion == 'tijeras':
                                print('La maquina ha elegido tijeras...')
                                print('¡Empate!')
                            
                        print(f'Score: Jugador {user_score} - Maquina {machine_score}')

                    else:
                        print('Ups, has finalizado el juego antes de lo esperado...')
                        exit()


                except ValueError as e:
                    print(f"Error: {e}")
                    continue
            


        print('JUEGO FINALIZADO...')
        print(f'El marcador ha quedado de la siguiente manera: Jugador {user_score} - Maquina {machine_score}')
        if machine_score > user_score:
            print('Ups, perdiste contra la maquina BUJAJAJAJA, buena suerte la proxima vez')
        elif machine_score < user_score:
            print('Uhra, ganaste contra la maquina felicidades.')
        else:
            print('Vaya, vaya.. Han empatado, una proxima vez se decidira quien sera el vencedor.')
        break 

    except ValueError:
        print('Error, ingrese un numero de rondas valido..')








        







    

    


