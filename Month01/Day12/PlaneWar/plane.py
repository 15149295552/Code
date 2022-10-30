import pygame
from gameconfig import *


class Plane(pygame.sprite.Sprite):
    '''  英雄飞机类(继承的精灵类) '''
    # 定义飞机的生命数
    plane_life = 3

    def __init__(self):
        # 调用父类的构造方法
        super().__init__()
        # 存储飞机图片对象(获取飞机图片的实体区域)
        self.list_image = [
            pygame.image.load('./images/hero1.png').convert_alpha(),
            pygame.image.load('./images/hero2.png').convert_alpha()
        ]
        # 存储飞机被摧毁的图片对象
        self.list_hit_image = [
            pygame.image.load('./images/hero_blowup_n1.png').convert_alpha(),
            pygame.image.load('./images/hero_blowup_n2.png').convert_alpha(),
            pygame.image.load('./images/hero_blowup_n3.png').convert_alpha(),
            pygame.image.load('./images/hero_blowup_n4.png').convert_alpha(),
        ]
        # 图片列表的索引值
        self.switch_image = 0
        # 定义飞机的尺寸
        self.rect = self.list_image[self.switch_image].get_rect()
        # 英雄飞机的x值( (屏幕宽度 - 飞机图片宽度) // 2)
        self.rect.left = (SCREEN_WIDTH - self.list_image[self.switch_image].get_width()) // 2
        # 英雄飞机的y值( 屏幕高度 - 飞机图片高度 - 60)
        self.rect.top = SCREEN_HEIGHT - self.list_image[self.switch_image].get_height() - 60
        # 设置飞机移动的速度
        self.speed = 10
        # 定义飞机的存活状态
        self.active = True
        # 定义获取飞机图片的实体
        self.mask = pygame.mask.from_surface(self.list_image[self.switch_image])
        # 飞机被摧毁的图片列表的索引值
        self.switch_hit_image = 0
        # 定义飞机无敌属性
        self.invincible = False

    def reset(self):
        self.active = True
        self.invincible = True
        self.rect.left = (SCREEN_WIDTH - self.list_image[self.switch_image].get_width()) // 2
        self.rect.top = SCREEN_HEIGHT - self.list_image[self.switch_image].get_height() - 60

    def draw_plane(self, screen, delay, enemies, invincible_event, me_down_sound):
        # 英雄飞机与敌机碰撞检测
        enemy_hit = pygame.sprite.spritecollide(self, enemies, False, pygame.sprite.collide_mask)

        if enemy_hit and not self.invincible:  # 存储敌机被碰撞的对象
            self.active = False
            for e in enemy_hit:  # 遍历被碰撞的敌机对象
                e.active = False  # 敌机损毁

        # 绘制我方飞机
        if self.active:
            # 当变量为5的倍数时,切换第2张英雄飞机图片对象
            if delay % 5 == 0:
                self.switch_image = 1
            # 当变量不为5的倍数时,切换第1张英雄飞机图片对象
            else:
                self.switch_image = 0

            screen.blit(self.list_image[self.switch_image], self.rect)
        else:  # 飞机被碰撞
            if not (delay % 5):
                screen.blit(self.list_hit_image[self.switch_hit_image], self.rect)
                self.switch_hit_image = (self.switch_hit_image + 1) % 4
                if self.switch_hit_image == 0:
                    Plane.plane_life -= 1
                    me_down_sound.play()
                    self.reset()
                    pygame.time.set_timer(invincible_event, 3 * 1000)

    def move_up(self):
        '''
            英雄向上移动 (x不变,y减小)
        :return: None
        '''
        self.rect.top -= self.speed

        # 向上移动越界判断[顶住窗口最上边,则y设置为0,不能向上移动]
        if self.rect.top <= 0:
            self.rect.top = 0

    def move_down(self):
        '''
            英雄向下移动 (x不变,y增大)
        :return: None
        '''
        self.rect.top += self.speed

        # 向下移动越界判断: 不能超出屏幕高度(预留60个像素)
        if self.rect.top >= SCREEN_HEIGHT - self.list_image[self.switch_image].get_height() - 60:
            self.rect.top = SCREEN_HEIGHT - self.list_image[self.switch_image].get_height() - 60

    def move_left(self):
        '''
            英雄向左移动(x减小,y不变)
        :return: None
        '''
        self.rect.left -= self.speed

        # 左移动越界判断: 不能超出屏幕左侧区域
        if self.rect.left <= 0:
            self.rect.left = 0

    def move_right(self):
        '''
            英雄向右移动(x增大,y不变)
        :return: None
        '''
        self.rect.left += self.speed

        # 右移动越界判断: 不能超出屏幕右侧区域
        if self.rect.left >= SCREEN_WIDTH - self.list_image[self.switch_image].get_width():
            self.rect.left = SCREEN_WIDTH - self.list_image[self.switch_image].get_width()

    @classmethod
    def show_plane_life(cls, screen, images):
        for i in range(cls.plane_life):
            screen.blit(images, ((SCREEN_WIDTH - (cls.plane_life - i) * images.get_width() - 10),
                                 SCREEN_HEIGHT - images.get_height() - 5))
