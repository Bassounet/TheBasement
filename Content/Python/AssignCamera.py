import unreal

def run():
    # 1. Recuperer le Sequencer actuel
    level_sequence_editor_subsystem = unreal.get_editor_subsystem(unreal.LevelSequenceEditorSubsystem)
    current_sequence = level_sequence_editor_subsystem.get_current_level_sequence()
    
    if not current_sequence:
        unreal.log_warning("ERREUR : Aucune sequence ouverte.")
        return

    # 2. Recuperer la section Camera Cut Selectione
    selected_sections = level_sequence_editor_subsystem.get_selected_sections()
    camera_cut_section = None
    
    for section in selected_sections:
        if isinstance(section, unreal.MovieSceneCameraCutSection):
            camera_cut_section = section
            break
            
    if not camera_cut_section:
        unreal.log_warning("ERREUR : Selectionnez le bloc 'Camera Cut' dans la timeline.")
        return

    # 3. Recuperer la camera selectione dans le niveau
    editor_actor_subsystem = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    selected_actors = editor_actor_subsystem.get_selected_level_actors()
    
    target_camera = None
    for actor in selected_actors:
        # On accepte CameraActor classique et CineCameraActor
        if isinstance(actor, unreal.CameraActor) or isinstance(actor, unreal.CineCameraActor):
            target_camera = actor
            break
            
    if not target_camera:
        unreal.log_warning("ERREUR : Selectionnez une camera dans l'Outliner (scene).")
        return

    # 4. Faire le Binding
    # On ajoute la camera au sequencer (si elle n'y est pas deja) pour avoir un ID
    binding_id = current_sequence.add_possessable(target_camera)
    
    # On cree l'ID de liaison pour le cut
    camera_binding_id = unreal.MovieSceneObjectBindingID()
    camera_binding_id.set_editor_property("guid", binding_id.get_id())
    
    # On applique
    camera_cut_section.set_camera_binding_id(camera_binding_id)
    
    # Petit message de confirmation en bas a droite
    unreal.log(f"SUCCESS : Camera '{target_camera.get_actor_label()}' assignee !")

# Cette ligne lance la fonction quand on appelle le script
if __name__ == "__main__":
    run()