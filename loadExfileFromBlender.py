import bpy
import os
 
filename = os.path.join("_PATH_", "/tmp/bpy_external.io")
exec(compile(open(filename).read(), filename, 'exec'))