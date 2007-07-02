"""
$Id$
"""

from Products.CMFCore.utils import ToolInit, ContentInit
from Products.CMFCore.DirectoryView import registerDirectory

import RedirectionTool

redirection_tool_globals=globals()

# Make the skins available as DirectoryViews.
registerDirectory('skins', redirection_tool_globals)

def initialize( context ):
    
    ToolInit('Redirection Tool', 
            tools=(RedirectionTool.RedirectionTool, ), 
            icon='action_icon.gif'
            ).initialize(context)
