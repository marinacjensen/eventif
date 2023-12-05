from django.db import models



class Contact(models.Model):
    name = models.CharField('nome', max_length=200)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20, blank=True)
    message = models.TextField('mensagem')
    created_at = models.DateTimeField('enviada em', auto_now_add=True)
    reply = models.TextField('resposta')
    replied_at = models.DateTimeField('respondido em', auto_now_add=True)
    replied = models.BooleanField('respondido', default=False)
    

    class Meta:
        verbose_name_plural = "contatos"
        verbose_name = "contato"
        ordering = ['-created_at', 'replied']

    def __str__(self):
        return self.name
