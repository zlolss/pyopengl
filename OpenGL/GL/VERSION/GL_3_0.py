'''OpenGL extension VERSION.GL_3_0

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_3_0 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_3_0.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_3_0 import *
### END AUTOGENERATED SECTION
glget.addGLGetConstant( GL_NUM_EXTENSIONS, (1,))
from OpenGL.GL.ARB.vertex_array_object import *
from OpenGL.GL.ARB.texture_buffer_object import *
from OpenGL.GL.ARB.framebuffer_object import *
from OpenGL.GL.ARB.map_buffer_range import *
