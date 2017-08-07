import  pygame


class Ship():

    def __init__(self, ai_setting, screen):
        """初始化飞船并设置飞船的位置"""
        self.screen = screen
        self.ai_setting = ai_setting
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞创放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        # 限制飞船的活动范围，self.rect.right 返回飞船外接矩形的右边缘的x坐标
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # 更新 center的值
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setting.ship_speed_factor
        # 根据 sefl.centerx更新rect 对象
        self.rect.centerx = self.center

