from YaasHelper import *

class ViewHelper (YaasHelper):
    __module__ = __name__
    __doc__ = "Control the view"
     
    def __init__(self, yaas):

        YaasHelper.__init__(self, yaas)
        self.log.debug("(ViewHelper) init")
        
    def move_scene_view(self, down):
        """
            Moves the current selected scene up or down
        """
                
        all_scenes = self.song().scenes #then get all of the scenes
        scene_index = list(all_scenes).index(self.song().view.selected_scene) #then identify where the selected scene sits in relation to the full list

        self.log.verbose("(ViewHelper) current scene index is " + str(scene_index + 1))
                
        if down:
            self.log.debug("(ViewHelper) scene view down")
            scene_index = scene_index + 1
            if scene_index < len(self.song().scenes):
                self.song().view.selected_scene = self.song().scenes[scene_index]

        else:
            if scene_index == 0:
                return
            self.log.debug("(ViewHelper) scene view up")
            scene_index = scene_index - 1
            self.song().view.selected_scene = self.song().scenes[scene_index]
    
    def focus_on_track(self, track):
        """
            Sets the view to the given track and shows the devices
        """
        self.song().view.selected_track = track
        self.application().view.focus_view("Detail") 
        self.application().view.focus_view("Detail/DeviceChain") 

    def focus_on_device(self, device):        
        """
            Sets the view to the given device
        """
        self.application().view.focus_view("Detail/DeviceChain")  
        self.song().view.select_device(device)      
        
    def move_track_view_vertical(self, down):
        session = self.yaas.get_session()
        if down:
            self.log.debug("track view down")
            scene_offset = session._scene_offset + 1
            session.set_offsets(session._track_offset, scene_offset) #(track_offset, scene_offset) Sets the initial offset of the "red box" from top left
            self.song().view.selected_scene = self.song().scenes[scene_offset]

        else:
            self.log.debug("track view up")
            scene_offset = session._scene_offset - 1
            if scene_offset < 0:
                scene_offset = 0
            session.set_offsets(session._track_offset, scene_offset) #(track_offset, scene_offset) Sets the initial offset of the "red box" from top left
            self.song().view.selected_scene = self.song().scenes[scene_offset]

    def move_track_view_horizontal(self, right):
        session = self.yaas.get_session()
        if right:
            self.log.debug("track view right")
            track_offset = session._track_offset + 1
            session.set_offsets(track_offset, session._scene_offset) #(track_offset, scene_offset) Sets the initial offset of the "red box" from top left
            self.song().view.selected_track = self.song().tracks[track_offset]

        else:
            self.log.debug("track view left")
            track_offset = session._track_offset - 1
            if track_offset < 0:
                track_offset = 0
            session.set_offsets(track_offset, session._scene_offset) #(track_offset, scene_offset) Sets the initial offset of the "red box" from top left
            self.song().view.selected_track = self.song().tracks[track_offset]            


        

