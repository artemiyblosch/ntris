import pygame as pg
from sprites import *
from time import sleep
from utils import *
from mapgen import *
from assets_lib import *
from modes.mode_obj import Mode
from layouts import Grid

class Game:
    def check_size(self):
        if (a:=self.screen.get_height()) < 600:
            self.size = 8
        elif a < 800:
            self.size = 12
        else:
            self.size = 16

    @property
    def background(self):
        return self.backgrounds[self.size]
    
    @property
    def empty_line(self):
        return self.empty_lines[self.size]

    def create_size(self,size):
        self.backgrounds[size] = pg.Surface((21*size,42*size))
        for i in range(21):
            for j in range(42):
                draw_on(self.backgrounds[size], f"tile_block{size}.jpg", (i*size,j*size), col.bg)

        self.empty_lines[size] = pg.Surface((21*size, size))
        draw_on(self.empty_lines[size],self.backgrounds[size],(0,0))

    def __init__(self, screen : pg.Surface, mode : Mode, fps : int = 60):
        self.fps = fps
        self.mode = mode
        self.screen = screen
        self.size = 16
        self.sizes = [8, 12, 16]

        self.score = 0
        self.paused = False
        self.holds : dict[int,Figure] = {}
        self.held = False
        
        self.stun_cooldown = 0
        self.fall_timer = Timer(framerate=8)
        self.move_timer = Timer(framerate=13)
        self.rotate_timer = Timer(framerate=9)
        self.pause_timer = Timer(framerate=3)

        self.return_button = Button(pg.Rect(10,10,30,30),"X", lambda: self.ret_back(),"small",2)
        self.score_text = Text((500,110),f"Score: {self.score}")
        self.next_piece_text = Text((500,230),f"Next:")

        self.zone_start = (110,4*32)
        self.map = Map()
        self.next_figure = gen_figure(size_range=self.mode.gen_range)
        gen_figure(size_range=self.mode.gen_range).apply_to(self.map)

        self.backgrounds = {}
        self.empty_lines = {}
        for i in self.sizes: self.create_size(i)

        self.hold_grid = Grid(
            (100,100),
            (20,40),
            (500,500)
        )
    
    def init(self):
        sprites.empty()
        sprites.add(self.return_button)
        sprites.add(self.score_text)
        sprites.add(self.next_piece_text)
    
    def frame(self):
        self.check_size()
        keys = pg.key.get_pressed()
        if keys[pg.K_F1]:
            self.paused = not self.paused
            sleep(0.1)
        
        if self.paused: 
            pg.draw.rect(self.screen,col.bg,(0,0,self.screen.get_width(),self.screen.get_height()))
            return
        pg.draw.rect(
            self.screen,
            col.borders,
            (self.zone_start[0]-5,
             self.zone_start[1]-5,
             21*self.size + 10,
             42*self.size + 10),
            5)
        self.move()
        self.draw_holds()
        
        draw_on(self.screen, self.background, self.zone_start)
        draw_on(self.screen, self.next_figure.get_fig_preview(), (500,300))
        draw_on(self.screen, precompile_text(f"{self.next_figure.size()}", "small", col.borders), (500,415))
        pg.draw.rect(self.screen, col.borders, (495,295,110,110),5)

        fig = self.map.seek_figure()
        for f_tile in fig.figure:
            if f_tile[1] < 42: 
                draw_on(self.screen, f'tile_block{self.size}.jpg', 
                        self.convert(*f_tile), fig.color)
        
        if self.map.can_move():
            if self.fall_timer.tick(self.fps): self.map.move()
            self.stun_cooldown = 20
        elif self.stun_cooldown < 0:
            for f_tile in fig.figure:
                if f_tile[1] >= 42: continue
                for i in self.sizes: draw_on(self.backgrounds[i], f"tile_block{i}.jpg", (f_tile[0]*i, (41-f_tile[1])*i), fig.color)
            self.map.remove_figure_status()
            
            for i in fig.figure:
                if i[1] > 41: self.ret_back()
            self.apply_next_figure()
            self.contract_full_lines()

        self.stun_cooldown -= 1

    def draw_holds(self):
        for i,k in enumerate(self.holds.keys()):
            fig = self.holds[k]
            at = (self.hold_grid[i%2,i//2].left, self.hold_grid[i%2,i//2].top)

            draw_on(self.screen, fig.get_fig_preview(), at )
            pg.draw.rect(self.screen, col.borders, (at[0]-5, at[1]-5, 110, 110), 5)
            draw_on(self.screen, precompile_text(f"{fig.size()}", "small", col.borders), (at[0], at[1] + 110))

    def ret_back(self):
        self.mode.set_mode("menu")
        if self.mode.sandbox_entry == -1: return

        with open("./save/sandbox.txt", "r") as file:
            f_c = file.read().split("\n")
        
        entry = f_c[self.mode.sandbox_entry].split(",")
        entry[1] = str(self.score) if self.score > int(entry[1]) else entry[1]
        entry = ",".join(entry)
        f_c[self.mode.sandbox_entry] = entry
        f_c = "\n".join(f_c)

        with open("./save/sandbox.txt", "w") as file:
            file.write(f_c)

    def convert(self,x,y):
        return (x * self.size + self.zone_start[0], 
                self.zone_start[1] + self.size * (41 - y))

    def apply_next_figure(self):
        self.next_figure.apply_to(self.map)
        self.next_figure = gen_figure(size_range=self.mode.gen_range)
        self.score += 1
        self.score_text.ch_text(f"Score {self.score}")
        self.held = False
    
    def contract_full_lines(self):
        is_going = True
        while is_going:
            is_going = False
            for i in range(41):
                if has(self.map.get_line(i),None): continue
                self.score += 10
                self.score_text.ch_text(f"Score {self.score}")
                self.map.delete_line(i)
                is_going = True
                for J in self.sizes:
                    tmp = pg.Surface((21*J,(42-i)*J))
                    tmp.blit(self.backgrounds[J],(0,J))
                    tmp.blit(self.empty_lines[J],(0,0))
                    self.backgrounds[J].blit(tmp,(0,0))

    def hold(self):
        fig = self.map.seek_figure()
        size = len(fig.figure)
        for i in fig.figure:
            del self.map[i]
        
        if size in self.holds:
            self.holds[size].apply_pos((10,42))
            self.holds[size].apply_to(self.map)
        else:
            self.next_figure.apply_to(self.map)
            self.next_figure = gen_figure(size_range=self.mode.gen_range)
        
        self.holds[size] = fig
        self.held = True

    def move(self):
        keys = pg.key.get_pressed()
        can_do = self.move_timer.tick(self.fps)
        can_rot = self.rotate_timer.tick(self.fps)

        if keys[pg.K_RIGHT] and self.map.can_move(direction=(1,0)) and can_do:
            self.map.move(direction=(1,0))
            self.stun_cooldown += 1
        if keys[pg.K_LEFT] and self.map.can_move(direction=(-1,0)) and can_do:
            self.map.move(direction=(-1,0))
            self.stun_cooldown += 1
        if keys[pg.K_DOWN] and self.map.can_move() and can_do:
            self.map.move()
            self.stun_cooldown = 20
        if keys[pg.K_UP] and self.map.can_rotate() and can_rot:
            self.map.rotate()
            self.stun_cooldown += 1
        if keys[pg.K_SPACE] and self.map.can_move() and can_do:
            while self.map.can_move(): self.map.move()
            self.stun_cooldown = 20
        if keys[pg.K_v] and self.map.can_flip() and can_rot:
            self.map.flip()
            self.stun_cooldown += 1
        if keys[pg.K_c] and not self.held: self.hold()
