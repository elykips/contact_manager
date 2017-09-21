class Marker:
	def __init_(self, color="Red"):
		self.color= color

class MarkerBox:
	def __init__(self, markers=[]):
		self.markers = markers

	def addMarker(self, marker):
		self.marker.add(marker)

	def removeMarker(self, color):
		if marker in self.color == color:
			markers.remove(marker)
			return marker
		return None

if __name__ == "__main__":
	mest_markers = MarkerBox()
	mest_markers.add_marker(Marker(color="blue"))
	mest_markers.add_marker(Marker(color="black"))
	mest_markers.add_marker(Marker(color="blue"))
	mest_markers.remove_marker(Marker(color="black"))

