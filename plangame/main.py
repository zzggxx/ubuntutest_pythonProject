# coding=utf-8
import pygame
import time


def main():
    '''
        1. 搭建界面，主要完成窗口和背景图的显示,代码固定,只是画布大小等调整一下即可
    '''
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)
    # 2. 创建一个和窗口大小的图片，用来充当背景
    background = pygame.image.load("./feiji/background.png").convert()
    # 3. 把背景图片放到窗口中显示
    while True:
        # 设置背景,坐标,坐标和android的一样
        screen.blit(background, (0, 0))
        '''
            2. 用来检测事件，比如按键操作
        '''
        # 获取事件，比如按键等
        for event in pygame.event.get():
            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')
        # 刷新
        pygame.display.update()
        time.sleep(0.04)


# -------------------------------------------------


if __name__ == "__main__":
    main()
