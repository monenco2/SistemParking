from django.db import models

# Create your models here.here
class pagofinal(models.Model):
    card_number = models.TextField("card_number", blank=True)
    card_name = models.TextField("card_name", blank=True)
    expiry_date = models.TextField("expiry_date", blank=True)
    cvv = models.TextField("cvv", blank=True)
    debit_card_number = models.TextField("debit_card_number", blank=True)
    debit_card_name = models.TextField("debit_card_name", blank=True)
    debit_expiry_date = models.TextField("debit_expiry_date", blank=True)
    debit_cvv = models.TextField("debit_cvv", null=True)


    def __str__(self):
        return f'{self.card_name}'
