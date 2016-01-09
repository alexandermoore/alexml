from Constants import *

class Game:
    def __init__(self):
        self.player = Object()
        self.objects = [self.player]
        self.players = [self.player]
        self.movedirs = {"d": (0,1),
                         "u": (0,-1),
                         "l": (-1,0),
                         "r": (1,0)}


    def move_object(self, obj, direction):
        xmv, ymv = self.movedirs[direction]
        obj.move(xmv, ymv)
        self.keep_object_on_screen(obj)

    def keep_object_on_screen(self, obj):
        obj.limit_position(0, 0, screen_width, screen_height)

    def get_colliding_objects(self, obj):
        collidingobjs = []
        for otherobj in self.objects:
            if otherobj != obj:
                collision = obj.collision(otherobj)
                if collision:
                    collidingobjs.append(otherobj)
        return collidingobjs

    def get_nearby_objects(self, obj, radius, use_sqrt=False):
        nearby = []
        for otherobj in self.objects:
            dist = obj.distance(otherobj, use_sqrt)
            if dist <= radius:
                nearby.append((otherobj, dist))
        return [o[0] for o in sorted(nearby, key=lambda o: o[1])]


    def handle_actions(self):
        player_control()
        ai_control()

    def player_control(self, obj):
        pass

    def ai_control(self, obj):
        pass

    def handle_rewards(self):
        for player in Players:
            

    def draw_objects(self):
        pass



    def loop(self):
        self.handle_actions()
        self.handle_rewards()

