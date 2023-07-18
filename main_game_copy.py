import pygame

pygame.init()
# 화면 크기 설정
screen_width = 1920 # 가로 크기
screen_height = 1080 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

pygame.display.set_caption("Chronoscape")

# FPS
clock = pygame.time.Clock()
######################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임, 게임 이미지, 좌표, 속도, 폭트 등)
    # 배경 이미지 불러오기
main_poster = pygame.image.load("game_git/resources/images/tutorial_background.png")
main_poster = pygame.transform.scale(main_poster, (1920, 1080))
start_button = pygame.image.load("game_git/resources/images/start_button.png")
start_button = pygame.transform.scale(start_button, (256, 142))
start_button_size = start_button.get_rect().size
start_button_width = start_button_size[0] # 캐릭터의 가로 크기
    # 캐릭터 불러오기
    # 적 불러오기

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수를 설정


    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님


    # 3. 게임 캐릭터 위치 정의
        # 가로 경계값 처리
        # 세로 경계값 처리


    # 4. 충돌처리


    # 5. 화면에 그리기
    screen.blit(main_poster, (0, 0)) # 배경 그리기
    screen.blit(start_button, ((screen_width / 2) - (start_button_width / 2), (screen_height / 1.5)))
    pygame.display.update() # 게임화면을 다시 그리기!
    
pygame.quit()