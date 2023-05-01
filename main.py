from cellular_automata import *
import pygame


def render_field(field):
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                print(' ', end='')
            elif field[y][x] == 1:
                print('X', end='')
        print()
    print('----------------------')


def render_pygame(field, scr):
    scale = 15
    for y in range(0, len(field)):
        for x in range(0, len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(scr, (255, 255, 255), (x*scale, y*scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(scr, (0, 0, 255), (x * scale, y * scale, scale, scale))
            # Рисуем обводку
            pygame.draw.rect(scr, (0, 0, 0), (x * scale, y * scale, scale, scale), 1)

def main():
    gof = GameOfLife(30, 30)
    gof.initialize(0)
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    is_running = True
    # В начале программы ставим игру на паузу
    is_paused = True
    # Переменная, в которой хранится шрифт
    main_font = pygame.font.Font(None, 24)

    while is_running:
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                is_running = False
            # Если тип события - нажатая клавиша
            if event.type == pygame.KEYDOWN:
                # Если эта клавиша - пробел
                if event.key == pygame.K_SPACE:
                    # Если была пауза, то снимаем
                    if is_paused == True:
                        is_paused = False
                    # Если паузы не было, то ставим на паузу
                    else:
                        is_paused = True
            # Если нажата кнопка мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Записываем позицию курсора в пикселях
                cursor_pos = event.pos
                # Считаем индекс клетки по Х
                x_pos = cursor_pos[0] // 15
                # Считаем индекс клетки по Y
                y_pos = cursor_pos[1] // 15
                # Создаем переменную, в которую пишем новое состояние
                # Сначала пишем туда текущее состояние клетки, что не было ошибок,
                # если нажатие не будет обработано (например, нажата вторая кнопка мыши)
                new_state = gof.field[y_pos][x_pos]
                # Если нажата левая кнопка, то новое состояние - живая
                if event.button == 1:
                    new_state = 1
                # Если нажата правая кнопка, то новое состояние - неживая
                elif event.button == 3:
                    new_state = 0
                # Пишем в массив новое состояние клетки
                gof.field[y_pos][x_pos] = new_state
        # Если игра на паузе, то не обновляем состояние автомата, но рисовка
        # все равно должна быть!
        if is_paused == False:
            gof.run_transition_rule()
        screen.fill((0, 0, 0))
        render_pygame(gof.field, screen)

        text1 = main_font.render('Я люблю писать программы', True, (255, 255, 255))
        screen.blit(text1, (10, 450))

        pygame.display.flip()
        # держим цикл на правильной скорости
        clock.tick(60)
        pygame.time.delay(50)




if __name__ == '__main__':
    main()

