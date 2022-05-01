"""
Created By Jivansh Sharma 
April 2022
@parzuko
"""

from get_token import token as TOKEN
from models import MetroGraph
import discord


kamui = discord.Bot()
kamui_url = "https://github.com/parzuko/kamui/blob/main/assets/kamui.jpeg?raw=true"
kamui_graph = MetroGraph()
kamui_graph.populate_graph()

def style_shortest_path(shortest_path):
    styled_shortest_path = []
    for station in shortest_path:
        pretty_station = f"{station.capitalize()} {kamui_graph.get_station_line(station)}"
        styled_shortest_path.append(pretty_station)
    
    return styled_shortest_path

class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Start Point"))
        self.add_item(discord.ui.InputText(label="Destination"))

    async def callback(self, interaction: discord.Interaction):
        source = self.children[0].value.lower()
        destination = self.children[1].value.lower()
        embed = discord.Embed(
            title="Kamui! We got the shortest path!",
            description=f"Shortest path from {source.capitalize()} to {destination.capitalize()}",
            color=discord.Colour.random(),
        )
        
        shortest_path, duration = kamui_graph.get_shortest_path(source, destination)
        styled_shortest_path = style_shortest_path(shortest_path)
        
        embed.set_author(name="Kamui", icon_url=kamui_url)
        embed.add_field(name="Shortest Path", value=(" → ").join(styled_shortest_path))
        embed.set_footer(text=f"This route will take{int(duration)} minutes!")

        await interaction.response.send_message(embeds=[embed])


@kamui.event
async def on_ready():
    print(f"{kamui.user} is ready and online!")


@kamui.slash_command(name="kamui", description="Find the shortest path between two metro stations!")
async def modal_slash(ctx: discord.ApplicationContext):
    """Shows an example of a modal dialog being invoked from a slash command."""
    modal = MyModal(title="Calculate Shortest Path!")
    await ctx.send_modal(modal)

kamui.run(TOKEN)