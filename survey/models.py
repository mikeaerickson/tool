from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Survey(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250)
    last_updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True, related_name='survey')
    def __str__(self):
        return self.name


class Profile(models.Model):
    name=models.CharField(max_length=30,unique=True)
    image=models.URLField(max_length=200, null=True)
    att1=models.DecimalField(max_digits=5, decimal_places=4)
    att2=models.DecimalField(max_digits=5, decimal_places=4)
    att3=models.DecimalField(max_digits=5, decimal_places=4)
    att4=models.DecimalField(max_digits=5, decimal_places=4)
    att5=models.DecimalField(max_digits=5, decimal_places=4)
    att6=models.DecimalField(max_digits=5, decimal_places=4)
    att7=models.DecimalField(max_digits=5, decimal_places=4)
    att8=models.DecimalField(max_digits=5, decimal_places=4)
    att9=models.DecimalField(max_digits=5, decimal_places=4)
    att10=models.DecimalField(max_digits=5, decimal_places=4)
    in_survey = models.ForeignKey(Survey, related_name='profile')

class Design(models.Model):
    name=models.CharField(max_length=30,unique=False)
    num_alts=models.IntegerField()
    num_qs=models.IntegerField()
    none_option=models.IntegerField()
    att1_name=models.CharField(max_length=30, blank=True, default='')
    att1_type=models.IntegerField(blank=True, default='-1')
    att1_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, blank=True,)
    att2_name=models.CharField(max_length=30, blank=True, default='')
    att2_type=models.IntegerField(blank=True, default='-1')
    att2_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att3_name=models.CharField(max_length=30, blank=True, default='')
    att3_type=models.IntegerField(blank=True, default='-1')
    att3_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att4_name=models.CharField(max_length=30, blank=True, default='')
    att4_type=models.IntegerField(blank=True, default='-1')
    att4_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att5_name=models.CharField(max_length=30, blank=True, default='')
    att5_type=models.IntegerField(blank=True, default='-1')
    att5_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att6_name=models.CharField(max_length=30, blank=True, default='')
    att6_type=models.IntegerField(blank=True, default='-1')
    att6_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att7_name=models.CharField(max_length=30, blank=True, default='')
    att7_type=models.IntegerField(blank=True, default='-1')
    att7_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att8_name=models.CharField(max_length=30, blank=True, default='')
    att8_type=models.IntegerField(blank=True, default='-1')
    att8_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att9_name=models.CharField(max_length=30, blank=True, default='')
    att9_type=models.IntegerField(blank=True, default='-1')
    att9_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    att10_name=models.CharField(max_length=30, blank=True, default='')
    att10_type=models.IntegerField(blank=True, default='-1')
    att10_values=ArrayField(models.DecimalField(max_digits=5,decimal_places=4, default='-1'), size=10, null=True)
    in_survey = models.ForeignKey(Survey, related_name='design',unique=True)

class Response(models.Model):
    models.CharField(max_length=30,unique=True)
    Q1=models.IntegerField()
    Q2=models.IntegerField()
    Q3=models.IntegerField()
    Q4=models.IntegerField()
    Q5=models.IntegerField()
    Q6=models.IntegerField()
    Q7=models.IntegerField()
    Q8=models.IntegerField()
    Q9=models.IntegerField()
    Q10=models.IntegerField()
    Q11=models.IntegerField()
    Q12=models.IntegerField()
    Q13=models.IntegerField()
    Q14=models.IntegerField()
    Q15=models.IntegerField()
    Q16=models.IntegerField()
    Q17=models.IntegerField()
    Q18=models.IntegerField()
    Q19=models.IntegerField()
    Q20=models.IntegerField()


class Questions(models.Model):
    name=models.CharField(max_length=30,unique=True)
    Q1A1=models.IntegerField()
    Q1A2=models.IntegerField()
    Q1A3=models.IntegerField()
    Q1A4=models.IntegerField()

    Q2A1=models.IntegerField()
    Q2A2=models.IntegerField()
    Q2A3=models.IntegerField()
    Q2A4=models.IntegerField()

    Q3A1=models.IntegerField()
    Q3A2=models.IntegerField()
    Q3A3=models.IntegerField()
    Q3A4=models.IntegerField()

    Q4A1=models.IntegerField()
    Q4A2=models.IntegerField()
    Q4A3=models.IntegerField()
    Q4A4=models.IntegerField()

    Q5A1=models.IntegerField()
    Q5A2=models.IntegerField()
    Q5A3=models.IntegerField()
    Q5A4=models.IntegerField()

    Q6A1=models.IntegerField()
    Q6A2=models.IntegerField()
    Q6A3=models.IntegerField()
    Q6A4=models.IntegerField()

    Q7A1=models.IntegerField()
    Q7A2=models.IntegerField()
    Q7A3=models.IntegerField()
    Q7A4=models.IntegerField()

    Q8A1=models.IntegerField()
    Q8A2=models.IntegerField()
    Q8A3=models.IntegerField()
    Q8A4=models.IntegerField()

    Q9A1=models.IntegerField()
    Q9A2=models.IntegerField()
    Q9A3=models.IntegerField()
    Q9A4=models.IntegerField()

    Q10A1=models.IntegerField()
    Q10A2=models.IntegerField()
    Q10A3=models.IntegerField()
    Q10A4=models.IntegerField()

    Q11A1=models.IntegerField()
    Q11A2=models.IntegerField()
    Q11A3=models.IntegerField()
    Q11A4=models.IntegerField()

    Q12A1=models.IntegerField()
    Q12A2=models.IntegerField()
    Q12A3=models.IntegerField()
    Q12A4=models.IntegerField()

    Q13A1=models.IntegerField()
    Q13A2=models.IntegerField()
    Q13A3=models.IntegerField()
    Q13A4=models.IntegerField()

    Q14A1=models.IntegerField()
    Q14A2=models.IntegerField()
    Q14A3=models.IntegerField()
    Q14A4=models.IntegerField()

    Q15A1=models.IntegerField()
    Q15A2=models.IntegerField()
    Q15A3=models.IntegerField()
    Q15A4=models.IntegerField()

    Q16A1=models.IntegerField()
    Q16A2=models.IntegerField()
    Q16A3=models.IntegerField()
    Q16A4=models.IntegerField()

    Q17A1=models.IntegerField()
    Q17A2=models.IntegerField()
    Q17A3=models.IntegerField()
    Q17A4=models.IntegerField()

    Q18A1=models.IntegerField()
    Q18A2=models.IntegerField()
    Q18A3=models.IntegerField()
    Q18A4=models.IntegerField()

    Q19A1=models.IntegerField()
    Q19A2=models.IntegerField()
    Q19A3=models.IntegerField()
    Q19A4=models.IntegerField()

    Q20A1=models.IntegerField()
    Q20A2=models.IntegerField()
    Q20A3=models.IntegerField()
    Q20A4=models.IntegerField()

    in_study = models.ForeignKey(Survey, related_name='questions')

'''class Study(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    #last_updated = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, related_name='study')
    def __str__(self):
        return self.name

class Survey(models.Model):
    name = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=250)
    #questions = models.CharField(max_length=250)  # ???()
    #profiles = models.CharField(max_length=250)  # ???()
    in_study = models.ForeignKey(Study, related_name='survey')
    def __str__(self):
        return self.name

class Response(models.Model):
    datefilled = models.DateTimeField(auto_now_add=True)
    responses = ArrayField(
        ArrayField(
            models.IntegerField(blank=True),
            ),
        size=8,
        )
    metaData1 = models.CharField(max_length=100)
    metaData2 = models.CharField(max_length=100)
    metaData3 = models.CharField(max_length=100)
    for_survey = models.ForeignKey(Survey, related_name='response')
    def __str__(self):
        return self.name

class Results(models.Model):
    parthworths = models.CharField(max_length=250)  # ???()
    tfmodel = models.CharField(max_length=250)  # ???()
    dategenerated=models.DateTimeField(auto_now_add=True)
    for_survey = models.ForeignKey(Survey, related_name='results')
    def __str__(self):
        return self.name

        '''

