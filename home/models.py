from django.db import models


class NFT(models.Model):
    MUSIC_ART = 'msc'
    DIGITAL_ART = 'dig'
    BLOCKCHAIN = 'blc'
    VIRTUAL = 'vtr'

    CATEGORY_CHOICES = [
        (MUSIC_ART, 'Music Art'),
        (DIGITAL_ART, 'Digital Art'),
        (BLOCKCHAIN, 'Blockchain'),
        (VIRTUAL, 'Virtual'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=600)
    description = models.TextField()
    username = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    royalties = models.DecimalField(max_digits=5, decimal_places=2)
    file = models.FileField(upload_to='nft_files/')

    def __str__(self):
        return self.title
