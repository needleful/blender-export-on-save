
import bpy

# Blender Addon: Export on Save

bl_info = {
	"name": "Export on Save",
	"author": "needleful",
	"version": (1, 0, 0),
	"blender": (2, 93, 0),
	"category": "Import-Export", 
}

def export_path_callback(settings):
	print("Export on Save: Exported to " + settings["gltf_filepath"])
	bpy.context.scene["gltf_filepath"] = settings["gltf_filepath"]

glTF2_pre_export_callback = export_path_callback

class AutoExportPanel(bpy.types.Panel):
	bl_label = "Export on Save"
	bl_idname = "OBJECT_PT_ExportOnSave"
	bl_space_type = "PROPERTIES"
	bl_region_type = "WINDOW"
	bl_context = "scene"

	def draw(self, context):
		layout = self.layout
		op = layout.operator("export_scene.gltf", text="GLB Export")
		op.export_apply = True
		op.use_active_collection = True
		op.will_save_settings = True
		if "gltf_filepath" in bpy.context.scene:
			op.filepath = bpy.context.scene["gltf_filepath"]


def export_handler(scene):
	print("Saving...")
	if "gltf_filepath" in bpy.context.scene:
		print("Exporting GLB now..")
		# Hopefully these are automatic?
		bpy.ops.export_scene.gltf(filepath=bpy.context.scene["gltf_filepath"])
	else:
		print("Export on Save: No saved filepath. Can't export")

bpy.app.handlers.save_post.append(export_handler)

def register():
	bpy.utils.register_class(AutoExportPanel)
	print("Export on Save")

def unregister():
	bpy.utils.unregister_class(AutoExportPanel)
	print("Unregistered: Export on Save")

if __name__ == "__main__":
	register()