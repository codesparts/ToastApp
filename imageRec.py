from clarifai.rest import ClarifaiApp


class Image(object):
    def __init__(self, url):
        self.url = url

    def getIng(self):
        item = list()
        app = ClarifaiApp()
        model = app.models.get('food-items-v1.0')
        image = app.inputs.create_image_from_bytes(img_bytes=self.url)
        predicted = model.predict([image])
        items = predicted[u'outputs'][0][u'data'][u'concepts']
        for i in items:
            item.append(i['name'])
        return item

