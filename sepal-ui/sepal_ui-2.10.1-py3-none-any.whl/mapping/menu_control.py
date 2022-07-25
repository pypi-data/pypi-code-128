from ipyleaflet import WidgetControl

from sepal_ui import sepalwidgets as sw
from sepal_ui.mapping.map_btn import MapBtn


class MenuControl(WidgetControl):
    """
    Widget control displaying a btn on the map. When clicked the menu expand to show the content set by the user and all the others are closed.
    It's used to display interactive tiles directly in the map. If the card_content is a Tile it will be automatically nested.

    Args:
        icon_content (str): the icon content as specified in the sm.MapBtn object (i.e. a 3 letter name or an icon name)
        card_content (container): any container from sw. The sw.Tile is specifically design to fit in this component
        card_title (str, optional): the card title. THe tile title will override this parameter if existing
    """

    menu = None
    "sw.Menu: the menu displayed on the map as a widget"

    m = None
    "sm.SepalMap: the map used to display the control"

    def __init__(self, icon_content, card_content, card_title=None, m=None, **kwargs):

        # save the map in the members
        self.m = m

        # create a clickable btn
        btn = MapBtn(content=icon_content, v_on="menu.on")
        slot = {"name": "activator", "variable": "menu", "children": btn}

        # nest the content if it's a sw.Tile
        children = [card_content]
        if isinstance(card_content, sw.Tile):
            card_title = card_content.get_title()
            card_content.nest()
            card_content.class_list.replace("ma-5", "ma-0")
            card_content.children[0].class_list.replace("pa-5", "pa-2")
            card_content.children[0].raised = False
            card_content.children[0].elevation = 0

        # set up a title of needed
        if card_title is not None:
            card_title = sw.CardTitle(children=[card_title])
            children.insert(0, card_title)

        # set up the content style
        card = sw.Card(
            tile=True,
            style_="overflow: auto",
            children=children,
        )

        # assemble everything in a menu
        self.menu = sw.Menu(
            v_model=False,
            close_on_click=False,
            close_on_content_click=False,
            children=[card],
            v_slots=[slot],
            offset_x=True,
        )

        # by default MenuControls will be displayed in the bottomright corner
        kwargs["position"] = kwargs.pop("position", "bottomright")
        kwargs["widget"] = self.menu

        super().__init__(**kwargs)

        # place te menu according to the widget positioning
        self.update_position(None)
        self.set_size()

        # add some interaction
        self.observe(self.update_position, "position")
        self.menu.observe(self.close_others, "v_model")

    def update_position(self, change):
        """
        update the position of the menu if the position of the widget is dynamically changed
        """

        self.menu.top = "bottom" in self.position
        self.menu.bottom = "top" in self.position
        self.menu.left = "right" in self.position
        self.menu.right = "left" in self.position

        return

    def set_size(self, **kwargs):
        """
        Set the size of the card using all the sizing parameters from a v.Card

        Args:
          min_width(str, optional): a fully qualified css description of the wanted min_width. default to 400px.
          max_width(str, optional): a fully qualified css description of the wanted max_width. default to 400px.
          min_height(str, optional): a fully qualified css description of the wanted min_height. default to 40vh.
          max_height(str, optional): a fully qualified css description of the wanted max_height. default to 40vh.

        Return:
          self
        """

        card = self.menu.children[0]

        card.min_width = kwargs.pop("min_width", "400px")
        card.max_width = kwargs.pop("max_width", "400px")
        card.min_height = kwargs.pop("min_height", "40vh")
        card.max_height = kwargs.pop("max_height", "40vh")

        return self

    def close_others(self, change):
        """Close all the other menus associated to the map to avoid overlapping"""

        # don't do anything if no map was set to avoid deprecation
        # remove when jumping to sepal-ui 3.0
        if self.m is None:
            return

        # avoid infinite loop by exiting the method when it's closed
        if self.menu.v_model is True:

            [
                setattr(c.menu, "v_model", False)
                for c in self.m.controls
                if isinstance(c, MenuControl) and c != self
            ]

        return
