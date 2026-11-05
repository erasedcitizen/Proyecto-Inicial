from django.db import models

class Universidad(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Conflicto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subconflicto(models.Model):
    conflicto = models.ForeignKey(
        Conflicto,
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Orientacion(models.Model):
    universidad = models.ForeignKey(
        Universidad,
        on_delete=models.CASCADE
    )

    conflicto = models.ForeignKey(
        Conflicto,
        on_delete=models.CASCADE
    )

    subconflicto = models.ForeignKey(
        Subconflicto,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(max_length=200)

    diagnostico = models.TextField()

    departamento = models.CharField(
        max_length=200,
        blank=True
    )

    recursos = models.TextField(
        blank=True
    )

    pasos = models.TextField()

    def __str__(self):
        return self.titulo