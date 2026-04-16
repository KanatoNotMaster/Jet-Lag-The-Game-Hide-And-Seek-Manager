import pygame
import math

# --- COORDINATE SETTINGS ---
IMG_PATH = "Greenfield Map.png"
RED_OVERLAY = (255, 0, 0, 127)
SIDEBAR_WIDTH = 250

# --- CROP SETTINGS ---
CROP_LEFT = 1088
CROP_TOP = 2032
CROP_RIGHT_MARGIN = 60
CROP_BOTTOM_MARGIN = 1375

# Original Map Constants (Before Crop)
ORIG_MC_TL_X, ORIG_MC_TL_Z = -4608, -6144 

# New Constants (Calculated after crop)
# Since we cut 1088 pixels from the left, the new "0,0" is 1088 blocks further East.
MC_TL_X = ORIG_MC_TL_X + CROP_LEFT
MC_TL_Z = ORIG_MC_TL_Z + CROP_TOP

# --- STATION DATA ---
STATIONS = [
    {"name": "Shing Mun River", "mc_x": 12534, "mc_z": -1797},
    {"name": "Eastern Industrial District", "mc_x": 12194, "mc_z": -1797},
    {"name": "Factory Street", "mc_x": 11892, "mc_z": -1827},
    {"name": "Northern Industrial District", "mc_x": 11586, "mc_z": -2082},
    {"name": "Green Island", "mc_x": 11887, "mc_z": -1387},
    {"name": "Airport", "mc_x": 12095, "mc_z": -633},
    {"name": "Tin Wah", "mc_x": 10877, "mc_z": -1492},
    {"name": "Lingping", "mc_x": 10719, "mc_z": -1811},
    {"name": "IKEA", "mc_x": 10601, "mc_z": -1327},
    {"name": "Tsun Yip Mall", "mc_x": 10641, "mc_z": -916},
    {"name": "Second Street Park", "mc_x": 10778, "mc_z": -825},
    {"name": "Third Street", "mc_x": 10778, "mc_z": -825},
    {"name": "SKH Lee Wing Him College", "mc_x": 10833, "mc_z": -438},
    {"name": "Tsun Yip Railway", "mc_x": 10595, "mc_z": -737},
    {"name": "Tsun Yip", "mc_x": 10434, "mc_z": -790},
    {"name": "Green Hill", "mc_x": 10203, "mc_z": -623},
    {"name": "Southern Hotel", "mc_x": 10067, "mc_z": -1083},
    {"name": "Southling Stadium", "mc_x": 10202, "mc_z": -1452},
    {"name": "Sai Sha Hospital", "mc_x": 9964, "mc_z": -1495},
    {"name": "Sai Sha", "mc_x": 9789, "mc_z": -1721},
    {"name": "Central Park", "mc_x": 10323, "mc_z": -1930},
    {"name": "Pak Sha", "mc_x": 9873, "mc_z": -2218},
    {"name": "Kamlong Bay", "mc_x": 10340, "mc_z": -2223},
    {"name": "Ting Kau", "mc_x": 10288, "mc_z": -2610},
    {"name": "Sham Tseng", "mc_x": 9875, "mc_z": -2656},
    {"name": "Kwai Chung", "mc_x": 10288, "mc_z": -3119},
    {"name": "Kwai Shing", "mc_x": 9863, "mc_z": -3129},
    {"name": "Man Kam To", "mc_x": 10103, "mc_z": -3332},
    {"name": "Nagashima Resort", "mc_x": 9243, "mc_z": -3165},
    {"name": "Greenfield", "mc_x": 5379, "mc_z": -2033},
    {"name": "Lannex", "mc_x": 4998, "mc_z": -1969},
    {"name": "Thorne", "mc_x": 5023, "mc_z": -3168},
    {"name": "Airport Cargo Centre", "mc_x": 4695, "mc_z": -2237},
    {"name": "LOHAS Town", "mc_x": 4996, "mc_z": -772},
    {"name": "Palma", "mc_x": 4913, "mc_z": 715},
    {"name": "South Palma", "mc_x": 5083, "mc_z": 1058},
    {"name": "Airport Garage", "mc_x": 4102, "mc_z": -1841},
    {"name": "Rio Pueblo", "mc_x": 4253, "mc_z": -1336},
    {"name": "Sumida River", "mc_x": 4213, "mc_z": -792},
    {"name": "Rio Pueblo-Downtown Highway", "mc_x": 4150, "mc_z": -488},
    {"name": "Los Llanos", "mc_x": 4150, "mc_z": -73},
    {"name": "Sonora River", "mc_x": 4165, "mc_z": 565},
    {"name": "Sonora", "mc_x": 4088, "mc_z": 525},
    {"name": "Rockwell Light Rail", "mc_x": 4042, "mc_z": 1453},
    {"name": "Rockwell", "mc_x": 4079, "mc_z": 1575},
    {"name": "Terminal 1", "mc_x": 3682, "mc_z": -1936},
    {"name": "Airport", "mc_x": 3529, "mc_z": -2000},
    {"name": "South Los Llanos", "mc_x": 3544, "mc_z": 525},
    {"name": "Nihonmachi", "mc_x": 3088, "mc_z": -801},
    {"name": "Lennox", "mc_x": 2899, "mc_z": 367},
    {"name": "Longport", "mc_x": 2647, "mc_z": 1345},
    {"name": "Longport Light Rail", "mc_x": 3069, "mc_z": 1288},
    {"name": "Whitestone East", "mc_x": 2413, "mc_z": -792},
    {"name": "Dawson Rail", "mc_x": 1743, "mc_z": 97},
    {"name": "Dawson", "mc_x": 1873, "mc_z": 226},
    {"name": "South Dawson", "mc_x": 1992, "mc_z": 590},
    {"name": "Longport Keys East", "mc_x": 1718, "mc_z": 1357},
    {"name": "Ngong Ping", "mc_x": 1566, "mc_z": -792},
    {"name": "Riverwood", "mc_x": 1288, "mc_z": 226},
    {"name": "Kennedy", "mc_x": 1205, "mc_z": 838},
    {"name": "Eagle-Point", "mc_x": 819, "mc_z": -476},
    {"name": "Georgetown", "mc_x": 886, "mc_z": 226},
    {"name": "Old Georgetown", "mc_x": 600, "mc_z": 229},
    {"name": "Sunnyside", "mc_x": 558, "mc_z": -2061},
    {"name": "Ashfield East Park", "mc_x": 544, "mc_z": -1736},
    {"name": "Ashfield East", "mc_x": 502, "mc_z": -1432},
    {"name": "Ashfield South", "mc_x": 544, "mc_z": -1255},
    {"name": "Downtown", "mc_x": 234, "mc_z": -586},
    {"name": "Southern Park", "mc_x": 275, "mc_z": -457},
    {"name": "Union", "mc_x": 342, "mc_z": -265},
    {"name": "Market Street", "mc_x": 345, "mc_z": -7},
    {"name": "Hunter’s point", "mc_x": 268, "mc_z": -17},
    {"name": "Retail Park", "mc_x": 262, "mc_z": 375},
    {"name": "Longport Keys West", "mc_x": 233, "mc_z": 1120},
    {"name": "Glewview", "mc_x": 58, "mc_z": -1841},
    {"name": "Ashfield Central", "mc_x": 79, "mc_z": -1200},
    {"name": "Ashfield Park", "mc_x": 104, "mc_z": -1034},
    {"name": "Bridge Street", "mc_x": -31, "mc_z": -224},
    {"name": "Hall Street", "mc_x": 53, "mc_z": 63},
    {"name": "Montaro Mall", "mc_x": 53, "mc_z": 365},
    {"name": "Genmar Stadium", "mc_x": -352, "mc_z": -1036},
    {"name": "Fort Franklin", "mc_x": -465, "mc_z": -196},
    {"name": "Wanking", "mc_x": -371, "mc_z": 224},
    {"name": "Olympia", "mc_x": -352, "mc_z": 454},
    {"name": "Clinton Light Rail", "mc_x": -646, "mc_z": -1199},
    {"name": "Clinton", "mc_x": -648, "mc_z": -902},
    {"name": "Franklin", "mc_x": -648, "mc_z": -443},
    {"name": "Deltapier", "mc_x": -839, "mc_z": 505},
    {"name": "Melrose", "mc_x": -1011, "mc_z": -2275},
    {"name": "Northpark", "mc_x": -1121, "mc_z": -1394},
    {"name": "Southpark", "mc_x": -1101, "mc_z": -1087},
    {"name": "Baron’s Bar", "mc_x": -1110, "mc_z": -94},
    {"name": "Melrose West", "mc_x": -1483, "mc_z": -1744},
    {"name": "Zetapier", "mc_x": -1641, "mc_z": 456},
    {"name": "Springfield", "mc_x": -2152, "mc_z": -1934},
    {"name": "Springfield Coliseum", "mc_x": -2488, "mc_z": -1951},
    {"name": "Ashfield West", "mc_x": -2774, "mc_z": -959},
    {"name": "Ashifield Industrial District", "mc_x": -1973, "mc_z": -959},
    {"name": "Westwood", "mc_x": -2181, "mc_z": -102},
    {"name": "Gammapier", "mc_x": -2240, "mc_z": 555},
    {"name": "Eagle Island", "mc_x": 477, "mc_z": -674},
    {"name": "Ralsewell", "mc_x": 714, "mc_z": -674},
    {"name": "Veteran Boulevard", "mc_x": 906, "mc_z": -236}
]

pygame.init()
screen = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("MTR Greenfield Map Helper")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Segoe UI", 14)
bold_font = pygame.font.SysFont("Segoe UI", 16, bold=True)

# --- LOAD AND CROP ---
try:
    full_img = pygame.image.load(IMG_PATH).convert()
    orig_w, orig_h = full_img.get_size()
    
    # Define crop area: x, y, width, height
    crop_w = orig_w - CROP_LEFT - CROP_RIGHT_MARGIN
    crop_h = orig_h - CROP_TOP - CROP_BOTTOM_MARGIN
    
    # Perform the crop to free up RAM
    map_img = full_img.subsurface((CROP_LEFT, CROP_TOP, crop_w, crop_h)).copy()
    del full_img # Remove original large image from memory
    
    IMG_W, IMG_H = map_img.get_size()
except Exception as e:
    print(f"Error loading image: {e}")
    exit()

class StationIcon:
    def __init__(self, name, mc_x, mc_z):
        self.name = name
        self.mc_pos = pygame.Vector2(mc_x, mc_z)
        # Position relative to new cropped Top-Left
        self.img_pos = pygame.Vector2(mc_x - MC_TL_X, mc_z - MC_TL_Z)
        self.hitbox = pygame.Rect(0, 0, 0, 0)

station_icons = [StationIcon(s["name"], s["mc_x"], s["mc_z"]) for s in STATIONS]

# --- STATE ---
zoom = 0.1
offset = pygame.Vector2(0, 0)
shapes_list = [] 
active_box = None
inputs = {"Ax": "", "Ay": "", "Bx": "", "By": "", "Radius": ""}
input_rects = {}
mode = "circle" 
circle_mode = "radius" 
shade_side = "inside" 

def add_shape_to_list():
    try:
        ax = int(inputs["Ax"] or 0) - MC_TL_X
        ay = int(inputs["Ay"] or 0) - MC_TL_Z
        bx = int(inputs["Bx"] or 0) - MC_TL_X
        by = int(inputs["By"] or 0) - MC_TL_Z
        
        if mode == "circle":
            if circle_mode == "2coors":
                rad = int(math.sqrt((bx - ax)**2 + (by - ay)**2))
            else:
                rad = int(inputs["Radius"] or 0)
            shapes_list.append({"type": "circle", "center": (ax, ay), "radius": rad, "side": shade_side})
        else:
            shapes_list.append({"type": "line", "pts": (ax, ay, bx, by), "side": shade_side})
    except ValueError:
        pass


def get_distance_text():
    try:
        ax = int(inputs["Ax"])
        ay = int(inputs["Ay"])
        bx = int(inputs["Bx"])
        by = int(inputs["By"])
    except ValueError:
        return ""
    dist = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
    return f"Distance: {dist:.1f} blocks"

running = True
while running:
    mx, my = pygame.mouse.get_pos()
    map_area = pygame.Rect(SIDEBAR_WIDTH, 0, 1280 - SIDEBAR_WIDTH, 800)
    
    world_x = int(((offset.x + (mx - SIDEBAR_WIDTH)) / zoom) + MC_TL_X)
    world_z = int(((offset.y + my) / zoom) + MC_TL_Z)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            station_found = None
            for icon in station_icons:
                if icon.hitbox.collidepoint(mx, my):
                    station_found = icon
                    break
            
            if station_found:
                if event.button == 1: 
                    inputs["Ax"], inputs["Ay"] = str(int(station_found.mc_pos.x)), str(int(station_found.mc_pos.y))
                elif event.button == 3: 
                    inputs["Bx"], inputs["By"] = str(int(station_found.mc_pos.x)), str(int(station_found.mc_pos.y))
            
            elif event.button == 1:
                active_box = None
                for key, rect in input_rects.items():
                    if rect.collidepoint(mx, my): active_box = key
                
                if pygame.Rect(10, 50, 110, 30).collidepoint(mx, my): mode = "circle"
                if pygame.Rect(130, 50, 110, 30).collidepoint(mx, my): mode = "line"
                if mode == "circle" and pygame.Rect(10, 90, 230, 25).collidepoint(mx, my):
                    circle_mode = "2coors" if circle_mode == "radius" else "radius"

                lbl1, lbl2 = ("inside", "outside") if mode == "circle" else ("hotter", "colder")
                if pygame.Rect(10, 310, 110, 30).collidepoint(mx, my): shade_side = lbl1
                if pygame.Rect(130, 310, 110, 30).collidepoint(mx, my): shade_side = lbl2
                
                if pygame.Rect(10, 360, 230, 40).collidepoint(mx, my): add_shape_to_list()
                if pygame.Rect(10, 410, 110, 30).collidepoint(mx, my): 
                    if shapes_list: shapes_list.pop()
                if pygame.Rect(130, 410, 110, 30).collidepoint(mx, my): shapes_list = []

        if event.type == pygame.KEYDOWN and active_box:
            if event.key == pygame.K_BACKSPACE: inputs[active_box] = inputs[active_box][:-1]
            elif event.unicode.isdigit() or (event.unicode == '-' and len(inputs[active_box]) == 0):
                inputs[active_box] += event.unicode

        if event.type == pygame.MOUSEWHEEL and map_area.collidepoint(mx, my):
            old_zoom = zoom
            zoom = max(0.005, min(2.0, zoom + event.y * 0.1 * zoom))
            rel_m = pygame.Vector2(mx - SIDEBAR_WIDTH, my)
            offset = ((rel_m + offset) / old_zoom) * zoom - rel_m

    if (pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[1]) and map_area.collidepoint(mx, my):
        is_on_station = any(icon.hitbox.collidepoint(mx, my) for icon in station_icons)
        if not is_on_station:
            offset -= pygame.Vector2(pygame.mouse.get_rel())
        else: pygame.mouse.get_rel()
    else: pygame.mouse.get_rel()

    # --- RENDERING ---
    screen.fill((25, 25, 25))
    view_rect = pygame.Rect(offset.x/zoom, offset.y/zoom, (1280-SIDEBAR_WIDTH)/zoom, 800/zoom)
    clip_rect = view_rect.clip(pygame.Rect(0, 0, IMG_W, IMG_H))
    
    if clip_rect.width > 1 and clip_rect.height > 1:
        sub_map = map_img.subsurface(clip_rect)
        sc_size = (int(clip_rect.width * zoom), int(clip_rect.height * zoom))
        map_final = pygame.transform.scale(sub_map, sc_size)
        pos = (max(SIDEBAR_WIDTH, SIDEBAR_WIDTH - offset.x), max(0, -offset.y))
        screen.blit(map_final, pos)

        overlay_sc = pygame.Surface(sc_size, pygame.SRCALPHA)
        for s in shapes_list:
            if s["type"] == "circle":
                cx, cy = (s["center"][0] - clip_rect.x) * zoom, (s["center"][1] - clip_rect.y) * zoom
                r = s["radius"] * zoom
                if s["side"] == "inside":
                    temp = pygame.Surface(sc_size, pygame.SRCALPHA)
                    temp.fill(RED_OVERLAY)
                    pygame.draw.circle(temp, (0,0,0,0), (int(cx), int(cy)), int(r))
                    overlay_sc.blit(temp, (0,0))
                else:
                    pygame.draw.circle(overlay_sc, RED_OVERLAY, (int(cx), int(cy)), int(r))
            
            elif s["type"] == "line":
                ax, ay, bx, by = s["pts"]
                m_x, m_y = ((ax+bx)/2 - clip_rect.x) * zoom, ((ay+by)/2 - clip_rect.y) * zoom
                diff = pygame.Vector2(bx-ax, by-ay)
                if diff.length() == 0: continue
                perp = pygame.Vector2(-diff.y, diff.x).normalize() * IMG_W * zoom
                shade_dir = diff.normalize() * IMG_W * zoom
                if s["side"] == "hotter": shade_dir *= -1
                p1, p2 = (m_x+perp.x, m_y+perp.y), (m_x-perp.x, m_y-perp.y)
                pygame.draw.polygon(overlay_sc, RED_OVERLAY, [p1, p2, (p2[0]+shade_dir.x, p2[1]+shade_dir.y), (p1[0]+shade_dir.x, p1[1]+shade_dir.y)])

        screen.blit(overlay_sc, pos)

        for icon in station_icons:
            sx = (icon.img_pos.x * zoom) - offset.x + SIDEBAR_WIDTH
            sy = (icon.img_pos.y * zoom) - offset.y
            if map_area.collidepoint(sx, sy):
                icon.hitbox = pygame.Rect(sx - 8, sy - 8, 16, 16)
                pygame.draw.rect(screen, (255, 255, 255), icon.hitbox)
                pygame.draw.rect(screen, (0, 0, 0), icon.hitbox, 2)
                
                txt_surf = font.render(icon.name, True, (0, 0, 0))
                txt_rect = txt_surf.get_rect(topleft=(sx + 12, sy - 8))
                
                bg_rect = txt_rect.inflate(6, 4)
                bg_surface = pygame.Surface(bg_rect.size, pygame.SRCALPHA)
                bg_surface.fill((255, 255, 255, 180)) 
                
                screen.blit(bg_surface, bg_rect.topleft)
                screen.blit(txt_surf, txt_rect.topleft)
            else:
                icon.hitbox = pygame.Rect(0,0,0,0)

    # --- UI ---
    pygame.draw.rect(screen, (40, 40, 45), (0, 0, SIDEBAR_WIDTH, 800))
    screen.blit(bold_font.render(f"X: {world_x}  Z: {world_z}", True, (150, 255, 150)), (10, 15))

    distance_text = get_distance_text()
    if distance_text:
        screen.blit(font.render(distance_text, True, (255, 255, 255)), (10, 35))
    
    if mode == "circle":
        pygame.draw.rect(screen, (100, 60, 60), (10, 90, 230, 25))
        txt = f"MODE: {'2-COORDS' if circle_mode == '2coors' else 'RADIUS'}"
        screen.blit(font.render(txt, True, (255,255,255)), (25, 93))

    y_off = 130
    if mode == "circle":
        labels = [("Centre X", "Ax"), ("Centre Y", "Ay"), ("Point X", "Bx"), ("Point Y", "By"), ("Radius", "Radius")]
    else:
        labels = [("Start X", "Ax"), ("Start Y", "Ay"), ("End X", "Bx"), ("End Y", "By"), ("Radius", "Radius")]

    for label_text, key in labels:
        screen.blit(font.render(label_text, True, (200, 200, 200)), (10, y_off))
        rect = pygame.Rect(100, y_off, 140, 22)
        input_rects[key] = rect
        pygame.draw.rect(screen, (100, 100, 150) if active_box == key else (60, 60, 60), rect)
        screen.blit(font.render(inputs[key], True, (255, 255, 255)), (105, y_off + 2))
        y_off += 30

    pygame.draw.rect(screen, (80, 80, 100) if mode == "circle" else (50, 50, 50), (10, 50, 110, 30))
    pygame.draw.rect(screen, (80, 80, 100) if mode == "line" else (50, 50, 50), (130, 50, 110, 30))
    screen.blit(font.render("CIRCLE", True, (255,255,255)), (40, 55))
    screen.blit(font.render("LINE", True, (255,255,255)), (170, 55))
    
    lbl1, lbl2 = ("INSIDE", "OUTSIDE") if mode == "circle" else ("HOTTER", "COLDER")
    pygame.draw.rect(screen, (70, 70, 70) if shade_side == lbl1.lower() else (40, 40, 40), (10, 310, 110, 30))
    pygame.draw.rect(screen, (70, 70, 70) if shade_side == lbl2.lower() else (40, 40, 40), (130, 310, 110, 30))
    screen.blit(font.render(lbl1, True, (255,255,255)), (40, 315))
    screen.blit(font.render(lbl2, True, (255,255,255)), (160, 315))

    pygame.draw.rect(screen, (0, 120, 215), (10, 360, 230, 40))
    screen.blit(bold_font.render("EXECUTE DRAWING", True, (255,255,255)), (55, 370))
    pygame.draw.rect(screen, (100, 100, 50), (10, 410, 110, 30))
    screen.blit(font.render("UNDO", True, (255,255,255)), (45, 415))
    pygame.draw.rect(screen, (150, 50, 50), (130, 410, 110, 30))
    screen.blit(font.render("CLEAR", True, (255,255,255)), (165, 415))

    inst1 = "LMB:"
    inst2 = "Circle: the centre"
    inst3 = "Line: starting point"
    inst4 = "RMB:"
    inst5 = "Circle: a point on the circumference"
    inst6 = "Line: ending point"

    screen.blit(font.render(inst1, True, (180, 180, 180)), (10, 460))
    screen.blit(font.render(inst2, True, (180, 180, 180)), (10, 480))
    screen.blit(font.render(inst3, True, (180, 180, 180)), (10, 500))
    screen.blit(font.render(inst4, True, (180, 180, 180)), (10, 540))
    screen.blit(font.render(inst5, True, (180, 180, 180)), (10, 560))
    screen.blit(font.render(inst6, True, (180, 180, 180)), (10, 580))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()