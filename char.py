import pygame
import sys
import random
sitey=random.randint(0,468)
t = pygame.time.get_ticks()
# 初始化pygame
pygame.init()
# 定义变量
size = width, height = 1500,700
bg = (255, 255, 255)
# 加载logo图
img = pygame.image.load("图拉真.jpg")
img1 = pygame.image.load("怪物.png")

# 获取图像的位置
position = img.get_rect()
position1 = img1.get_rect()

# 创建一个主窗口
screen = pygame.display.set_mode(size)
# 标题
pygame.display.set_caption("图拉真打怪物")
# 创建游戏主循环
site = [0, 0]
site0 = [1168, sitey]
site1 = [0, 0]
# 移动图像
position = position.move(site)
position1 = position1.move(site0)
# 填充背景
screen.fill(bg)
# 放置图片
screen.blit(img, position)
screen.blit(img1, position1)
# 更新显示界面
pygame.display.flip()
while True:

    # 设置初始值
    site = [0, 0]
    site0=[0,0]
    site1=[0,0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 图像移动 KEYDOWN 键盘按下事件
        # 通过 key 属性对应按键
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                site[1] -= 8
                site1[0] -= 8
            if event.key == pygame.K_DOWN:
                site[1] += 8
                site1[0] -= 8
            if event.key == pygame.K_LEFT:
                site[0] -= 8
                site1[0] -= 8
            if event.key == pygame.K_RIGHT:
                site[0] += 8
                site1[0] -= 8
            # 移动图像

            position = position.move(site)
            position1 = position1.move(site1)
            if position[1]+100 in range(position1[1],position1[1]+232):
                img1.fill('white')
                print('win')
                sys.exit()



            # 填充背景
            screen.fill(bg)
            # 放置图片
            screen.blit(img, position)
            screen.blit(img1, position1)
            # 更新显示界面
            pygame.display.flip()
