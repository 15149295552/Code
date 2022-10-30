import pygame
from gameconfig import *
import sys
import random
from plane import Plane
from pygame.locals import *
from enemy import SmallEnemy, MiddleEnemy, BigEnemy
from bullet import Bullet1, Bullet2
from supply import Bullet_Supply, Bomb_Supply

# 模块初始化
pygame.init()
# 音效模块初始化
pygame.mixer.init()

class Background:  # 背景类
    def __init__(self):
        # 背景图片1
        self.image1 = pygame.image.load('./images/background.png')
        # 背景图片2
        self.image2 = pygame.image.load('./images/background.png')
        # 背景图片的x轴的值
        self.x = 0
        # 背景图片1的y轴的值 (初始加载在窗口内)
        self.y1 = 0
        # 背景图片2的y轴的值 (初始加载在窗口外,负图片高度的位置)
        self.y2 = -self.image2.get_height()

    def move(self):
        '''
            定义背景图片的动态移动位置计算
        :return: None
        '''
        # 第1张和第2张背景图同时向下移动 (y轴的值增加)
        self.y1 += 1
        self.y2 += 1
        # 第一张背景图超过屏幕之外,设置其y轴值为负的图片的高度 (窗口外)
        if self.y1 >= SCREEN_HEIGHT:
            self.y1 = -self.image1.get_height()

        # 第二张背景图超过屏幕之外,设置其y轴值为负的图片的高度 (窗口外)
        if self.y2 >= SCREEN_HEIGHT:
            self.y2 = - self.image2.get_height()

    def draw_bgimage(self, screen):
        '''
            绘制背景图片对象
        :param screen: 窗口对象
        :return: None
        '''
        # 加载背景图, 并设置图片显示的位置
        screen.blit(self.image1, (self.x, self.y1))
        screen.blit(self.image2, (self.x, self.y2))


class PauseResume:
    ''' 游戏暂停与运行类 '''
    # 标识游戏是否暂停
    paused = False

    def __init__(self):
        self.pause_nor = pygame.image.load('./images/game_pause_nor.png').convert_alpha()
        self.pause_pressed = pygame.image.load('./images/game_pause_pressed.png').convert_alpha()
        self.resume_nor = pygame.image.load('./images/game_resume_nor.png').convert_alpha()
        self.resume_pressed = pygame.image.load('./images/game_resume_pressed.png').convert_alpha()
        # 获取游戏中,鼠标未移动的暂停图片的尺寸
        self.paused_rect = self.pause_nor.get_rect()
        # 定义游戏中,鼠标未移动的暂停图片的位置(左/上位置)
        self.paused_rect.left = SCREEN_WIDTH - self.paused_rect.width - 10
        self.paused_rect.top = 10
        # 用于运行时的图片切换
        self.switch_image = self.pause_nor

    def draw(self, screen):
        screen.blit(self.switch_image, self.paused_rect)


class PlaneWar:
    # 存储所有敌机的精灵组
    enemies = pygame.sprite.Group()
    # 存储小型敌机的精灵组
    small_enemies = pygame.sprite.Group()
    # 小型敌机销毁图片对象的索引值
    e1_destroy_index = 0
    # 存储中型敌机的精灵组
    middle_enemies = pygame.sprite.Group()
    # 中型敌机销毁图片对象的索引值
    e2_destroy_index = 0
    # 存储大型敌机的精灵组
    big_enemies = pygame.sprite.Group()
    # 大型敌机销毁图片对象的索引值
    e3_destroy_index = 0
    # 定义分数
    score = 0

    def __init__(self):
        # 定义窗口大小
        self.screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        # 创建窗口(480x700)
        self.screen = pygame.display.set_mode(self.screen_size)
        # 设置窗口的图标
        icon = pygame.image.load('./images/icon72x72.png')
        pygame.display.set_icon(icon)
        # 设置窗口的名称
        pygame.display.set_caption('飞机大战V1')
        # 定义时钟对象(控制屏幕的FPS)
        self.clock = pygame.time.Clock()
        # 创建背景图片对象
        self.bg = Background()
        # 创建英雄飞机对象
        self.hero = Plane()
        # 创建小型敌机对象
        # self.sm_enemy = SmallEnemy()
        # 添加5个小型敌机对象
        SmallEnemy.add_small_enemy(PlaneWar.enemies, PlaneWar.small_enemies, 5)
        # 添加3个中型敌机对象
        MiddleEnemy.add_middle_enemy(PlaneWar.enemies, PlaneWar.middle_enemies, 3)
        # 添加2个大型敌机对象
        BigEnemy.add_big_enemy(PlaneWar.enemies, PlaneWar.big_enemies, 2)
        # 调用添加单发子弹方法 (生成10颗子弹)
        Bullet1.add_bullet1(self.hero)
        # 调用添加双发子弹方法 (生成20颗子弹)
        Bullet2.add_bullet2(self.hero)
        # 定义字体格式
        self.font_type = pygame.font.Font('./font/font.ttf', 36)
        # 定义游戏暂停与运行的对象
        self.pr = PauseResume()
        # 定义超级子弹对象
        self.bullet_supply = Bullet_Supply()
        # 自定义事件 - 补给包发放定时器
        self.BULLET_SUPPLY = USEREVENT
        # 设置每30秒发放超级子弹补给包
        pygame.time.set_timer(self.BULLET_SUPPLY, 5 * 1000)
        # 定义是否获得超级子弹补给包
        self.is_double_bullet = False
        # 超级子弹持有的定时器
        self.DOUBLE_BULLET = USEREVENT + 1
        # 定义超级炸弹对象
        self.bomb_supply = Bomb_Supply()
        # 解除我方无敌状态定时器
        self.INVINCIBLE_TIME = USEREVENT + 2
        # 定义超级炸弹的图片对象
        self.bomb_image = pygame.image.load('./images/bomb.png').convert_alpha()
        # 定义飞机生命的图片对象
        self.plane_life_image = pygame.image.load('./images/life.png').convert_alpha()
        # 定义重新开始的图片对象
        self.again_image = pygame.image.load("./images/restart_nor.png").convert_alpha()
        self.again_rect = self.again_image.get_rect()
        # 定义游戏结束的图片对象
        self.gameover_image = pygame.image.load("./images/gameover.png").convert_alpha()
        self.gameover_rect = self.gameover_image.get_rect()
        # 调用背景音效配置方法
        self.music_config()
        # 文件打开设置
        self.recorded = False

    def music_config(self):
        # 载入游戏音乐
        pygame.mixer.music.load("sound/game_music.ogg")
        pygame.mixer.music.set_volume(0.2)
        self.bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
        self.bullet_sound.set_volume(0.2)
        self.bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
        self.bomb_sound.set_volume(0.2)
        self.supply_sound = pygame.mixer.Sound("sound/supply.wav")
        self.supply_sound.set_volume(0.2)
        self.get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
        self.get_bomb_sound.set_volume(0.2)
        self.get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
        self.get_bullet_sound.set_volume(0.2)
        self.upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
        self.upgrade_sound.set_volume(0.2)
        self.enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
        self.enemy3_fly_sound.set_volume(0.2)
        self.enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
        self.enemy1_down_sound.set_volume(0.2)
        self.enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
        self.enemy2_down_sound.set_volume(0.2)
        self.enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
        self.enemy3_down_sound.set_volume(0.5)
        self.me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
        self.me_down_sound.set_volume(0.2)

    # 事件
    def __event_handle(self):
        '''
            事件处理功能
        :return: None
        '''
        # 循环判断用户操作事件
        for event in pygame.event.get():
            # 判断用户是否退出[点击关闭按钮]
            if event.type == pygame.QUIT:
                # 结束进程
                sys.exit('欢迎下次继续')

            # 检测鼠标动作
            elif event.type == pygame.MOUSEMOTION:
                # 鼠标移动到暂停未选中的图片上
                if self.pr.paused_rect.collidepoint(event.pos):
                    # 游戏中,判断是否暂停
                    if PauseResume.paused:
                        # 重启选中的图片对象(深色的 >)
                        self.pr.switch_image = self.pr.resume_pressed
                    else:  # 游戏中,不暂停
                        # 游戏中选中(深色的||)
                        self.pr.switch_image = self.pr.pause_pressed
                else:  # 鼠标未移动到暂停未选中的图片上
                    # 暂停,显示[重启]
                    if PauseResume.paused:
                        # 暂停游戏 (浅色的 >)
                        self.pr.switch_image = self.pr.resume_nor
                    else:
                        # 运行游戏 (浅色的 ||)
                        self.pr.switch_image = self.pr.pause_nor

            # 检测鼠标是否点击
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 表示鼠标单击,游戏中暂停的图片对象
                if event.button == 1 and self.pr.paused_rect.collidepoint(event.pos):
                    # 暂停与重新开始切换
                    PauseResume.paused = not PauseResume.paused

            # 检测用户自定义事件 -- 超级子弹
            elif event.type == self.BULLET_SUPPLY:
                self.supply_sound.play()
                if random.choice((True, False)):
                    self.bullet_supply.reset()
                else:
                    self.bomb_supply.reset()

            # 检测用户自定义事件 -- 超级子弹持有
            elif event.type == self.DOUBLE_BULLET:
                self.is_double_bullet = False
                pygame.time.set_timer(self.DOUBLE_BULLET, 0)   # 取消定时器

            # 按下空格,则使用超级炸弹
            elif event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    if Bomb_Supply.bobm_number > 0:
                        Bomb_Supply.bobm_number -= 1
                        self.bomb_sound.play()
                        for e in self.enemies:
                            # 判断敌机进入屏幕则销毁
                            if e.rect.top >= 0:
                                e.active = False

            # 检测用户自定义事件 -- 3秒无敌
            elif event.type == self.INVINCIBLE_TIME:
                self.hero.invincible = False
                pygame.time.set_timer(self.INVINCIBLE_TIME, 0)

    # 绘制方法
    def __draw_element(self):
        '''
            绘制各种对象(背景图/飞机/子弹/补给等)
        :return: None
        '''
        self.bg.draw_bgimage(self.screen)  # 绘制背景

        if not PauseResume.paused and Plane.plane_life:  # 游戏不暂停
            global DELAY
            DELAY += 1
            self.hero.draw_plane(self.screen, DELAY, PlaneWar.enemies, self.INVINCIBLE_TIME, self.me_down_sound)  # 绘制英雄飞机

            if self.hero.active:  # 飞机存活则绘制子弹
                # 未获取到双发子弹补给包,则绘制单发子弹,否则绘制双发子弹
                if not self.is_double_bullet:
                    # 绘制单发子弹
                    Bullet1.draw_bullet1(self.hero, self.screen, DELAY,
                                         PlaneWar.enemies, PlaneWar.middle_enemies, PlaneWar.big_enemies)
                else:
                    # 绘制双发子弹
                    Bullet2.draw_bullet2(self.hero, self.screen, DELAY,
                                         PlaneWar.enemies, PlaneWar.middle_enemies, PlaneWar.big_enemies)

            # 绘制大型敌机
            for benemy in PlaneWar.big_enemies:
                # 表示敌机存活则绘制
                if benemy.active:
                    if benemy.hit:  # 被攻击,绘制攻击的图片对象
                        self.screen.blit(benemy.hit_image, benemy.rect)
                        benemy.hit = False
                    else:
                        benemy.draw_big_enemy(self.screen)
                    benemy.move()

                    # 绘制血槽 (窗口对象, 颜色, (起始点x, 起始点y), (终点x, 终点y), 线宽)
                    pygame.draw.line(self.screen, WHITE,
                                     (benemy.rect.left, benemy.rect.top - 5),
                                     (benemy.rect.left + benemy.image.get_width(),
                                      benemy.rect.top - 5), 2)

                    # 当血量小于20%,则显示红色,否则显示绿色
                    remain_life = benemy.life / BigEnemy.life
                    if remain_life <= 0.2:
                        color = RED
                    else:
                        color = GREEN

                    pygame.draw.line(self.screen, color,
                                     (benemy.rect.left, benemy.rect.top - 5),
                                     (benemy.rect.left + benemy.image.get_width() * remain_life,
                                      benemy.rect.top - 5), 2)
                    # 即将出现在画面中，播放音效
                    if benemy.rect.bottom == -50:
                        self.enemy3_fly_sound.play(-1)
                else:  # 敌机销毁,则绘制特效
                    PlaneWar.score += 200
                    if not (DELAY % 5):  # 每计数到5的倍数,则切换销毁图片
                        # 绘制销毁的图片
                        self.screen.blit(benemy.destroy_images[PlaneWar.e3_destroy_index], benemy.rect)
                        # 切换销毁的图片显示: 修改销毁图片的索引值
                        PlaneWar.e3_destroy_index = (PlaneWar.e3_destroy_index + 1) % 6
                        # 当循环再次计算到0,敌机重置
                        if PlaneWar.e3_destroy_index == 0:
                            self.enemy3_down_sound.play()
                            benemy.reset()

            # 绘制中型敌机
            for menemy in PlaneWar.middle_enemies:
                # 表示敌机存活则绘制
                if menemy.active:
                    if menemy.hit:  # 绘制被攻击的图片
                        self.screen.blit(menemy.hit_image, menemy.rect)
                        menemy.hit = False
                    else:
                        menemy.draw_middle_enemy(self.screen)
                    menemy.move()

                    # 绘制血槽 (窗口对象, 颜色, (起始点x, 起始点y), (终点x, 终点y), 线宽)
                    pygame.draw.line(self.screen, WHITE,
                                     (menemy.rect.left, menemy.rect.top - 5),
                                     (menemy.rect.left + menemy.image.get_width(),
                                      menemy.rect.top - 5), 2)

                    # 当血量小于20%,则显示红色,否则显示绿色
                    remain_life = menemy.life / MiddleEnemy.life
                    if remain_life <= 0.2:
                        color = RED
                    else:
                        color = GREEN

                    pygame.draw.line(self.screen, color,
                                     (menemy.rect.left, menemy.rect.top - 5),
                                     (menemy.rect.left + menemy.image.get_width() * remain_life,
                                      menemy.rect.top - 5), 2)

                else:  # 敌机销毁,则绘制特效
                    PlaneWar.score += 100
                    if not (DELAY % 5):  # 每计数到5的倍数,则切换销毁图片
                        # 绘制销毁的图片
                        self.screen.blit(menemy.destroy_images[PlaneWar.e2_destroy_index], menemy.rect)
                        # 切换销毁的图片显示: 修改销毁图片的索引值
                        PlaneWar.e2_destroy_index = (PlaneWar.e2_destroy_index + 1) % 4
                        # 当循环再次计算到0,敌机重置
                        if PlaneWar.e2_destroy_index == 0:
                            self.enemy2_down_sound.play()
                            menemy.reset()

            # 绘制小型敌机
            for senemy in PlaneWar.small_enemies:
                # 表示敌机存活则绘制
                if senemy.active:
                    senemy.draw_small_enemy(self.screen)
                    senemy.move()
                else:  # 敌机销毁,则绘制特效
                    PlaneWar.score += 50
                    if not (DELAY % 5):  # 每计数到3的倍数,则切换销毁图片
                        # 绘制销毁的图片
                        self.screen.blit(senemy.destroy_images[PlaneWar.e1_destroy_index], senemy.rect)
                        # 切换销毁的图片显示: 修改销毁图片的索引值
                        PlaneWar.e1_destroy_index = (PlaneWar.e1_destroy_index + 1) % 4
                        # 当循环再次计算到0,敌机重置
                        if PlaneWar.e1_destroy_index == 0:
                            self.enemy1_down_sound.play()
                            senemy.reset()

            # 绘制补给包
            if self.bullet_supply.active:
                self.screen.blit(self.bullet_supply.image, self.bullet_supply.rect)
                self.bullet_supply.move()
                # 飞机与超级子弹补给包是否碰撞
                if pygame.sprite.collide_mask(self.bullet_supply, self.hero):
                    self.get_bullet_sound.play()
                    self.bullet_supply.active = False
                    self.is_double_bullet = True
                    # 表示定义超级子弹可用18s
                    pygame.time.set_timer(self.DOUBLE_BULLET, 18 * 1000)

            # 绘制超级炸弹
            if self.bomb_supply.active:
                self.bomb_supply.move()
                self.screen.blit(self.bomb_supply.image, self.bomb_supply.rect)
                # 飞机与超级炸弹补给包是否碰撞
                if pygame.sprite.collide_mask(self.bomb_supply, self.hero):
                    self.bomb_supply.active = False
                    self.get_bomb_sound.play()
                    if Bomb_Supply.bobm_number < 3:
                        Bomb_Supply.bobm_number += 1
                    else:
                        Bomb_Supply.bobm_number = 3

            # 绘制超级炸弹图片
            Bomb_Supply.show_bomb_info(self.bomb_image, self.screen, self.font_type)

            # 绘制英雄飞机生命图片
            Plane.show_plane_life(self.screen, self.plane_life_image)

            if DELAY == 100:
                DELAY = 0

            # 绘制分数
            text = self.font_type.render('SCORE: %d' % PlaneWar.score, True, WHITE)
            self.screen.blit(text, (10, 5))

        elif Plane.plane_life == 0:    # 游戏结束
            # 背景音乐停止
            pygame.mixer.music.stop()

            # 停止全部音效
            pygame.mixer.stop()

            # 停止发放补给
            pygame.time.set_timer(self.BULLET_SUPPLY, 0)

            record_score = 0
            if not self.recorded:
                self.recorded = True
                # 读取文件最高分记录
                with open('record.txt', 'r') as f:
                    record_score = int(f.read())

                # 如果玩家的分数比当前高,则存档
                if self.score > record_score:
                    with open('record.txt', 'w') as f:
                        f.write(str(self.score))

            # 绘制最好成绩
            record_score_text = self.font_type.render('Best SCORE:', True, WHITE)
            self.screen.blit(record_score_text, (50, 50))
            record_score_text = self.font_type.render(str(record_score), True, WHITE)
            self.screen.blit(record_score_text, (90, 50))
            # 绘制本次游戏的文本
            game_score_text = self.font_type.render('YOU SCORE:', True, WHITE)
            game_score_text_rect = game_score_text.get_rect()
            game_score_text_rect.left = (SCREEN_WIDTH - game_score_text_rect.width) // 2
            game_score_text_rect.top = SCREEN_HEIGHT // 3 + 80
            self.screen.blit(record_score_text, game_score_text_rect)
            # 绘制本次游戏的数据
            game_score_data = self.font_type.render(str(self.score), True, WHITE)
            game_score_data_rect = game_score_data.get_rect()
            game_score_data_rect.left = (SCREEN_WIDTH - game_score_data_rect.width) // 2
            game_score_data_rect.top = game_score_data_rect.bottom + 10
            self.screen.blit(game_score_data, game_score_data_rect)
            # 绘制重新开始图片对象
            self.again_rect.left = (SCREEN_WIDTH - self.again_rect.width) // 2
            self.again_rect.top = self.again_rect.bottom + 400
            self.screen.blit(self.again_image, self.again_rect)
            # 绘制游戏结束图片对象
            self.gameover_rect.left = (SCREEN_WIDTH - self.gameover_rect.width) // 2
            self.gameover_rect.top = self.gameover_rect.bottom + 500
            self.screen.blit(self.gameover_image, self.gameover_rect)

            # 检测用户鼠标操作
            if pygame.mouse.get_pressed()[0]:   # 获取左键
                # 获取鼠标的坐标
                pos = pygame.mouse.get_pos()
                # 判断用户点击"重新开始"
                if self.again_rect.left < pos[0] < self.again_rect.right and \
                        self.again_rect.top < pos[1] < self.again_rect.bottom:
                    PlaneWar()

                # 判断用户点击"游戏结束"
                if self.gameover_rect.left < pos[0] < self.gameover_rect.right and \
                        self.gameover_rect.top < pos[1] < self.gameover_rect.bottom:
                    pygame.quit()
                    sys.exit('欢迎再来')

        # 绘制游戏暂停与开始
        self.pr.draw(self.screen)

    def __calculate_location(self):
        '''
            计算各种对象的显示位置
        :return:
        '''
        # 计算背景图对象的位置
        self.bg.move()

    def __display_control(self):
        '''
            显示控制
        :return: None
        '''
        # 刷新屏幕
        pygame.display.update()
        # 设置fps (60帧/秒)
        self.clock.tick(60)

    def __game_pressed(self):
        '''
            用户的键盘操作检测
        :return: None
        '''
        # 检测用户的键盘操作
        key_pressed = pygame.key.get_pressed()
        # 判断用户按 w 或 上方向键 则飞机上移
        if key_pressed[K_w] or key_pressed[K_UP]:
            self.hero.move_up()
        # 判断用户按 s 或 下方向键 则飞机下移
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            self.hero.move_down()
        # 判断用户按 a 或 左方向键 则飞机左移
        elif key_pressed[K_a] or key_pressed[K_LEFT]:
            self.hero.move_left()
        # 判断用户按 d 或 右方向键 则飞机右移
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            self.hero.move_right()

    def runScence(self):
        pygame.mixer.music.play(-1)
        while True:
            # 调用用户键盘操作检测方法
            self.__game_pressed()
            # 调用事件处理方法
            self.__event_handle()
            # 调用计算位置方法
            self.__calculate_location()
            # 调用对象的绘制方法
            self.__draw_element()
            # 调用显示控制方法
            self.__display_control()