from django.db import models
#import文を足すことを忘れずに

class Lesson(models.Model):

    UNDERGRADUATE_CHOICES = (
        (1, '共通科目'),
        (2, '外国語科目'),
        (3, '健康余暇科学科目'),
        (4, '英語英文学科'),
        (5, '国際関係学科'),
        (6, '数学科'),
        (7, '情報科学科'),
        )

    TERM_CHOICES =(
        (1,'1ターム'),
        (2,'２ターム'),
        (3,'３ターム'),
        (4,'４ターム'),
        )
    WEEK_CHOICES = (
        (1,'月曜'),
        (2,'火曜'),
        (3,'水曜'),
        (4,'木曜'),
        (5,'金曜'),
        
        )

    PERIOD_CHOICES= (
        (1,'1限'),
        (2,'2限'),
        (3,'3限'),
        (4,'4限'),
        (5,'5限'),
        (6,'6限'),
        
        )
    LEVEL_CHOICES= (
        (1,'1年'),
        (2,'2年'),
        (3,'3年'),
        (4,'4年'),
        )
    

    undergraduate = models.IntegerField(
                                verbose_name = '学部',
                                choices = UNDERGRADUATE_CHOICES,
                                default = 1,
                                )

    course = models.CharField(
                             verbose_name = '科目名',
                             max_length = 200,
                             help_text = "該当授業の科目名を入力してください。",
                             )

    instructor = models.CharField(
                              verbose_name = '担当教員名',
                              max_length = 200,
                              help_text = "該当授業の担当教員名を入力してください。",
                              blank = True,
                              null = True,
                              )

    term = models.IntegerField(
                                verbose_name = 'ターム',
                                choices = TERM_CHOICES,
                                default = 1,
                                )
    
    dayOfTheWeek = models.IntegerField(
                                verbose_name = '曜日',
                                choices = WEEK_CHOICES,
                                default = 1,
                                )

    period = models.IntegerField(
                                verbose_name = '時限',
                                choices = PERIOD_CHOICES,
                                default = 1,
                                )

    yearOfStudy = models.IntegerField(
                                verbose_name = '推奨レベル',
                                choices = LEVEL_CHOICES,
                                default = 1,
                                )
    
        

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

