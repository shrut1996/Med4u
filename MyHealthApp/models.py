# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Doctor(models.Model):
    SPECIALITY_CHOICE=(
            
    ('ADDICTION PSYCHIATRIST',"Addiction psychiatrist"),
    ('ADOLESCENT MEDICINE SPECIALIST',"Adolescent medicine specialist"),
    ('ALLERGIST (IMMUNOLOGIST)',"Allergist (immunologist)"),
    ('ANESTHESIOLOGIST',"Anesthesiologist"),
    ('CARDIAC ELECTROPHYSIOLOGIST',"Cardiac electrophysiologist"),
    ('CARDIOLOGIST',"Cardiologist"),
    ('CARDIOVASCULAR SURGEON',"Cardiovascular surgeon"),
    ('COLON ',"Colon "),
    ('CRITICAL CARE MEDICINE SPECIALIST',"Critical care medicine specialist"),
    ('DERMATOLOGIST',"Dermatologist"),
    ('DEVELOPMENTAL PEDIATRICIAN',"Developmental pediatrician"),
    ('EMERGENCY MEDICINE SPECIALIST',"Emergency medicine specialist"),
    ('ENDOCRINOLOGIST',"Endocrinologist"),
    ('FAMILY MEDICINE PHYSICIAN',"Family medicine physician"),
    ('FORENSIC PATHOLOGIST',"Forensic pathologist"),
    ('GASTROENTEROLOGIST',"Gastroenterologist"),
    ('GERIATRIC MEDICINE SPECIALIST',"Geriatric medicine specialist"),
    ('GYNECOLOGIST',"Gynecologist"),
    ('GYNECOLOGIC ONCOLOGIST',"Gynecologic oncologist"),
    ('HAND SURGEON',"Hand surgeon"),
    ('HEMATOLOGIST',"Hematologist"),
    ('HEPATOLOGIST',"Hepatologist"),
    ('HOSPITALIST',"Hospitalist"),
    ('HOSPICE ',"Hospice "),
    ('HYPERBARIC PHYSICIAN',"Hyperbaric physician"),
    ('INFECTIOUS DISEASE SPECIALIST',"Infectious disease specialist"),
    ('INTERNIST',"Internist"),
    ('INTERVENTIONAL CARDIOLOGIST',"Interventional cardiologist"),
    ('MEDICAL EXAMINER',"Medical examiner"),
    ('MEDICAL GENETICIST',"Medical geneticist"),
    ('NEONATOLOGIST',"Neonatologist"),
    ('NEPHROLOGIST',"Nephrologist"),
    ('NEUROLOGICAL SURGEON',"Neurological surgeon"),
    ('NEUROLOGIST',"Neurologist"),
    ('NUCLEAR MEDICINE SPECIALIST',"Nuclear medicine specialist"),
    ('OBSTETRICIAN',"Obstetrician"),
    ('OCCUPATIONAL MEDICINE SPECIALIST',"Occupational medicine specialist"),
    ('ONCOLOGIST',"Oncologist"),
    ('OPHTHALMOLOGIST',"Ophthalmologist"),
    ('ORAL SURGEON ',"Oral surgeon "),
    ('ORTHOPEDIC SURGEON',"Orthopedic surgeon"),
    ('OTOLARYNGOLOGIST',"Otolaryngologist"),
    ('PAIN MANAGEMENT SPECIALIST',"Pain management specialist"),
    ('PATHOLOGIST',"Pathologist"),
    ('PEDIATRICIAN',"Pediatrician"),
    ('PERINATOLOGIST',"Perinatologist"),
    ('PHYSIATRIST',"Physiatrist"),
    ('PLASTIC SURGEON',"Plastic surgeon"),
    ('PSYCHIATRIST',"Psychiatrist"),
    ('PULMONOLOGIST',"Pulmonologist"),
    ('RADIATION ONCOLOGIST',"Radiation oncologist"),
    ('RADIOLOGIST',"Radiologist"),
    ('REPRODUCTIVE ENDOCRINOLOGIST',"Reproductive endocrinologist"),
    ('RHEUMATOLOGIST',"Rheumatologist"),
    ('SLEEP DISORDERS SPECIALIST',"Sleep disorders specialist"),
    ('SPINAL CORD INJURY SPECIALIST',"Spinal cord injury specialist"),
    ('SPORTS MEDICINE SPECIALIST',"Sports medicine specialist"),
    ('SURGEON',"Surgeon"),
    ('THORACIC SURGEON',"Thoracic surgeon"),
    ('UROLOGIST',"Urologist"),
    ('VASCULAR SURGEON',"Vascular surgeon"),
            )
    
    name = models.CharField(max_length=100)
    mobile = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999),MinValueValidator(1000000000)])
    description = models.TextField()
    address = models.TextField()
    speciality = models.CharField(max_length=300,choices=SPECIALITY_CHOICE, default ="SURGEON")
    timings = models.CharField(max_length=12,default="06AM to 06PM")

    def __str__(self):
        return self.name

class Medicine (models.Model):

    name=models.CharField(max_length=50)
    dossage_amt = models.FloatField()
    method  = models.CharField(max_length=2,choices=(('s',"tablet"),('p',"powder"),('ml','liquid ml'),), default ='s')
    frequency = models.IntegerField()
    # Frontend please write number per day on the side of the frequency field
    date = models.DateField(default =datetime.date.today())
    notes = models.TextField()
    doctors = models.ManyToManyField(Doctor)
    # remove the comment after "Disease" model is made
   

    def __str__(self):
        return self.name    
    


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    #mobile = user.(pk=pk).mobile
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(default =datetime.timedelta(days=3))
    time=models.TimeField()
    """ time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
FRONTEND look at this for exit change
    [[[https://stackoverflow.com/questions/34841008/django-timefield-format]]]
"""
    reason = models.TextField()
    
class Disease(models.Model):
    disease_name=models.CharField(max_length=20)
    disease_id=models.AutoField(primary_key=True)
    user=models.ManyToManyField(User)
    bodypart=models.ManyToManyField(Bodypart)
    symptom=models.ManyToManyField(Symptom)
    procedure=models.ManyToManyField(Procedure)
    medicine=models.ManyToManyField(Medicine)

    def __str__(self):
    	return self.disease_name
