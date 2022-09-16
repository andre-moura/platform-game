from os import walk
import pygame 

def import_folder(path):
    surface_list = []
    for _,__, img_file in walk(path):
        for file in img_file:
            full_path = path + '/' + file
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    return surface_list