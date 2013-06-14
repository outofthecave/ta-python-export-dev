#!/usr/bin/env python

# TODO how to find out this path automatically?
# path to the toplevel directory of the TA installation
TA_ROOT_PATH = "../turtleart"

# TODO remove unused imports and global variables
import pygtk
pygtk.require('2.0')
import gtk
import gobject
import pango
import pangocairo

from gettext import gettext as _

try:
    import gst
    _GST_AVAILABLE = True
except ImportError:
    # Turtle Art should not fail if gst is not available
    _GST_AVAILABLE = False

import os
import subprocess
import errno

from random import uniform
from math import atan2, pi
DEGTOR = 2 * pi / 360

import locale

from TurtleArt.taconstants import (HORIZONTAL_PALETTE, VERTICAL_PALETTE, BLOCK_SCALE,
                         MEDIA_SHAPES, STATUS_SHAPES, OVERLAY_SHAPES,
                         TOOLBAR_SHAPES, TAB_LAYER, RETURN, OVERLAY_LAYER,
                         CATEGORY_LAYER, BLOCKS_WITH_SKIN, ICON_SIZE,
                         PALETTE_SCALE, PALETTE_WIDTH, SKIN_PATHS, MACROS,
                         TOP_LAYER, BLOCK_LAYER, OLD_NAMES, DEFAULT_TURTLE,
                         TURTLE_LAYER, EXPANDABLE, NO_IMPORT, TEMPLATES,
                         PYTHON_SKIN, PALETTE_HEIGHT, STATUS_LAYER, OLD_DOCK,
                         EXPANDABLE_ARGS, XO1, XO15, XO175, XO30, XO4, TITLEXY,
                         CONTENT_ARGS, CONSTANTS, EXPAND_SKIN, PROTO_LAYER,
                         EXPANDABLE_FLOW, SUFFIX)
from TurtleArt.tapalette import (palette_names, palette_blocks, expandable_blocks,
                       block_names, content_blocks, default_values,
                       special_names, block_styles, help_strings,
                       hidden_proto_blocks, string_or_number_args,
                       make_palette, palette_name_to_index,
                       palette_init_on_start)
from TurtleArt.talogo import (LogoCode, primitive_dictionary, logoerror)
from TurtleArt.tacanvas import TurtleGraphics
from TurtleArt.tablock import (Blocks, Block)
from TurtleArt.taturtle import (Turtles, Turtle)
# from TurtleArt.tautils import (magnitude, get_load_name, get_save_name, data_from_file,
#                      data_to_file, round_int, get_id, get_pixbuf_from_journal,
#                      movie_media_type, audio_media_type, image_media_type,
#                      save_picture, calc_image_size, get_path, hide_button_hit,
#                      show_button_hit, chooser_dialog, arithmetic_check, xy,
#                      find_block_to_run, find_top_block, journal_check,
#                      find_group, find_blk_below, data_to_string,
#                      find_start_stack, get_hardware, debug_output,
#                      error_output, convert, find_hat, find_bot_block,
#                      restore_clamp, collapse_clamp, data_from_string,
#                      increment_name, get_screen_dpi)
from TurtleArt.tautils import (magnitude, get_load_name, get_save_name, data_from_file,
                     data_to_file, round_int, get_id, get_pixbuf_from_journal,
                     movie_media_type, audio_media_type, image_media_type,
                     save_picture, calc_image_size, get_path, hide_button_hit,
                     show_button_hit, arithmetic_check, xy,
                     find_block_to_run, find_top_block, journal_check,
                     find_group, find_blk_below, data_to_string,
                     find_start_stack, get_hardware, debug_output,
                     error_output, convert, find_bot_block,
                     restore_clamp, collapse_clamp, data_from_string,
                     increment_name, get_screen_dpi)
from TurtleArt.tasprite_factory import (SVG, svg_str_to_pixbuf, svg_from_file)
from TurtleArt.sprites import (Sprites, Sprite)

if _GST_AVAILABLE:
    from TurtleArt.tagplay import stop_media

_MOTION_THRESHOLD = 6
_SNAP_THRESHOLD = 200
_NO_DOCK = (100, 100)  # Blocks cannot be docked
_BUTTON_SIZE = 32
_MARGIN = 5
_UNFULLSCREEN_VISIBILITY_TIMEOUT = 2
_PLUGIN_SUBPATH = 'plugins'
_MACROS_SUBPATH = 'macros'


import cairo
#import gtk

# import the canvas implementation from TA
#from TurtleArt.tacanvas import TurtleGraphics
from TurtleArt.tawindow import TurtleArtWindow



class DummyTurtleMain(object):
    """Keep the main objects for running a dummy TA window in one place.
    (Try not to have to inherit from turtleblocks.TurtleMain.)
    """
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__dict__[k] = v
    
    def set_title(self, *args, **kwargs):
        # TODO don't just rely on the 'win' attribute to be present
        self.win.set_title(*args, **kwargs)



class DummyTAWindow(TurtleArtWindow):
    """TurtleArtWindow without menus or palettes. Supports only the 
    functionality that is essential for running the generated Python 
    code.
    """

    def __init__(self, canvas_window, path, parent=None,
                 mycolors=None, mynick=None, turtle_canvas=None,
                 running_sugar=True):
        self.parent = parent
        # TODO what is this?
        self.turtle_canvas = turtle_canvas
        self._loaded_project = ''
        self._sharing = False
        self._timeout_tag = [0]
        self.send_event = None  # method to send events over the network
        self.gst_available = _GST_AVAILABLE
        self.running_sugar = False
        self.nick = None
        self.window = canvas_window
        if isinstance(canvas_window, gtk.DrawingArea):
            self.interactive_mode = True
            #self.window = canvas_window
            self.window.set_flags(gtk.CAN_FOCUS)
            self.window.show_all()
            if running_sugar:
                self.parent.show_all()
                #self.running_sugar = True

                from sugar import profile

                self.nick = profile.get_nick_name()
                self.macros_path = os.path.join(
                    get_path(parent, 'data'), _MACROS_SUBPATH)
            else:
                # Make sure macros_path is somewhere writable
                self.macros_path = os.path.join(
                    os.path.expanduser('~'), 'Activities',
                    'TurtleArt.activity', _MACROS_SUBPATH)
            self._setup_events()
        else:
            self.interactive_mode = False
            #self.window = canvas_window
            self.running_sugar = False
        self.activity = parent

        self.path = path
        self.load_save_folder = os.path.join(path, 'samples')
        self.py_load_save_folder = os.path.join(path, 'pysamples')
        self._py_cache = {}
        # TODO needed?
        self.used_block_list = []  # Which blocks has the user used?
        self.save_folder = None
        self.save_file_name = None
        self.width = gtk.gdk.screen_width()
        self.height = gtk.gdk.screen_height()
        self.rect = gtk.gdk.Rectangle(0, 0, 0, 0)

        self.no_help = False
        self.last_label = None
        self._autohide_shape = True
        self.keypress = ''
        self.keyvalue = 0
        self._focus_out_id = None
        self._insert_text_id = None
        self._text_to_check = False
        self.mouse_flag = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.update_counter = 0
        self.running_blocks = False
        self.saving_blocks = False
        self.copying_blocks = False
        self.sharing_blocks = False
        self.deleting_blocks = False

        try:
            locale.setlocale(locale.LC_NUMERIC, '')
        except locale.Error:
            debug_output('unsupported locale', self.running_sugar)
        self.decimal_point = locale.localeconv()['decimal_point']
        if self.decimal_point == '' or self.decimal_point is None:
            self.decimal_point = '.'

        self.orientation = HORIZONTAL_PALETTE

        self.hw = get_hardware()
        self.lead = 1.0
        if self.hw in (XO1, XO15, XO175, XO4):
            self.scale = 1.0
            self.entry_scale = 0.67
            if self.hw == XO1:
                self.color_mode = '565'
            else:
                self.color_mode = '888'
            if self.running_sugar and not self.activity.has_toolbarbox:
                self.orientation = VERTICAL_PALETTE
        else:
            self.scale = 1.0
            self.entry_scale = 1.0
            self.color_mode = '888'  # TODO: Read visual mode from gtk image
        self._set_screen_dpi()

        self.block_scale = BLOCK_SCALE[3]
        self.trash_scale = 0.5
        self.myblock = {}
        self.python_code = None
        self.nop = 'nop'
        self.loaded = 0
        self.step_time = 0
        self.hide = True
        self.palette = False
        self.coord_scale = 1
        self.buddies = []
        self._saved_string = ''
        self._saved_action_name = ''
        self._saved_box_name = ''
        self.dx = 0
        self.dy = 0
        self.media_shapes = {}
        self.cartesian = False
        self.polar = False
        self.metric = False
        self.overlay_shapes = {}
        self.toolbar_shapes = {}
        self.toolbar_offset = 0
        self.status_spr = None
        self.status_shapes = {}
        self.toolbar_spr = None
        self.palette_sprs = []
        self.palettes = []
        self.palette_button = []
        self.trash_stack = []
        self.selected_palette = None
        self.previous_palette = None
        self.selectors = []
        self.selected_selector = None
        self.previous_selector = None
        self.selector_shapes = []
        self.selected_blk = None
        self.selected_spr = None
        self.selected_turtle = None
        self.drag_group = None
        self.drag_turtle = 'move', 0, 0
        self.drag_pos = 0, 0
        self.dragging_canvas = [False, 0, 0]
        self.turtle_movement_to_share = None
        self.paste_offset = 20  # Don't paste on top of where you copied.

        self.block_list = Blocks(font_scale_factor=self.scale,
                                 decimal_point=self.decimal_point)
        if self.interactive_mode:
            self.sprite_list = Sprites(self.window)
        else:
            self.sprite_list = None

        self.canvas = TurtleGraphics(self, self.width, self.height)
        if self.hw == XO175 and self.canvas.width == 1024:
            self.hw = XO30
        if self.interactive_mode:
            self.sprite_list.set_cairo_context(self.canvas.canvas)

        self.turtles = Turtles(self.sprite_list)
        if self.nick is None:
            self.default_turtle_name = DEFAULT_TURTLE
        else:
            self.default_turtle_name = self.nick
        if mycolors is None:
            Turtle(self.turtles, self.default_turtle_name)
        else:
            Turtle(self.turtles, self.default_turtle_name, mycolors.split(','))
        self.active_turtle = self.turtles.get_turtle(self.default_turtle_name)
        self.active_turtle.show()

        self.canvas.clearscreen(False)

        self._configure_cb(None)

        self._icon_paths = [os.path.join(self.path, 'icons')]

        # TODO this isn't needed, right?
        self.lc = LogoCode(self)

        self.turtleart_plugins = []
        self.saved_pictures = []
        self.block_operation = ''

        #from tabasics import Palettes
        #self._basic_palettes = Palettes(self)

        if self.interactive_mode:
            gobject.idle_add(self._lazy_init)
        else:
            self._init_plugins()
            self._setup_plugins()
    
    # TODO refactor TAWindow to make these methods inheritable
    def _lazy_init(self):
        self._init_plugins()
        self._setup_plugins()
        self._setup_misc()
#         for name in palette_init_on_start:
#             debug_output('initing palette %s' % (name), self.running_sugar)
#             self.show_toolbar_palette(palette_names.index(name),
#                                       init_only=False, regenerate=True,
#                                       show=False)
# 
#         self._basic_palettes.make_trash_palette()
# 
#         self.show_toolbar_palette(0, init_only=False, regenerate=True,
#                                   show=True)

        if self.running_sugar:
            self.activity.check_buttons_for_fit()

    def _init_plugins(self):
        ''' Try importing plugin files from the plugin dir. '''
        plist = self._get_plugins_from_plugins_dir(self._get_plugin_home())
        for plugin_dir in plist:
            self.init_plugin(plugin_dir)

    def _get_plugin_home(self):
        ''' Look in the execution directory '''
        path = os.path.join(self.path, _PLUGIN_SUBPATH)
        if os.path.exists(path):
            return path
        else:
            return None

    def _setup_plugins(self):
        ''' Initial setup -- called just once. '''
        for plugin in self.turtleart_plugins:
            plugin.setup()

    def _setup_misc(self):
        ''' Misc. sprites for status, overlays, etc. '''
        self.load_media_shapes()
        for i, name in enumerate(STATUS_SHAPES):
            # Temporary hack to use wider shapes
            if name in ['print', 'help', 'status'] and self.width > 1024:
                self.status_shapes[name] = svg_str_to_pixbuf(
                    svg_from_file(
                        os.path.join(self.path, 'images', name + '1200.svg')))
            else:
                self.status_shapes[name] = svg_str_to_pixbuf(
                    svg_from_file(
                        os.path.join(self.path, 'images', name + '.svg')))
        self.status_spr = Sprite(self.sprite_list, 0, self.height - 200,
                                 self.status_shapes['status'])
        self.status_spr.hide()
        self.status_spr.type = 'status'
        self._autohide_shape = True

        for name in OVERLAY_SHAPES:
            self.overlay_shapes[name] = Sprite(
                self.sprite_list,
                int(self.width / 2 - 600),
                int(self.height / 2 - 450),
                svg_str_to_pixbuf(
                    svg_from_file("%s/images/%s.svg" % (self.path, name))))
            self.overlay_shapes[name].hide()
            self.overlay_shapes[name].type = 'overlay'

        if not self.running_sugar:
            # offset = 2 * self.width - 55 * len(TOOLBAR_SHAPES)
            offset = 55 * (1 + len(palette_blocks))
            for i, name in enumerate(TOOLBAR_SHAPES):
                self.toolbar_shapes[name] = Sprite(
                    self.sprite_list, i * 55 + offset, 0,
                    svg_str_to_pixbuf(
                        svg_from_file(
                            os.path.join(
                                self.path, 'icons', '%s.svg' % (name)))))
                self.toolbar_shapes[name].set_layer(TAB_LAYER)
                self.toolbar_shapes[name].name = name
                self.toolbar_shapes[name].type = 'toolbar'
            self.toolbar_shapes['stopiton'].hide()



# copied from turtleblocks.TurtleMain._setup_gtk()

win = gtk.Window(gtk.WINDOW_TOPLEVEL)
# win.set_default_size(gui.width, gui.height)
# win.move(gui.x, gui.y)
win.maximize()
# win.set_title('%s %s' % (gui.name, str(gui.version)))
# if os.path.exists(os.path.join(gui._execdirname, gui._ICON_SUBPATH)):
#     win.set_icon_from_file(os.path.join(gui._execdirname,
#                                         gui._ICON_SUBPATH))
win.show()
# win.connect('delete_event', gui._quit_ta)

''' Create a scrolled window to contain the turtle canvas. We
add a Fixed container in order to position text Entry widgets
on top of string and number blocks.'''
# TODO get rid of fixed container

gui = DummyTurtleMain()
gui.fixed = gtk.Fixed()
gui.fixed.connect('size-allocate', lambda widget, rect: gui.vbox.set_size_request(rect[2], rect[3]))
width = gtk.gdk.screen_width() - 80
height = gtk.gdk.screen_height() - 80
gui.fixed.set_size_request(width, height)

gui.vbox = gtk.VBox(False, 0)
gui.vbox.show()

gui.sw = gtk.ScrolledWindow()
gui.sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
gui.sw.show()
canvas_ = gtk.DrawingArea()
width = gtk.gdk.screen_width() * 2
height = gtk.gdk.screen_height() * 2
canvas_.set_size_request(width, height)
gui.sw.add_with_viewport(canvas_)
canvas_.show()
gui.vbox.pack_end(gui.sw, True, True)
gui.fixed.put(gui.vbox, 0, 0)
gui.fixed.show()

win.add(gui.fixed)
win.show_all()
gui.win = win
gui.canvas = canvas_


# TODO how to find out whether we're in interactive mode? are we always in interactive mode?
interactive = True

# copied from turtleblocks.TurtleMain._build_window()
if interactive:
    win = gui.canvas.get_window()
    cr = win.cairo_create()
    surface = cr.get_target()
else:
    img_surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                                     1024, 768)
    cr = cairo.Context(img_surface)
    surface = cr.get_target()
gui.turtle_canvas = surface.create_similar(
    cairo.CONTENT_COLOR, max(1024, gtk.gdk.screen_width() * 2),
    max(768, gtk.gdk.screen_height() * 2))



# instantiate either a real TurtleArtWindow instance 
# or an instance of a dummy sub-class that supports only the stuff 
# TurtleGraphics needs
window = DummyTAWindow(gui.canvas, TA_ROOT_PATH,
                                  turtle_canvas=gui.turtle_canvas,
                                  parent=gui, running_sugar=False)
canvas = window.canvas



# auto-converted block code (assuming it had a 'start' block at the top)
def start():
    # example: draw a square
    for i in range(4):
        canvas.forward(100)
        canvas.right(90)

    # The idea is to handle everything as it is handled when the block code is 
    # executed in TA. That is, translate all blocks to operations on the canvas 
    # or Python control structures (e.g., loops).



if __name__ == '__main__':
    gtk.main()
    start()


