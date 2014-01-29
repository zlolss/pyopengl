'''OpenGL extension I3D.digital_video_control

This module customises the behaviour of the 
OpenGL.raw.WGL.I3D.digital_video_control to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/I3D/digital_video_control.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.WGL import _types
from OpenGL.raw.WGL.I3D.digital_video_control import *

def glInitDigitalVideoControlI3D():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION