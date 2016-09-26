from vispy import scene


canvas = scene.SceneCanvas(keys=None, size=(800, 600), show=True)
view = canvas.central_widget.add_view()
scene_transform = scene.STTransform()
view.camera = scene.cameras.TurntableCamera(parent=view.scene,
                                            fov=0., distance=4.0)

ax = scene.visuals.Axis(pos=[[-1.0, 0], [1.0, 0]],
                        tick_direction=(0, -1),
                        parent=view.scene, axis_label='X',
                        anchors=['center', 'middle'])

canvas.render()
