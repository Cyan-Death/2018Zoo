class.LocationNeighbors(models.Model):
    fromLocation = models.ForeignKey('Location' , on_delete=models.SET_NULL , null=True)
    direction = models.CharField(max_length=200)
    toLocation = models.ForeignKey('Location' , on_delete=models.SET_NULL , null=True , related_name='neighbors_of')

    def __str__(self):
        return str(self.fromLocation) + ': ' + str(self.direction) + 'to: ' + str(self.toLocation)