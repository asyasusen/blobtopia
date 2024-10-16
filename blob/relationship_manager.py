from blob.relationship_class import Relationship


class RelationshipManager:
    def __init__(self):
        self.relationships = {}

    def add_relationship(self, blob_feels, blob_towards, friendScore=0, loverScore=0):
        reln = Relationship(blob_feels, blob_towards, friendScore, loverScore)
        self.relationships[(blob_feels, blob_towards)] = reln

    def get_relationship(self, blob_feels, blob_towards):
        reln= self.relationships.get((blob_feels, blob_towards))
        if reln:
            return reln
        else:
            return None
