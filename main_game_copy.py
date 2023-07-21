import pygame
import sys
import os
import time

pygame.init() # 초기화

# 파일 경로 탐색
current_path = os.path.dirname(__file__)
resource_path = os.path.join(current_path, "resources/images")

# 타이틀 이름
pygame.display.set_caption("Chronoscape")

# 로고 설정
logo = pygame.image.load(os.path.join(resource_path, "chronoscape_logo.png"))
pygame.display.set_icon(logo)

# 파일 이미지들 로드하기
character_img = pygame.image.load(os.path.join(resource_path, "character.png"))
main_poster_img = pygame.image.load(os.path.join(resource_path, "main_poster.png"))
start_button_img = pygame.image.load(os.path.join(resource_path, "start_button.png"))
start_button_act_img = pygame.image.load(os.path.join(resource_path, "start_button_act.png"))
tutorial_background_img = pygame.image.load(os.path.join(resource_path, "tutorial_background.png"))

# 프레임
clock = pygame.time.Clock()

# 화면 크기
screen_width = 1920 # 가로 크기
screen_height = 1080 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# 이미지 크기 설정
main_poster_img = pygame.transform.scale(main_poster_img, (1920, 1080))
start_button_img = pygame.transform.scale(start_button_img, (256, 142))
start_button_size = start_button_img.get_rect().size
start_button_width = start_button_size[0]
start_button_height = start_button_size[1]
start_button_act_img = pygame.transform.scale(start_button_act_img, (start_button_width, start_button_height))


# 기본 버튼 클래스
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x, y))
            if click[0] and action != None:
                action()
        else:
            screen.blit(img_in, (x, y))

# 종료 함수
def quitGame():
    pygame.quit()
    sys.exit()

# 메인 메뉴 함수
def mainMenu():
    menu = True

    while menu:
        dt = clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            screen.blit(main_poster_img, (0, 0))
            start_button = Button(start_button_img, ((screen_width / 2) - (start_button_width / 2)), (screen_height / 1.5), start_button_width, start_button_height, start_button_act_img, quitGame)
            pygame.display.update()

mainMenu() # 메인 메뉴 함수 불러오기
pygame.quit()
