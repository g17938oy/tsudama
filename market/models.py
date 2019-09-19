from django.db import models
#import文を足すことを忘れずに

class Book(models.Model):
    
    STATE_CHOICES = (
                     (1, 'とても良い'),
                     (2, '良い'),
                     (3, 'あまり良くない'),
                     (4, '良くない'),
                     )

    title = models.CharField(
                             verbose_name = '書籍名',
                             max_length = 200,
                             help_text = "本の奥付に書いてある書籍名を入力してください。",
                             )
    author = models.CharField(
                              verbose_name = '著者名',
                              max_length = 200,
                              help_text = "本の奥付に書いてある著者名を入力してください。",
                              blank = True,
                              null = True,
                              )
    publisher = models.CharField(
                                 verbose_name = '出版社',
                                 max_length = 200,
                                 help_text = "本の奥付に書いてある出版社を入力してください。",
                                 blank = True,
                                 null = True,
                                 )
    published_date = models.DateField(
                                      verbose_name = '出版日',
                                      help_text = "本の奥付に書いてある出版日を入力してください。",
                                      blank = True,
                                      null = True,
                                      )
    version = models.CharField(
                               verbose_name = '版数',
                               max_length = 200,
                               help_text = "本の奥付に書いてある版数を入力してください。",
                               blank = True,
                               null = True,
                               )
    isbn = models.BigIntegerField(
                                 verbose_name = 'ISBN',
                                 help_text = "本の奥付に書いてあるISBNを入力してください。ISBNとは13桁の97から始まるコードです。",
                                 blank = True,
                                 null = True,
                                 )
    text = models.TextField(
                            verbose_name = '宣伝文',
                            help_text = "宣伝文を入力してください。",
                            blank = True,
                            null = True,
                            )
    state = models.IntegerField(
                                verbose_name = '状態',
                                choices = STATE_CHOICES,
                                default = 1,
                                )
    price = models.IntegerField(
                                verbose_name = '価格',
                                default = 300,
                                )
    
    def __str__(self):
        return self.title
