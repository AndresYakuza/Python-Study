import random

# Inicializar puntuaciones
user_score = 0
machine_score = 0

# Opciones posibles
options = ['piedra', 'papel', 'tijeras']


while True: 
    try:
        rounds = int(input('🎯 Cantidad de rondas a jugar: '))

        for i in range(1, rounds + 1):
            machine_opcion = random.choice(options)
            print(f'\n🔁 Ronda número {i} 🔁')

            while True: 
                try: 
                    user_opcion = input('👉 Digita "Piedra", "Papel" o "Tijeras": ')
                    user_opcion = user_opcion.lower().strip()

                    if user_opcion not in ('piedra', 'papel', 'tijeras', 'salir'):
                        raise ValueError("❌ Opción no válida, intenta de nuevo...")
                        
                        
                    if user_opcion != 'salir':

                        if user_opcion == 'piedra':

                            if machine_opcion == 'piedra':
                                print('🤖 La máquina ha elegido piedra.')
                                print('🤝 ¡Empate!')

                            elif machine_opcion == 'papel':
                                print('🤖 La máquina ha elegido papel.')
                                print('❌ Pierdes esta ronda.')
                                machine_score += 1

                            elif machine_opcion == 'tijeras':
                                print('🤖 La máquina ha elegido tijeras.')
                                print('✅ ¡Ganaste esta ronda!')
                                user_score += 1


                        elif user_opcion == 'papel':

                            if machine_opcion == 'piedra':
                                print('🤖 La máquina ha elegido piedra.')
                                print('✅ ¡Ganaste esta ronda!')
                                user_score += 1

                            elif machine_opcion == 'papel':
                                print('🤖 La máquina ha elegido papel.')
                                print('🤝 ¡Empate!')

                            elif machine_opcion == 'tijeras':
                                print('🤖 La máquina ha elegido tijeras.')
                                print('❌ Pierdes esta ronda.')
                                machine_score += 1


                        elif user_opcion == 'tijeras': 

                            if machine_opcion == 'piedra':
                                print('🤖 La máquina ha elegido piedra.')
                                print('❌ Pierdes esta ronda.')
                                machine_score += 1

                            elif machine_opcion == 'papel':
                                print('🤖 La máquina ha elegido papel.')
                                print('✅ ¡Ganaste esta ronda!')
                                user_score += 1

                            elif machine_opcion == 'tijeras':
                                print('🤖 La máquina ha elegido tijeras.')
                                print('🤝 ¡Empate!')
                            
                        print(f'📊 Marcador actual: Jugador {user_score} - Máquina {machine_score}')

                    else:
                        print('🚪 ¿Te vas antes? No pasa nada… igual te muestro cómo ibas y te lanzo una despedida divertida 😄')
                        print('\n🏁 JUEGO FINALIZADO 🏁')
                        print(f'📊 Resultado sin concluir todas las rondas: Jugador {user_score} - Máquina {machine_score}')
                        
                        if machine_score > user_score:
                            print('😈 La máquina te ha vencido... BUJAJAJAJA. ¡Suerte para la próxima!')
                        elif machine_score < user_score:
                            print('🎉 ¡Has vencido a la máquina! Felicidades, humano.')
                        else:
                            print('🤝 Empate total. ¡Una revancha decidirá al verdadero campeón!')
                        exit()


                    break  # sale del while True interno si la jugada fue válida


                except ValueError as e:
                    print(f"Error: {e}")
                    continue  # vuelve a pedir entrada si hay error

        # Resultado final

        print('\n🏁 JUEGO FINALIZADO 🏁')
        print(f'📊 Resultado final: Jugador {user_score} - Máquina {machine_score}')
        
        if machine_score > user_score:
            print('😈 La máquina te ha vencido... BUJAJAJAJA. ¡Suerte para la próxima!')
        elif machine_score < user_score:
            print('🎉 ¡Has vencido a la máquina! Felicidades, humano.')
        else:
            print('🤝 Empate total. ¡Una revancha decidirá al verdadero campeón!')

        break  # salir del while principal tras terminar todas las rondas

    except ValueError:
        print('⚠️ Error: ingresa un número válido de rondas.')