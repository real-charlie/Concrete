from dataclasses import dataclass


@dataclass
class Groups:
    src_group = None
    dest_group = None

    def set_source_group(self, group):
        self.src_group = group

    def set_destination_group(self, group):
        self.dest_group = group

    def get_src(self):
        return self.src_group

    def get_des(self):
        return self.dest_group


class Server:
    def __init__(self, server_id, groups):
        self.server_id = server_id
        self.groups = groups
