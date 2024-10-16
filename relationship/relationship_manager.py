from blob.relationship.relationship_class import Relationship
from blob.relationship.relationship_modifier_class import Relationship_Modifier


class Relationship_Manager:
    
    relationships = {}

    @classmethod
    def add_relationship(self, blob_feels, blob_towards):
        reln = Relationship(blob_feels, blob_towards)
        self.relationships[(blob_feels, blob_towards)] = reln
        return reln

    @classmethod
    def get_relationship(self, blob_feels, blob_towards):
        reln= self.relationships.get((blob_feels, blob_towards))
        if reln:
            return reln
        else:
            return None

    @classmethod
    def blobs_meet(self, blob1, blob2):
        reln1 = self.add_relationship(blob1, blob2)
        reln2 = self.add_relationship(blob2, blob1)
        modifier = Relationship_Modifier("Just met",time_limit= 20, friend_score_modifier=10)
        reln1.add_modifier(modifier)
        reln2.add_modifier(modifier)
