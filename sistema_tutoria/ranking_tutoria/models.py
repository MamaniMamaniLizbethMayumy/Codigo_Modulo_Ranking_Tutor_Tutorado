from django.db import models

# Create your models here.

class documentos(models.Model):
	nombre_doc = models.CharField(max_length=45)
	archivo = models.FileField(upload_to='documentos')
	tipo = models.CharField(max_length=15)

	def __str__(self):
		return f'{self.nombre_doc} ({self.archivo.name}) - {self.tipo}'

class rol_usuarios(models.Model):
	nombre_rol = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre_rol

class dato_usuarios(models.Model):
	id = models.CharField(max_length=20, primary_key=True)
	usuario = models.CharField(max_length=45)
	contrasenia = models.CharField(max_length=100)
	nombres = models.CharField(max_length=45)
	apellidos = models.CharField(max_length=45)
	correo = models.CharField(max_length=50, null=True)
	fk_documento = models.ForeignKey(documentos, on_delete=models.CASCADE, null=True)
	fk_rol = models.ForeignKey(rol_usuarios, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return 'usuario: {}, contrasenia: {}, nombres: {}, apellidos: {}, correo: {}'.format(self.usuario, self.contrasenia, self.nombres, self.apellidos, self.correo)

class doc_generados(models.Model):
	doc_generado = models.FileField(upload_to='documentos')
	fk_usuario = models.ForeignKey(dato_usuarios, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.doc_generado.name

class modalidades(models.Model):
	nombre_modalidad= models.CharField(max_length=20)

	def __str__(self):
		return self.nombre_modalidad

class rankings(models.Model):
	ranking = models.IntegerField()

	def __str__(self):
		return str(self.ranking)

class dato_tutores(models.Model):
	id = models.CharField(max_length=20, primary_key=True)
	grado = models.CharField(max_length=10)
	nombres = models.CharField(max_length=45)
	apellidos = models.CharField(max_length=45)
	nro_tutorados = models.IntegerField(null=True, blank=True)
	ses_individuales = models.IntegerField(null=True, blank=True)
	ses_grupales = models.IntegerField(null=True, blank=True)
	referidos = models.IntegerField(null=True, blank=True)
	atendidos = models.IntegerField(null=True, blank=True)
	criterio = models.IntegerField(null=True, blank=True)
	fk_ranking = models.ForeignKey(rankings, on_delete=models.CASCADE, null=True, blank=True)
	fk_usuario = models.ForeignKey(dato_usuarios, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return 'grado: {}, nombres: {}, apellidos: {}, nro_tutorados: {}, ses_individuales: {}, ses_grupales: {}, referidos: {}, atendidos: {}, criterio: {}'.format(self.grado, self.nombres, self.apellidos, self.nro_tutorados, self.ses_individuales, self.ses_grupales, self.referidos, self.atendidos, self.criterio)

class dato_tutorados(models.Model):
	id = models.CharField(max_length=6, primary_key=True)
	nombres = models.CharField(max_length=45)
	apellidos = models.CharField(max_length=45)
	ciclo = models.IntegerField()
	tipo_beca = models.CharField(max_length=45, blank=True)
	modalidad = models.ManyToManyField(modalidades)
	fk_dato_tutor = models.ForeignKey(dato_tutores, on_delete=models.CASCADE, null=True, blank=True)
	fk_ranking = models.ForeignKey(rankings, on_delete=models.CASCADE, null=True, blank=True)
	fk_usuario = models.ForeignKey(dato_usuarios, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return 'nombres: {}, apellidos: {}, ciclo: {}, tipo_beca: {}, modalidad: {}'.format(self.nombres, self.apellidos, self.ciclo, self.tipo_beca, self.modalidad)