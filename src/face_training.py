class FaceModel:
    def fit(self, images, labels):
        pass

def train_face_model(dataset):
    model = FaceModel()
    model.fit(dataset.images, dataset.labels)
    return model
